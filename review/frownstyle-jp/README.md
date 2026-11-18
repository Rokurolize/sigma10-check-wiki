# Review package — theme:frownstyle-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:frownstyle-jp — origin EN, population #91 [GOSIGN2-LEDGER (b) row 91]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now bf5df2b0bea19dbc33b7ee56ba5a7b1d4f01bd137ed4bb8f911123a16f1d00a3); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 3 warns / 1 info (pseudo-ref×4, hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 81; GOSIGN2-LEDGER (b) row 91]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — PC-width header broken at 1366 both engines (JP nav absent, wordmark clipped to "IN…", auth buttons overprint theme header) + blank `.open-menu` button + navy-on-navy opened-sidebar overprint; 383–419px sample overflow. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 91, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 91]
- FIX5 re-judgement: item 19 (class F) DISPOSITIONED — FIX5-FUNC §4 (no edit): header CSS L269-313 and L389-423 byte-identical to original L242-286 / L362-396 (both diffs IDENTICAL); the render lane itself recorded that candidate vs shared site chrome attribution could not be settled from screenshots [GOSIGN2-LEDGER-SUPPLEMENT (a) item 19]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:frownstyle-jp.txt sha256:bf5df2b0bea19dbc33b7ee56ba5a7b1d4f01bd137ed4bb8f911123a16f1d00a3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 19 [F] — PC-width header broken at 1366 in both engines (JP nav absent, wordmark clipped to "IN…", auth buttons overprint the theme header), plus a blank `.open-menu` button and navy-on-navy opened-sidebar overprint |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 19: **DISPOSITIONED** (FIX5-FUNC §4, no edit), on the header-identity ground re-derived in the per-theme record below (with one byte-level precision recorded there) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref×4 / hotlink×2 (classes (iii) and (ii)); the 383–419px sample overflow (KB-33/KB-34 families); localize P5 (class (ii) / KB-58), P9 (ruling 2), P11 (sibling / batch-posting class) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:frownstyle | theme:frownstyle-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 9, as recorded in the candidate's credit block (初訳時参照リビジョン: 9, candidate L29) and in review/sources.tsv | — |
| Source of this copy | Mirror store `review-mirrors/orig-frownstyle-rev9.txt`, class COPY, fetched once by the LOCALIZE-S2-B lane at rev 9 | Canonical file `pages/theme:frownstyle-jp.txt`, copied at worktree HEAD 71ac75b |
| Lines / bytes | 1,418 lines / 22,391 bytes | 1,436 lines / 23,698 bytes |
| SHA-256 | 9cbbe22148476d80f2e4801db61c4e8c5b3c664394d852c30af86374bbc48abd | bf5df2b0bea19dbc33b7ee56ba5a7b1d4f01bd137ed4bb8f911123a16f1d00a3 |

Package files: `original.txt` and `candidate.txt` as tabled above; `classification.json` and the skeleton behind this README are from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## Summary

Frownstyle is a Black Highlighter based aesthetic theme by MisterFrown whose CSS ships as four code fragments: a main block and three variant blocks (dark mode, alternate rating module, intro animation) delivered by tail modules under include-parameter gates. The port keeps that whole delivery chain step for step — same four blocks, same gates in render-time text, addresses repointed to the candidate's own draft-host fragments — and adds at the head the BHL base delivery the original page does not carry (its rules presume BHL variables throughout). The documentation body is carried entire and translated. The theme's only blocking item was the broken PC-width header, dispositioned because the operative header CSS is the original's own and the render lane itself recorded that the break could not be attributed to the candidate over shared site chrome — re-derived from this package's two files in the per-theme record, where one byte-level precision on the FIX5 identity claim is recorded. The verdict stamp reads STALE because the usage sweep changed one line after the verdict (commit b5cb724); this package re-judges the current bytes.

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind. The candidate carries one component the original lacks (a head module-css holding the BHL base imports, candidate L7–10) — a supplement, treated in section 3, not a relocation.

- **Provenance route:** derived from the branch original at the reference revision (theme:frownstyle rev 9 on scp-wiki). This is not an R4 production adoption: no production JP counterpart exists in the record for this theme. The evidence is mutually consistent: review/sources.tsv keys the row `standard` with the mirror's SHA-256 equal to this package's original.txt; the candidate's credit block records 初訳時参照リビジョン: 9 (candidate L29); and the sources.tsv note records the first translation at rev 9 with no supersession claim.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 4 |
| DRAFT-HOST | 4 |
| ESCAPED-INCLUDE | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 4 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 4 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 14 |
| TRANS-UNANCHORED | 6 |
| WS-ONLY | 36 |

Counts: 78 blocks, 64 specific, 7 heuristic, 7 residue, 0 skipped (comment text).

## 1. Credit and attribution

- **What:** block B2 (orig L2–5 → cand L4–31) carries BARE-RATE-DEL, CREDIT-PREVIEW, IFTAGS, and TASL-FIELDS in its span. The gate tag localizes (`[[iftags +theme]]` → `[[iftags +テーマ]]`, candidate L5; B1 is the gate's opening line at candidate L1–3, section 3). The original's bare Rate exhibit (original L3–5, `[[>]] [[module Rate]] [[/>]]`) is removed — the KB-09 class: the preview credit module is already rate-bearing, so a second bare Rate double-renders the widget. The candidate's credit block (candidate L22–31, `credit:start-preview` / `credit:end-preview`) carries all eight TASL fields: タイトル FROWNSTYLE (L23), 翻訳責任者 AI (L24), 翻訳年 2026 (L25), 原題 FROWNSTYLE (L26), 著作権者 MisterFrown (L27), 作成年 2024 (L28), 初訳時参照リビジョン 9 (L29), 元記事リンク https://scp-wiki.wikidot.com/theme:frownstyle (L30). The original carries no credit block; its attribution is the intro sentence "Frownstyle is an aesthetic theme by [[*user MisterFrown]]" (original L30) and the CSS banner "Frownstyle Theme by MisterFrown" (original L190, retained at candidate L217). The candidate's 著作権者 field names the same author, in plain-name form — there is no pointer-instead-of-author defect in this package. The credit link's host (scp-wiki.wikidot.com) is the host sources.tsv records for the original. The 翻訳責任者 value is ruling 3's campaign form (AI). Neither file carries a license box (`grep -n 'license-box'` returns nothing on both sides): the original has none, so none was dropped; the theme's licensing rides on the credit block's TASL fields.
- **Why:** P3/T1 — the preview credit module is the rate-bearing form in this environment, and TASL attribution (ruling 3) is what makes the port redistributable.
- **Verify:** Read candidate L22–31 against original L30 and L190; `grep -cn 'module Rate' candidate.txt` returns 0 outside the translated prose mention of the rating module (candidate L58, which names the feature, not the module).
- **Disposition:** No P3 item is charged against this theme in the ledger register; the T1 baseline records no credit-domain error. Standing.

## 2. Includes and components

- COMPONENT-SWAP (B): JP component form (P6, KB-19): a component that exists under both branch names must use the JP form; a kept branch-name include is the flag shape.
  Verify: Resolve the include target on scp-jp; a page that will not exist is the KB-19 failure.
  - B9: orig 66-66 -> cand 92-92 (body -> body)

- INCLUDE-REPOINT (B): Include prefix repoint (P6): the same include, repointed to the JP branch prefix.
  Verify: The included page must exist on the JP side (probed or recorded).
  - B5: orig 44-44 -> cand 70-70 (body -> body)
  - B64: orig 1360-1360 -> cand 1378-1378 (body -> body)
  - B66: orig 1376-1376 -> cand 1394-1394 (body -> body)

- **What:** the tail includes are repointed to the JP prefix with their parameters byte-identical: `component:toggle-sidebar` (original L1378 → candidate L1408, B64's span) and `component:customizable-acs` with its `lang=EN` parameter (original L1380–1384 → candidate L1410–1414, B66's span). The exhibit includes are treated in section 8 (image-block at candidate L76; the ACS exhibit's repoint inside B9's span at candidate L93). The candidate adds no component include the original lacks; the base delivery it adds is an include of the BHL theme page itself, treated in section 3.
- **Why:** P6/KB-19 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): the JP environment resolves the JP component forms; a kept branch-name include would name a page that does not exist here.
- **Verify:** `grep -n 'component:' candidate.txt` returns the credit (L22, L31), image-block (L76), customizable-acs (L93, L1410), and toggle-sidebar (L1408) lines, all under the `:scp-jp:` prefix.
- **Disposition:** No ledger item charges this theme's includes. Standing.

## 3. Delivery and code loading

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B68: orig 1388-1388 -> cand 1406-1406 (body -> body)
  - B69: orig 1398-1398 -> cand 1416-1416 (body -> body)
  - B73: orig 1408-1408 -> cand 1426-1426 (body -> body)
  - B74: orig 1416-1416 -> cand 1434-1434 (body -> body)

- SELF-DELIVERY (A): Self-delivery (P4/T9): the candidate delivers its own CSS from its own page; a theme page importing another page's stylesheet is the flag shape.
  Verify: Every local--code reference in the candidate names the candidate page itself; classify each host line by section 3's rules before judging.
  - B68: orig 1388-1388 -> cand 1406-1406 (body -> body)
  - B69: orig 1398-1398 -> cand 1416-1416 (body -> body)
  - B73: orig 1408-1408 -> cand 1426-1426 (body -> body)
  - B74: orig 1416-1416 -> cand 1434-1434 (body -> body)

- **What:** the original's delivery chain, preserved step for step. The stylesheet ships as four `[[code type="css"]]` blocks (census 4 on each side, counting the typed form): the main block and three variant blocks. The tail of each file is a sequence of `[[module css]]` blocks in render-time text that import the page's own fragments: /1 unconditionally (original L1388 → candidate L1406, inside B68) and /2, /3, /4 each wrapped in a Wikidot comment gate — `[!-- {$dark} --]` (B69), `[!-- {$rate} --]` (B73), `[!-- {$anim} --]` (B74) — with the `[[module Backlinks]]` include repointed alongside (original L1390 → candidate L1408). The gates live in render-time text, where include-parameter substitution reaches them; they are not inside a URL-delivered code block, so they act (the FIX-PARALLEL2 test, REPORT-GOSIGN2-FIX5-FUNC.md §4). The candidate's addresses name its own page's fragments on the draft host (candidate L1416, L1426, L1434), and the fragments resolve to the four blocks in order: the named blocks are the stylesheet blocks themselves, not exhibits. One precision against FIX5-FUNC's "all 4 tail module-css references" phrasing: the /1 reference is an `[[include]]` of a fragment (candidate L1406), while /2, /3, /4 are the `[[module css]]` @imports — the chain is form-identical to the original either way.
- **What (the base supplement):** the original page carries no base delivery at all — its CSS presumes BHL's variables and normalize throughout, supplied in the original's environment by the wiki's site theme. The candidate makes the dependency explicit at the head: an unconditional `[[include :scp-jp:theme:black-highlighter-theme]]` inside a bare `[[iftags]]` (candidate L1–3, block B1), a head `[[module css]]` importing the BHL stylesheet and normalize from scp-jp.github.io (candidate L7–10), and two interwiki-style `[[frame]]` elements at priority 1 and 2 naming the same two stylesheets (candidate L12–20). Nothing is inlined; the base is imported, and the prose declares exactly what the bytes do (candidate L58 states the theme requires Black Highlighter, the original's own statement at original L32, translated). This is the campaign's BHL-base delivery form, not a deviation from the original's topology: the original's topology is "rules that presume BHL", and the candidate delivers that presumption.
- **Why:** P4/T9 and KB-41: self-delivery from the candidate's own page, draft-host form sanctioned at draft stage (class (iii)); the failure prevented is a theme importing another page's stylesheet or silently depending on site chrome for its base.
- **Verify:** `grep -n 'local--code' candidate.txt` returns the three module-css lines plus the L1406 include line, all naming theme%3Afrownstyle-jp; the code-block census (4 = 4) names the blocks those addresses resolve to.
- **Disposition:** The T1 baseline's pseudo-ref×4 are exactly these draft-host self-references — class (iii), recorded, not fixed (section 12).

## 4. Fonts and assets

- FONT-IMPORT (B): Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.
  Verify: KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200).
  - B29: orig 194-196 -> cand 221-223 (code-css -> code-css)

- JPFONT-LOAD (B): JP font load added (P7/T5): a stack-referencing JP family must be loaded somewhere in the delivery.
  Verify: The JP family's @import must sit in the delivered channel, not in an exhibit.
  - B26: orig 187-187 -> cand 214-215 (code-css -> code-css)

- **What:** (1) The original's font program is three fonts.bunny.net loads (original L194–196): Aldrich, Electrolize, Kdam Thmor Pro, Odibee Sans, Orbitron:wght@400..900; Lato:ital,wght@0,400;0,900 / PT Mono / Poppins:wght@600;800; and Oxanium. The candidate re-hosts all three to Google Fonts css2 (candidate L221–223) with the family and axis parameters identical (the css2 spelling of the Lato axis list included). This is a host repoint of the same loads, not a substitution: every family the original loads is loaded by the candidate from the new host, and no family is added or dropped by B29. (2) The JP supplement: Noto Sans JP is loaded at the head of code block 1 (candidate L215, inside B26) — the delivered channel itself — and appended to the three :root stacks (candidate L234–236 against original L207–209; the classifier labels that block CSS-BODY heuristic, and per the standing rule it is narrated here as what it is, a P7 font-stack rewrite). (3) Load/application census, per family, mentions on each side: Aldrich 3 = 3, Electrolize 3 = 3, Kdam Thmor Pro 3 = 3, Odibee Sans 3 = 3, Orbitron 3 = 3, Lato 5 = 5, PT Mono 3 = 3, Poppins 3 = 3, Oxanium 3 = 3; Noto Sans JP 0 → 4 (one load, three stack mentions). Families the original loads but no stack names are in that state identically in the original — an inherited load set, parity, not a port-introduced orphan. (4) Duplication: the file's @import census is 10 lines with no duplicate URL; FIX4-MECH (commit a497307) removed a duplicate Noto Sans JP @import from this file earlier in the campaign (KB-65), and the current bytes carry exactly one. (5) Assets: the logo asset's host repoints from cdn.scpwiki.com to scp-jp.github.io inside the div#extra-div-1 rule (original L233 → candidate L260, the CSS-BODY heuristic block B31, narrated in section 5's terms); the one kept original-host image reference is the hotel.png exhibit's `name=` attribute (candidate L76), the P5/KB-58 class of section 11.
- **Why:** P7/KB-16 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): Japanese text needs a JP face in the stacks, and its load must sit in the delivered channel. P5/KB-04: the family parameter form is what decides whether a load resolves at all.
- **Verify:** `grep -n '@import' candidate.txt` (10 lines) against the same grep on original.txt; per-family mention counts as tabled above.
- **Disposition:** T4's P5 on this theme (kept-host image reference) is DISPOSITIONED as class (ii) / KB-58 in section 11; no font item is charged. Standing on current bytes.

## 5. Header, sidebar, site furniture

none — no signature for this section fired over 78 change blocks, and the ground is the per-theme record: the header rules are the disposition's own subject. The `#header h1`/`h2` and wordmark rules (candidate L269–313) and the `#top-bar` region (candidate L389–423) are byte-identical to the original's apart from one trailing-space blank line (measured in the per-theme record); the header wordmark strings `content: "THE FOUNDATION"` and `content: "INTERNAL FILE STORAGE"` (candidate L297, L305) are kept in English — header/title identity strings, the class ruling 2 puts out of scope, and the localize lane's P9 on this theme is DISPOSITIONED on exactly that ground (section 11). The one furniture-adjacent delta the classifier surfaces, the logo asset's host repoint (block B31), is recorded in section 4. The charged header break itself is the theme's blocking item, treated in section 11 and the per-theme record, not here.

## 6. Text translation

- TRANSLATION-ANCHORED (A): Translation with anchors (P10, KB-18): Japanese localized text replaces English prose at anchored lines.
  Verify: KB-18: anchor tokens and term consistency against the standard glossary (KB-33).
  - B3: orig 9-9 -> cand 37-37 (body -> body)
  - B4: orig 14-18 -> cand 40-46 (body -> body)
  - B7: orig 34-40 -> cand 60-66 (body -> body)
  - B10: orig 70-73 -> cand 96-102 (body -> body)
  - B12: orig 76-79 -> cand 104-108 (body -> body)
  - B14: orig 94-99 -> cand 120-126 (body -> body)
  - B17: orig 105-108 -> cand 132-136 (body -> body)
  - B18: orig 112-114 -> cand 138-142 (body -> body)
  - B20: orig 124-128 -> cand 150-154 (body -> body)
  - B21: orig 130-134 -> cand 156-160 (body -> body)
  - B23: orig 138-144 -> cand 164-170 (body -> body)
  - B33: orig 263-268 -> cand 290-295 (code-css -> code-css)
  - B34: orig 274-279 -> cand 301-306 (code-css -> code-css)
  - B47: orig 594-598 -> cand 621-625 (code-css -> code-css)

- **What:** TRANSLATION-ANCHORED (14 blocks) and TRANS-UNANCHORED (6 blocks: B6, B8, B11, B13, B16, B19) together carry the whole documentation body: the intro (candidate L37–66), the settings documentation (candidate L96–186), and the prose between the code blocks are carried entire and translated. Two of the anchored blocks sit inside the CSS (B33, B34, B47): these are the `content:` strings of the header and sidebar pseudo-elements, and their adjudication is exact — "THE FOUNDATION" and "INTERNAL FILE STORAGE" (candidate L297, L305) are kept in English as identity strings under ruling 2, while the sidebar's `.side-block .heading p` content, a complete prose sentence in the original ("You are currently browsing the internal file storage of the SCP Foundation.", original L598), is translated (candidate L625, 「あなたは現在、SCP財団の内部ファイルストレージを閲覧しています。」) — a sentence is visible prose, not a mark, and it translates. The CSS comments are translated alongside (e.g. candidate L290–295, L301–306 region comments), which is the expected heuristic mass for this theme, resolved by shape in the appendix where they appear as residues. The intro's prose links `[[[theme:blankstyle|Blankstyle]]]` and `[[[theme:foxtrot|Foxtrot]]]` (candidate L56) name pages that serve 200 on scp-jp production (probed 2026-11-17): under the monotypical ground the links stand, recorded here, not flagged. The Navlastyle link in the same sentence keeps the original's scpko host on both sides (original L32 = candidate L58) — a kept cross-branch reference, parity with the original. No mistranslation, term drift, or untranslated reader prose was found in what the candidate carries; the footnote specimen is carried (one `[[footnote]]` on each side, zero `[[footnoteblock]]` on each side — parity, nothing dropped).
- **Why:** P10/KB-18 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): reader-visible text localizes; identity strings stay as marks.
- **Verify:** Read candidate L37–186 against original L9–160; the T5 verdict is cited in section 12.
- **Disposition:** T5 judged this theme FINDINGS on the P9/P11 items only, both DISPOSITIONED in section 11. Standing.

## 7. Links

none — no signature for this section fired over 78 change blocks. Ground: the candidate's external links are the credit's 元記事リンク (candidate L30; host is the original's recorded host, section 1), the two production links probed in section 6 (both 200 on scp-jp), and the kept Navlastyle reference (original host on both sides, section 6). The settings exhibits' escaped includes are section 8; the tail delivery addresses are section 3. No other link required a probe.

## 8. Structure

- ESCAPED-INCLUDE (A): Escaped include exhibit (P9): the settings exhibit's escaped include repoints to the candidate; the include-parameter gates in its text are load-bearing.
  Verify: The exhibit's gate text must still name the candidate page and its parameters.
  - B15: orig 102-103 -> cand 129-130 (body -> body)
  - B22: orig 135-136 -> cand 161-162 (body -> body)
  - B24: orig 145-146 -> cand 171-172 (body -> body)
  - B25: orig 149-150 -> cand 173-174 (body -> body)

- **Exhibit decision, the settings exhibits (B15, B22, B24, B25):** kept, repointed. The four settings exhibits (Dark Mode, Alternate Rating Module, Intro Animation, and the combined form) keep their escaped include lines naming the candidate page (`@@[[include :scp-jp:theme:frownstyle-jp …]]@@`) with their gate parameters intact (`dark="yes"`, `rate="yes"`, `anim="yes"`). The gates those parameters feed are the tail modules of section 3, in render-time text — the exhibit text and the delivery mechanism agree.
- **Exhibit decision, the image-block exhibit (B5 region, candidate L76):** kept. The `component:image-block` include is repointed to the JP prefix, its caption is translated (「ホテルのロビー。」), and its `name=` keeps the original host — the P5/KB-58 disposition of section 11, recorded, not a drop.
- **Exhibit decision, the ACS exhibit (B9 region, candidate L92–93):** kept, repointed (section 2).
- **CSS body:** two blocks carry CSS-BODY. B30 (orig L207–209 → cand L234–236) is the :root font-stack rewrite, narrated as P7 in section 4 per the standing rule. B31 (orig L233 → cand L260) is the logo asset's host repoint inside the div#extra-div-1 rule, recorded in section 4. No CSS rule is dropped anywhere in the four blocks: the tail blank-line and spacer deltas are resolved in the appendix (R5–R7), and the colour census in the per-theme record confirms no colour value changed.
- **Structure census:** code blocks 4 = 4; the documentation sections stand in the original's order; the one content delta at the tail is the original's four `@@@@` spacer lines (original L1383–1386), dropped — resolved as residue R7 in the appendix (inert spacers after the last documentation section, before the delivery tail; nothing they separated is lost).

## 9. Formatting only

- WS-ONLY blocks: 36
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

The 36 WS-ONLY blocks are the file's trailing-space blank lines normalized (the same EN10-era normalization shape as the fish package's, at this file's scale), plus the dropped trailing blank lines at code-block ends resolved in the appendix. Counted here so the churn is not mistaken for content change; the censuses in the per-theme record were run over tokens and rule text, which this whitespace cannot affect — with the one exception the per-theme record names: a single trailing-space blank line inside the header window, which is why that window's identity is stated at declaration level there.

## 10. Porter annotations

none — checked explicitly, because annotations ride inside other blocks: `grep -n 'localization\|\[JP\]\|JP:' candidate.txt` returns nothing, and a read of the added regions (head delivery, credit block, translated comments) finds no porter commentary. The candidate's additions state what they are in their own syntax (the BHL include, the TASL fields); there is no annotation whose truth needed checking. The CSS comments that are translated are the original's own comments carried in translation (section 6), not porter notes.

## 11. Dispositions and exceptions

- **Item 19 (class F), the broken PC-width header — DISPOSITIONED.** The full argument is the per-theme record below; its one-sentence form is that the operative header CSS is the original's own (byte-identical at declaration level, and byte-exact for the #top-bar window), the candidate's additions touch no header rule, and the render lane itself recorded that the break could not be attributed to the candidate over the test wiki's shared site chrome. [GOSIGN2-LEDGER-SUPPLEMENT.md item 19; REPORT-GOSIGN2-FIX5-FUNC.md §4]
- **The 383–419px sample overflow — DISPOSITIONED in the ledger, not charged to the theme.** The sample-page overflow band is the mobile width family (KB-33/KB-34), shared site-chrome ground [GOSIGN2-LEDGER.md §(c2), frownstyle row].
- **P5 (kept-host image reference) — DISPOSITIONED.** The hotel.png exhibit's `name=` keeps the original host: class (ii) posting matter / deferred asset hosting (KB-58) [GOSIGN2-LEDGER.md §(c3), LOCALIZE-S2-B frownstyle row].
- **P9 (header/title language) — DISPOSITIONED.** The wordmark strings kept in English are identity strings under ruling 2 (section 5) [GOSIGN2-LEDGER.md §(c3)].
- **P11 (sibling/batch-posting class) — DISPOSITIONED** [GOSIGN2-LEDGER.md §(c3)].
- **The T1 pseudo-ref×4 / hotlink×2 — classes (iii) and (ii), recorded not fixed:** the draft-host self-references of section 3 and the kept-host references of sections 4 and 8, which resolve at posting.
- **The verdict stamp's STALE** is explained, not a disposition: the candidate changed after the verdict by exactly one line (the usage sweep's posting-name line, commit b5cb724, candidate L39). The re-judgement on the current bytes is this package; the header ground of item 19 does not touch the changed line.

## 12. Verification

- **T1 (source check):** baseline 2026-11-16: exit 1, 6 errors / 3 warns / 1 info — the errors are pseudo-ref×4 and hotlink×2 [T1-ROWS row 81]. FIX5-FUNC ran the checker before and after its adjudication: 6 / 3 / 1 → 6 / 3 / 1 (no edit). The candidate's only later change is the sweep line (candidate L39), itself one of the sanctioned self-reference forms. No class (i) error stands against this candidate.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-1 (RENDER-S2-B, EN10)]. The one candidate-specific item is item 19 (dispositioned, section 11); the lane's remaining line is the cross-cutting overflow disposition of section 11. No re-render was run for this package: the render record is the lane's, cited, not re-measured here — and the lane's own attribution caveat is part of that record (per-theme record).
- **T4 (localize patterns + follow-up):** FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 91, source LOCALIZE-S2-B]: the P5 kept-host image reference, DISPOSITIONED in section 11. The mirror in this package is the reference revision the follow-up state rests on (sources.tsv records the first translation at rev 9, no supersession claim).
- **T5 (translation text):** FINDINGS on the P9/P11 items only, both DISPOSITIONED in section 11 [LOCALIZE-ROWS row 91].
- **This package:** `python3 review/build_review.py --check` — the verdict stamp regenerates identically from the two files in this package, and the package is not in the pre-existing stale set (the refresh-3 population: 79 packages at base 71ac75b, set-compared). The censuses in the per-theme record were re-derived from this package's two files while this README was written, not transcribed from the supplement.

## Per-theme record

### The header-identity disposition (ledger §(e) item 19)

The charge, as the ledger states it: item 19 [F] — at PC width (1366) in both engines the header is broken (JP nav absent, the wordmark clipped to "IN…", the auth buttons overprint the theme header), the `.open-menu` button is blank, and the opened sidebar overprints navy-on-navy; and the render lane's own record adds the sentence the disposition turns on: "attribution to candidate vs shared test-wiki site chrome cannot be settled from screenshots" [GOSIGN2-LEDGER.md §(e) item 19]. Class F charges a candidate-side functional defect, so the question is again narrow: does the candidate's header CSS differ from the original's in any rule that could produce the break? The supplement's ground is identity: "header CSS candidate L269–313 / L389–423 byte-identical to original L242–286 / L362–396; both diffs IDENTICAL" [GOSIGN2-LEDGER-SUPPLEMENT.md (a) item 19; REPORT-GOSIGN2-FIX5-FUNC.md §4]. Re-measured from this package's files:

1. **Window 2 (the #top-bar region).** Candidate L389–423 = original L362–396: byte-identical, 35 lines, 531 bytes, SHA-256 `f64ef52d178e184b1c2fab1d174fb7defd00d78ed59d57ca6f44bfc1d8c8d6d9` on both sides.
2. **Window 1 (the #header h1/h2 and wordmark rules).** Candidate L269–313 against original L242–286: every non-blank line is byte-identical, and exactly one byte differs in the whole window — original L275 is a blank line carrying one trailing space, candidate L302 is the same blank line empty (window hashes `bc4f3d84…` at 549 bytes against `96cb89f8…` at 548 bytes). This is the file's WS-ONLY shape (section 9), not a rule difference: at declaration level the identity FIX5-FUNC claims holds exactly.
3. **Whole-file corroboration.** The colour-token census over both files: 31 tokens on each side, multisets identical — no colour anywhere in the file changed, which covers the navy-on-navy sidebar half of the charge as well. A brace-depth scan of both files (max depth 2, final depth 0, no negative excursion) excludes a displaced brace re-scoping the header rules.
4. **The candidate's additions touch no header rule.** Everything the candidate adds stands outside both windows: the head base delivery (candidate L1–20), the credit block (L22–31), and the tail address repoints (section 3). The header the candidate renders is built from the original's rules plus the BHL base the original presumes.

The conclusion the identity licenses: with the operative CSS identical, the break the T3 walk photographed cannot be a candidate-authored rule difference; combined with the lane's own attribution caveat, the remaining explanation is the shared test-wiki site chrome the lane named. Disposition: **DISPOSITIONED, no edit** [GOSIGN2-LEDGER-SUPPLEMENT.md item 19; FIX5-FUNC §4].

**The one precision this package records against the supplement:** FIX5-FUNC's phrase "both diffs IDENTICAL" is exact for window 2 and exact at declaration level for window 1, but not byte-exact for window 1 — one trailing-space byte differs (original L275 vs candidate L302). The precision does not touch the disposition's ground (no rule, value, or selector differs), and it is recorded here rather than smoothed over because the class's standard is that identity claims are stated at the precision the bytes support.

### Second-reviewer walk

The class asks for the disposition to be walked once more from the third-party perspective: is the ground stated in terms a reader who did none of the work can check, and does it hold? The ground here is two named windows, a whole-file census, and a depth scan, every one reproducible from `original.txt` and `candidate.txt` alone. The walk re-ran each measurement: window 2 held byte-exact; window 1 held at declaration level with the single whitespace byte named above; the census and scan held exactly. The walk also checked the disposition's second leg — the attribution caveat — against the ledger text, and it is the lane's own sentence, not the supplement's invention. One limit is stated for completeness: identity of the header CSS proves the candidate authored no header rule difference; it does not by itself prove which shared-chrome element produced the photographed break — the disposition records the break as not-the-candidate's on the combined ground (identity plus the lane's caveat), which is the ground the supplement states. Walk outcome: **the disposition is sound as stated, with the window-1 precision recorded.**

### Multi-wave provenance

The candidate's current state is the product of successive waves, not one pass: the Stage 2 EN10 port (commit c210f75) produced the file the localize lane audited (LOCALIZE-S2-B, row 91, FINDINGS on the dispositioned P-items); commit 1869877 (FIX-CREDIT-D, translator attribution normalization over 163 files) settled the credit block's campaign form (section 1); commit a497307 (FIX4-MECH) removed the duplicate Noto Sans JP @import (KB-65, section 4); FIX5-FUNC closed the theme's only blocking item as a no-edit disposition, so no FIX5 commit touches this file; and the usage sweep (commit b5cb724) repointed the usage self-include to its posting name (candidate L39) — the one-line delta behind the stamp's STALE. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(b) row 91, §(c2) (render row), §(c3) (localize row), §(e) item 19; GOSIGN2-LEDGER-SUPPLEMENT.md item 19; REPORT-GOSIGN2-RENDER-S2-B.md (EN10, frownstyle); REPORT-GOSIGN2-FIX5-FUNC.md §4; T1-ROWS row 81; LOCALIZE-ROWS row 91. The go-sign over that record is what the Status block certifies.

## Appendix — residue blocks

### Residue R1 — B8 (residue; orig 42-43 -> cand 68-69, body -> body)
- Removed first line: + Settings
- Added first line: + 設定
- Note: heading lines only (orig 2 lines / cand 2 lines)

Resolution: assigned to section 6. B8 is the settings section's heading pair (`+ Settings` / `++ Frownstyle Settings` → `+ 設定` / `++ Frownstyleの設定`): a heading translation, the P10 class of section 6. The classifier gave it no signature because a bare heading pair carries no anchor token; no new signature is proposed — heading translations are a known shape the anchored/unanchored pair already covers in substance.

### Residue R2 — B19 (residue; orig 118-119 -> cand 144-145, body -> body)
- Removed first line: + Black Highlighter Theme Settings
- Added first line: + ブラックハイライターテーマの設定
- Note: heading lines only (orig 2 lines / cand 2 lines)

Resolution: assigned to section 6, same shape as R1: the BHL settings section's heading pair, translated.

### Residue R3 — B65 (residue; orig 1348-1348 -> cand 1365-1365, code-css -> code-css)
- Removed first line: }
- Added first line: }

Resolution: assigned to section 9. B65 is one of the four `}`-only residue pairings over the code blocks' ends; measured directly from the bytes, the candidate drops exactly one trailing blank line after the final `}` of each of the four code blocks (original L1079, L1249, L1351, L1378), and identical `}` lines pair ambiguously in a diff, so the four residues are one shape rather than four distinct loci. For code block 1 (original L188–1080) the line count is unchanged (893 lines on each side) because the candidate's added JP import (section 4) offsets the drop inside the same block. No rule is affected; the `}` lines themselves are identical.

### Residue R4 — B67 (residue; orig 1366-1366 -> cand 1383-1383, code-css -> code-css)
- Removed first line: }
- Added first line: }

Resolution: assigned to section 9, same shape as R3: one of the four block-end trailing-blank drops; code block 2 (original L1082–1250) is one line shorter in the candidate (169 → 168). No rule is affected.

### Residue R5 — B70 (residue; orig 1394-1394 -> cand 1412-1412, body -> body)
- Removed first line: }
- Added first line: }

Resolution: assigned to section 9, same shape as R3: one of the four block-end trailing-blank drops; code block 3 (original L1252–1352) is one line shorter in the candidate (101 → 100). No rule is affected. (B70's span also touches the tail include region; the include repoints themselves are section 2's blocks B64/B66.)

### Residue R6 — B71 (residue; orig 1404-1404 -> cand 1422-1422, body -> body)
- Removed first line: }
- Added first line: }

Resolution: assigned to section 9, same shape as R3: one of the four block-end trailing-blank drops; code block 4 (original L1354–1379) is one line shorter in the candidate (26 → 25). No rule is affected.

### Residue R7 — B72 (residue; orig 1382-1386 -> cand 1400-1400, body -> body)
- Removed first line: ----
- Added first line: [[include :scp-jp:component:toggle-sidebar]]

Resolution: assigned to section 8. B72 is the original's tail spacer run: a `----` rule followed by four `@@@@` lines (original L1382–1386) standing between the last documentation section and the delivery tail. The candidate drops the four `@@@@` spacers (keeping a `----` rule in the same region, candidate L1400 area); the spacers are inert layout filler, and everything they separated — the documentation above and the delivery tail below — is present on both sides. Recorded as a kept-content check, not a silent drop: the only lines in either file with no counterpart are these four spacers.

## License and attribution

- **Title:** FROWNSTYLE
- **Author:** MisterFrown
- **Source:** https://scp-wiki.wikidot.com/theme:frownstyle — revision 9
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
