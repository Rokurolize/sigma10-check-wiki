# Review package — theme:old-money-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:old-money-theme-jp — origin EN, population #115 [GOSIGN2-LEDGER (b) row 115]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now e32b7933bb8126501dc97c45d44777403259b27c092575a33bc7a08dfdae149c); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 10 errors / 1 warn / 1 info (pseudo-ref×10); standing classes dispositioned in register c1 [T1-ROWS row 115; GOSIGN2-LEDGER (b) row 115]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host; T3 REAL FINDING: sample "15. コンテンツパネル" notice panel and left/right column panel body text render near-white #F7F8F9 on light-gray/white #F4F4F4, effectively unreadable (chromium 1366 + 375, webkit 1366 + 375); broken OldMoney_Logo.png = deferred asset. [RENDER-ROWS-RERUN16 (EN15) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (EN15)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 115, source LOCALIZE-S2-B]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 115]
- FIX5 re-judgement: item 21 (class E) DISPOSITIONED — FIX5-CONTRA (no edit, no commit): fg #F7F8F9 / bg #F4F4F4 identical composition in the original; the only delta is the sanctioned BHL host swap to the JP distribution [GOSIGN2-LEDGER-SUPPLEMENT (a) item 21]
- Computed against: canonical commit b4109ab7758a2904b5dbfff500e1438718099212; candidate file pages/theme:old-money-theme-jp.txt sha256:e32b7933bb8126501dc97c45d44777403259b27c092575a33bc7a08dfdae149c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (batch R-disp-9 lane, 2026-11-17)
Candidate: review/old-money-theme-jp/candidate.txt (sha256 2d723e4d1e38d3b3baa1fa02bfd5d6a0e48f11e6756974f3ccbe2cf4a962c732)
Original: theme:old-money-theme — scp-wiki, revision 89 (sha256 09df9555eee80c82777bf8866c2a29566e9b1d4cc2354118fd1e4279bb95061e)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

| | |
|---|---|
| Original mirror | `review/old-money-theme-jp/original.txt` — 34,484 bytes, 741 lines; SHA-256 equals the sources.tsv row (mirror store `orig-old-money-theme-rev89.txt`, COPY class) |
| Candidate | `review/old-money-theme-jp/candidate.txt` — byte-identical copy of `pages/theme:old-money-theme-jp.txt` (38,369 bytes, 775 lines) |
| Diff | Tier 1: +174 / −146 lines (see diff.md) |
| Classification | 66 change blocks: 43 specific, 20 heuristic, 3 residue, 0 skipped (comment text) |
| Disposition re-derived | Ledger item 21 [E] (sample-panel contrast) — DISPOSITIONED by FIX5-CONTRA; ground re-measured on the package bytes and confirmed (per-theme record below) |
| Defect flags | F1 — the original head module's two inline .scp-image-block rules are absent from the candidate and are not subsumed by the base (per-theme record) |

## Provenance

- Route: derived from the original at the reference revision. The mirror is the LOCALIZE-S2-B lane's source cache (`gosign2-lanes/lane-oc-gs-localize-s2-B/orig-old-money-theme.txt`), hash-verified into the mirror store as a COPY.
- The sources.tsv note for this row is empty; there is no supersession claim to check against a follow-up artifact.

## Summary

A Black Highlighter (BHL) based EN theme. The port keeps the theme's single code block and its whole documentation body, moves the BHL stylesheet imports from the head module into the code block with the host swapped to the JP BHL distribution, replaces the Adobe Fonts (Typekit) program with an annotated Google Fonts substitution plus JP font loads, re-hosts the theme's own assets to the draft host, and adds the preview credit block and license box. Every colour value is unchanged: the whole-file colour censuses of the two sides are identical, which is the byte-level ground of the theme's one blocking item (item 21, the sample-panel contrast disposition).

## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 11 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 3 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 18 |
| WS-ONLY | 7 |

Counts: 66 blocks, 43 specific, 20 heuristic, 3 residue, 0 skipped (comment text). Sections below are written from the classifier's per-block label sets, so a section can carry a class the skeleton listed under a different section's block.

## 0. Header / provenance

- Theme fullname: theme:old-money-theme-jp. Original: theme:old-money-theme, EN branch original on scp-wiki, reference revision 89 (first-translation revision). Candidate file: pages/theme:old-money-theme-jp.txt.
- Provenance route: derived from the original at the reference revision (see Provenance above); no production JP counterpart adoption (not an R4 row).
- Verdict: GOSIGN2-LEDGER (b) row 115: T1 FINDINGS (classified), T2/T3 FINDINGS, T4 PASS, T5 PASS, overall NOT PASS — OPEN items (e) at ledger time. The theme is one of the 17 rerun themes, so the stamp's T2/T3 verdict comes from RENDER-ROWS-RERUN16 (EN15) under supersession rule S1. The single (e) item, 21 [E], was re-judged DISPOSITIONED by the supplement (FIX5-CONTRA, no edit); sources.tsv verdict PASS.

## 1. Credit and attribution

- What: CREDIT-PREVIEW and TASL-FIELDS fire inside B5 (orig L20-26 → cand L20-31): the credit:start-preview pair at cand L22-31 carries the eight ruling-3 fields. 著作権者 names a person, [[*user Woedenaz]] (cand L27); 作成年 2019; 初訳時参照リビジョン 89; 元記事リンク names https://scp-wiki.wikidot.com/theme:old-money-theme, the host recorded in sources.tsv. BARE-RATE-DEL fires in the same block: the original's bare Rate at orig L24-26 ([[>]] [[module Rate]] [[/>]]) is removed; the preview credit module is rate-bearing (KB-09). LICENSE-BOX fires in B65: the license box at cand L751-773 with |author=Woedenaz, carrying four entries (OldMoney_Logo.png; OldMoney_Divider.png; deco-pattern.png / goldfoil.png; the substitute fonts). The three image entries state that the original records no author or license for them, with the confirm-with-the-author-before-posting note; the font entry records the substitution of section 4 and the SIL Open Font License of the substitutes.
- Why: P3/T1 block swap and the ruling-3 TASL record; KB-09 (a second bare Rate beside the rate-bearing preview credit double-renders the widget); KB-63/KB-60 (license box in its settled JP form).
- Verify: grep the candidate for credit:start-preview / credit:end-preview / license-box-backend / license-box-end (one pair each); grep both files for [[module Rate]] (original 1, candidate 0); the credit source link's host against sources.tsv (scp-wiki.wikidot.com on both).
- Disposition: ledger (c3) records P3 credit fields FIXED (credit waves; checker-verified) for this theme; the bytes agree (fields present, author named in both carriers). No credit disposition stands against the theme. T7 credit CSS: neither side carries credit-button CSS of its own (grep creditButton: 0 in both files); the credit furniture's styling is the base/site layer's on both sides.

## 2. Includes and components

- What: IFTAGS fires twice: B1 (orig L1-7 → cand L1), the head restructure in which the candidate's base include takes the file's first line, and inside B5, where the gate itself localizes: [[iftags +theme]] (orig L1) → [[iftags +テーマ]] (cand L20), closing at cand L775. INCLUDE-REPOINT fires twice: B3 (orig L15 → cand L6-7), the priority-1 interwiki frame's target repointed from the EN BHL host to the JP distribution (section 3), and B7 (orig L32 → cand L37), the theme-squares include :scp-wiki:component:theme-squares → :scp-jp:component:theme-squares, its colour parameters carried unchanged (section 9 for their trailing-space trims). The candidate's first line, [[include :scp-jp:theme:black-highlighter-theme]] (cand L1), is the production BHL page include, the population's settled head form for BHL-based candidates (theme:ashes-to-ashes-jp carries the identical line at its L1); the original carries no base include line, its BHL arriving by direct stylesheet @import (orig L3-4). The usage exhibit teaches the same two-include form in :scp-jp: names (cand L79-80).
- Why: P2/T2 tag localization (KB-08); P1 include repoints; the base is delivered, not inlined, in both versions.
- Verify: include census on both files (each live include occurs once per side; the candidate's second :scp-jp:theme:black-highlighter-theme occurrence is the @@ exhibit at cand L79, not a duplicated live include).
- Disposition: no include disposition is recorded against this theme; the (c3) P1 item is DISPOSITIONED as the posting-procedure convention class, which the exhibit form above follows.

## 3. Delivery and code loading

- What: topology changes shape without changing what is delivered. Original: head module-css (orig L2-14) importing the two BHL stylesheets from nu-scptheme.github.io plus two inline rules; code-css (orig L174-731) delivered by a tail module-css (orig L735-737) importing own /1 from scp-wiki.wdfiles.com, with the priority-3 frame naming the same address (orig L738-741); frames priority 1/2 name the two BHL files (orig L15-23). Candidate: head module-css (cand L3-5) importing own /1 from the draft host only; code-css (cand L181-748) whose head imports the two BHL stylesheets from scp-jp.github.io (cand L182-183) ahead of the font loads; frames priority 1/2 name the JP BHL files (cand L7-14), priority 3 names own /1 (cand L15-18); the production base include stands at cand L1. SELF-DELIVERY fires in B2 and B4; DELIVERY-HOST in B4 (the BHL host swap, nu-scptheme.github.io → scp-jp.github.io, the JP distribution of the same BHL CSS); DRAFT-HOST fires 11 times (B2, B4, B14, B54, B57-B63): the candidate's own delivery address and its asset URLs (logo, divider, goldfoil, deco-pattern) on sigma10-jp-test.wdfiles.com/local--files/theme%3Aold-money-theme-jp/. One asset's folder changes name as well as host: the hr::after divider at orig L603 names local--files/component:old-money-theme/, the candidate's corresponding URL (cand L621) names its own page folder theme%3Aold-money-theme-jp. B66 (orig L735-741 → deleted at the tail) carries the EXHIBIT-RESTRUCTURE label, a false fire: no exhibit is involved; the tail module and priority-3 frame lines are deleted because the head module and the priority-3 frame at cand L15-18 carry their function. Brace-depth scan: both files' CSS ends at depth 0 and never goes negative.
- Why: P4/T9 host and local--code repoints (KB-41 draft-host form, class (iii)); the frame priority stack is preserved 1/2/3 in the original's order (KB-07).
- Verify: the candidate holds exactly one code block (cand L181, 566 content lines), so its /1 address names the stylesheet itself, not an exhibit; the FIX-CODEADDR census shapes (a named small exhibit, a renumbered stylesheet) do not occur. Compare the frame sets: three frames each side, priorities 1, 2, 3.
- Disposition: the draft-host delivery lines are class (iii) draft-stage form (KB-41), recorded in section 11, not fixed. Flag F1 belongs to this section's restructure and is stated in the per-theme record: the head module's two inline rules (orig L5-13) have no counterpart anywhere in the candidate's delivery chain.

## 4. Fonts and assets

- What: FONT-IMPORT and JPFONT-LOAD fire in B53 (orig L175 → cand L182-193). The original code block opens with one load, the Adobe Fonts (Typekit) stylesheet https://use.typekit.net/nxg5itx.css (orig L175), which serves the theme's three faces (Ivymode, Turnip, Pennsylvania). The candidate's code block opens with the two BHL imports (section 3), then three Google Fonts substitute loads (Bodoni Moda, EB Garamond, Courier Prime; cand L188-190), then Noto Sans JP and Noto Serif JP loads (cand L192-193). CSS-BODY's single block, B55 (orig L193-198 → cand L211-216), is the P7 font-stack rewrite the classifier labels heuristically: --body-font and --UI-font become "EB Garamond", "Noto Serif JP", serif; --header-font and --title-font become "Bodoni Moda", "Noto Serif JP", serif; --mono-font becomes "Courier Prime", "Noto Sans JP", monospace. HEADERVAR fires in B54 on the --logo-image URL re-host (orig L190 → cand L208, section 5). Load/apply census: every face named in the candidate's stacks is loaded in the same code block; no load is duplicated; no loaded face is unapplied. Assets: the P5 re-hosts of section 3; the theme-squares colour data is unchanged (section 9).
- Why: P7/T5 font supplement (KB-16) and the substitution of a font program that cannot be carried: the candidate states the ground in-file, twice (the prose translator's note at cand L174 and the CSS comment at cand L185-187): Typekit has no hotlink exception in the JP environment and the faces themselves cannot be redistributed, so near-matching Google Fonts faces substitute, with the JP faces appended for Japanese text.
- Verify: grep @import in both code blocks (original 1, candidate 7 lines: 2 BHL + 3 substitutes + 2 JP); read the five stacks at cand L211-215 against the loads at cand L188-193.
- Disposition: the substitution is the porter's recorded judgment, annotated in the candidate itself with its licensing ground; it is not an unrecorded wholesale substitution. The broken OldMoney_Logo.png render state is a separate disposition (KB-58 deferred asset, section 11).

## 5. Header, sidebar, site furniture

- What: HEADERVAR fires once, in B54 (orig L190 → cand L208): --logo-image's URL re-hosted to the draft host, the variable and its role unchanged. No header, sidebar, or top-bar rule changes: the candidate's furniture rules are the original's, line for line, in the unchanged body of the code block. --theme-name keeps the identity string "Old Money Theme" (cand L204, = orig L186) and --theme-id "old-money-theme" (cand L202).
- Why: P9/T6 variables carried; header and title language is out of scope for migration correctness (2026-11-16 ruling 2), and names functioning as marks stay as identity strings.
- Verify: grep --theme- and --logo-image in both files; the code-block rule census outside the head region is empty (the diff's code-css blocks are B53-B55 at the head and the DRAFT-HOST single-line URL swaps).
- Disposition: none recorded against this section.

## 6. Text translation

- What: TRANSLATION-ANCHORED fires 18 times and TRANS-UNANCHORED 22 times, together the whole documentation body: the Theme Colors heading (B6), the usage note and install cluster (B17-B20), the examples (horizontal rule, titles collapsible, tabview with its long-tab and empty-tab specimens, blockquote, table; B21-B51), and the font specimen lines (B51, cand L169-171), which also carry the substitution glosses (「JP版ではEB Garamondで代替」 and parallels). Residue B16 (+ Usage → + 使用方法）, B18 (the BHL note heading seam), B15 (Old Money Logo → Old Moneyロゴ caption), and heuristic B19/B20/B29 are members of this mass, assigned in the appendix. COMMENT-TEXT fires inside B53: the S-CSS-P banner comments inside the code block stay in English as carried text (R1 in-CSS text), while the added Japanese comment is the porter annotation of section 10. The theme-squares colour names (Husk, Sweet Corn, Wild Sand, ...) stay in English on both sides: they are the component's display labels for the original's palette, carried as data.
- Why: P10 body/usage/sample translation (KB-18); R1 in-CSS text stated separately from reader-visible text.
- Verify: read the pairs in diff.md; the anchors (heading levels, leading tokens, component parameters) confirm the pairings one-to-one.
- Disposition: ledger (b) row 115 records T5 PASS for this theme; no translation disposition stands.

## 7. Links

- What: no LINK-REPOINT signature fired. Two links deserve a stated ground. The usage note's prose link [[[theme:black-highlighter-theme|詳しくはこちらを参照してください]]] (cand L74) keeps the original's target (orig L73): in the JP environment that name is the production BHL page, the very page the candidate includes at cand L1, so the link resolves to a serving page; it stands on the production-existence ground, recorded, not edited. The credit block's 元記事リンク (cand L30) names the recorded original host (section 1). No other prose links exist in the file.
- Why: P11 repoints apply to targets with JP counterparts; a target that is itself the JP production page is not drift.
- Verify: the candidate's L1 include and L74 link name the same page; sources.tsv records the original URL's host as scp-wiki.wikidot.com, matching cand L30.
- Disposition: none. (An inbound reference exists from another candidate: the-track-changers-jp's prose link was repointed to theme:old-money-theme-jp under its own item 94; that is that package's record, not this file's change.)

## 8. Structure

- What: EXHIBIT-RESTRUCTURE fires four times and all four are adjudicated here. B3 (orig L15 → cand L6-7) and B7 (orig L32 → cand L37) are include repoints inside the head furniture and the theme-squares exhibit, not exhibit drops (the classifier's known false-fire on repoints inside exhibit regions). B5 is the head-zone restructure of sections 1-2. B66 is the tail delivery restructure of section 3. Exhibit census: theme-squares panel, logo image block, usage note and install cluster, titles collapsible, tabview (long tab and six empty tabs), blockquote, table, font specimens, and the code exhibit are all present at the aligned positions. CSS-BODY's only block is B55, the font stacks (section 4). The gate span differs in shape: the original's gate opens at orig L1 (its head module inside the gate, its tail module and frame outside, orig L735-741); the candidate's delivery furniture stands above its gate (cand L1-18), the gate opening at cand L20 and closing at cand L775, the file's last line. Both forms deliver the stylesheet ungated in practice, and the candidate's shape is the population's standard candidate form. The footnoteblock stands on both sides (orig L733, inside its gate after the code collapsible; cand L178, before the source-code collapsible): neither file carries a live [[footnote]] (grep count 0 on both sides), so it is carried furniture in both versions, its position moved with the source-code section's restructure (B52).
- Why: R3 exhibit restructuring needs a stated ground per block; the localize.md closing rule (variable names, selectors, channel order preserved) is the structure contract.
- Verify: the exhibit census above, read off diff.md; grep -n footnoteblock and footnote on both files (1 and 0 on each side).
- Disposition: no exhibit disposition is recorded against this theme.

## 9. Formatting only

- What: WS-ONLY fires 7 times: B8-B13, the theme-squares parameter lines whose original values carry trailing spaces ("Sweet Corn ", "Wild Sand ", "Alto ", "Yellow Metal ", "Fuel Yellow ", "Lisbon Brown "), trimmed in the candidate with the values otherwise unchanged; B56, a blank-line pair inside the code block. No re-indentation blocks pair up.
- Why: R7 whitespace churn is stated so a reviewer can skip it and so the follow-up-diff hazard is on record.
- Verify: the seven blocks in diff.md are whitespace-only by construction of the label.
- Disposition: none.

## 10. Porter annotations

- What: ANNOTATION fires once, inside B65 (the license-box block): the font entry's 訳注 at cand L771 restates the substitution of section 4. Two further annotations ride inside other labeled blocks and are recorded here explicitly. The prose translator's note at cand L174 (inside B52): states that the original uses Adobe Fonts (Typekit) Ivymode / Turnip / Pennsylvania, that Typekit has no hotlink exception in the JP environment and the faces cannot be redistributed, and that the JP form substitutes near-matching Google Fonts faces with Noto Serif JP / Noto Sans JP appended. The CSS comment at cand L185-187 (inside B53) states the same mapping face by face (Ivymode→Bodoni Moda / Turnip→EB Garamond / Pennsylvania→Courier Prime). Both claims check against the bytes: the loads at cand L188-193 and the stacks at cand L211-215 are exactly the faces the notes name.
- Why: R2 additions are listed so they are never mistaken for original content or for translation.
- Verify: read cand L174 and L185-187 against cand L188-193 and L211-215.
- Disposition: none; both annotations are true against the candidate's own bytes.

## 11. Dispositions and exceptions

- Item 21 [E] (sample-panel contrast): DISPOSITIONED by FIX5-CONTRA — re-derived in the per-theme record below.
- (c2) RERUN16 (EN15): page runtime-hotlink, DISPOSITIONED as environment-layer (KB-40); sample credit-modal and page-overflow 337px@320 + 389px@375 chromium / 416px@320 + 419px@375 webkit, DISPOSITIONED in the cross-cutting families (KB-32; KB-33/KB-34); broken OldMoney_Logo.png, DISPOSITIONED as a deferred asset (KB-58; owner decision 2026-11-16) [GOSIGN2-LEDGER (c2)].
- (c3) P1 DISPOSITIONED (posting-procedure convention class); P10 DISPOSITIONED (lane-recorded severity / specimen class) [GOSIGN2-LEDGER (c3)].
- The candidate's own draft-host delivery and asset lines (section 3) are class (iii) draft-stage form (KB-41): recorded here, not fixed; posting rewrites them (class (ii)).
- HTTP-KEPT: the classifier derives 2 instances, at cand L329 and L342 — the --mask-image data-URI SVGs, whose "http" strings are the W3C namespace declarations (xmlns / xmlns:xlink) inside the data URIs. That is the signature's known false-fire on data URIs, resolved here; no kept hotlink stands behind it.

## 12. Verification

- T1: FINDINGS (classified) per the stamp's baseline (GOSIGN2-LEDGER (b) row 115). T2/T3: FINDINGS per RERUN16 (EN15), supersession rule S1; the (c2) dispositions and item 21 are section 11's record. T4: PASS; T5: PASS (same row).
- Lane re-runs (2026-11-17, this package's bytes): original SHA-256 against sources.tsv (equal); candidate byte-identity against pages/theme:old-money-theme-jp.txt (cmp, equal); whole-file colour censuses (hex multiset equal; rgb-triple multiset equal; #F7F8F9 and the 247,248,249 triple absent from both files); the four sample-panel rules extracted and compared (byte-identical); brace-depth scans (end 0, min 0, both files); include, footnote, and creditButton censuses; the base-subsumption probe behind flag F1 (the JP BHL stylesheet fetched once from scp-jp.github.io and its .scp-image-block rules read; the EN distribution fetched once for comparison). Package acceptance (build_review.py --check set comparison, classify freshness) is recorded in the batch report BATCH-RDISP9.md.

## Per-theme record — FIX5 item re-derived

### Item 21 [E] — DISPOSITIONED (FIX5-CONTRA, no edit, no commit)

- The charge: sample content panels: body text #F7F8F9 on #F4F4F4 (contrast ~1.0), both engines; a RERUN16 T3 real finding (checklist section 1), a confirmed KB-28 instance. At ledger time no fix wave had corrected a KB-28 binding and no original-faithful ground was recorded.
- The disposition's ground (GOSIGN2-LEDGER-SUPPLEMENT, item 21): fg #F7F8F9 / bg #F4F4F4 identical composition in the original; the only delta is the sanctioned BHL host swap to the JP distribution.
- Re-measurement on this package's bytes (2026-11-17): (a) neither file contains the charged pair as text: grep counts for #F7F8F9 and for the 247,248,249 triple are 0 in the original and 0 in the candidate, so the pairing is not a declaration either file makes; it is composed at render from the theme's variables and the base BHL stylesheet. (b) The theme's own colour data is identical on both sides: the whole-file hex census and the rgb-triple census are equal as multisets, and 244,244,244 (the charged background, #F4F4F4) occurs exactly 3 times on each side in the same three roles (--pale-gray-monochrome, --light-pale-gray-monochrome, and the theme-squares subcolor1-info parameter). The :root colour block is value-for-value identical (cand L220-301 against orig L202-283). (c) The theme's own panel rules are byte-identical: blockquote, .yui-navset .yui-content, .code, and .scp-image-block .scp-image-caption extract to the same rule text on both sides. (d) The candidate's remaining CSS deltas are the delivery head (BHL imports and font loads, B53), the five font stacks (B55), and asset URL hosts (section 3); no colour declaration differs. The base swap itself: the original loads black-highlighter.min.css from nu-scptheme.github.io, the candidate from scp-jp.github.io, the JP distribution of the same BHL stylesheet (both distributions fetched once for this package; their .scp-image-block rule sets agree).
- Second-reviewer walk: the ground is checkable from this package alone, with the greps and censuses of section 12; a reader who did none of the work can confirm that the theme contributes no colour change and that the pairing's ingredients (the theme's pale-gray variables and BHL's text composition) are the original's own. A port-side correction would have to override the base's text/background composition or rebind the theme's palette variables, diverging the candidate from the original to fix the original author's own composition, which is the opposite of the port's contract; KB-28's fix recipe (correct the variable binding in the candidate) presupposes a port-introduced binding, and the censuses show there is none. The disposition holds.

### Defect flags (candidate not edited by this lane)

- F1 — two inline rules from the original's head module are absent from the candidate's whole delivery chain. The original's head module-css (orig L2-14) carries, after its two BHL @imports: .scp-image-block.block-right { margin: 1em 0 1em 2em; } (orig L5-7) and .scp-image-block img { min-width: 100%; border: 0.5rem solid rgba(var(--pale-gray-monochrome)); box-sizing: border-box; } (orig L9-13). The candidate's head module (cand L3-5) carries only the own-/1 import, and grep of the candidate for "min-width: 100%", "1em 0 1em 2em", and "box-sizing: border-box" returns nothing: the rules are not in the candidate file. Subsumption check against the base the candidate actually loads (https://scp-jp.github.io/Black-Highlighter/css/min/black-highlighter.min.css, fetched 2026-11-17): its corresponding rules are .scp-image-block.block-right { float: right; clear: right; margin: 0 0 1em 2em } and img.image { border: 0; width: 100% } — different values (margin-top 0 against the theme's 1em; no min-width, no 0.5rem border, no box-sizing on the image), and the EN distribution carries the same base rules, so the dropped pair was the theme's own override layer on both sides of the port. The markup the rules govern survives (the logo image block at cand L65-70 uses block-right), and the code block's own later img rule (.scp-image-block img { border: 0.5rem solid rgba(var(--black-monochrome)) }, cand L587) survives, so the visible delta is the block-right top margin and the image's min-width / box-sizing (the border declaration was already overridden by the code-block rule in the original's cascade). The classifier cannot see this loss: the two head modules pair by kind in B2/B4, and the rules rode inside a module whose other contents (the BHL imports) did move. Precedent shape: betwixt-jp's flag F1 (head-module rules absent from the whole delivery chain).

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:old-money-theme-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP9, landing `b4109ab` (report `R/review-scout/FIX-RDISP9.md`).** One candidate repair (+9 lines), postdating this package's build at `b5cb724`.
- **F1 — head-module inline rules restored verbatim.** The original's head module (original L2–14) carries two inline rules after its BHL @imports: `.scp-image-block.block-right { margin: 1em 0 1em 2em; }` and `.scp-image-block img { min-width: 100%; border: 0.5rem solid rgba(var(--pale-gray-monochrome)); box-sizing: border-box; }`. The whole delivery chain carried none of the three signature declarations, and the JP BHL base has different values, so the pair is the theme's own override layer, not base content. The two rules now stand in the candidate's head module immediately after its own-/1 @import (L5–13), byte-identical to original L5–13 including the blank line (cmp-verified); nothing else changed. The betwixt F1 restore is the precedent shape.
Checker per the report: plain error 10 / warn 0 / info 1 unchanged (all class (iii) pseudo-refs, class (i) 0); links error 10 / warn 1 / info 1 unchanged (the pre-existing BHL link-label warn, line-shifted only).

## Appendix — residue blocks

The 20 heuristic blocks are translation mass in the shapes below, plus the font and delivery seams; the 3 residue blocks are single-line seams of the same mass. Each is assigned here.

- B16 (residue; orig L67 → cand L72): + Usage → + 使用方法， the usage heading. Assigned to section 6.
- B18 (residue; orig L73 → cand L83): the BHL note's heading line, whose translation lands as the + 使用例 heading after the note text moved with B17; the pair B17+B18 is the note cluster. Assigned to section 6.
- B64 (residue; orig L730 → cand L748): the blank line after the code block's closing brace, deleted at the block's tail seam. Assigned to section 9 (formatting).
- B15 (orig L63 → cand L68): the logo caption, Old Money Logo → Old Moneyロゴ. Assigned to section 6.
- B17 (orig L69-70 → cand L74-80): the BHL note and logo div, translated and re-wrapped. Assigned to section 6.
- B19 (orig L75-84 → cand L85): the horizontal-rule explanation paragraph, translated; the install cluster's lines pair inside B17's range. Assigned to section 6.
- B20 (orig L88 → cand L89): the titles explanation line, translated. Assigned to section 6.
- B29 (orig L114 → cand L115): the tab specimen's closing line (How quaint. → なかなか趣がありますね。). Assigned to section 6.
- B31-B41 (orig L119-139 → cand L120-140): the long-tab exhibit's repeated text line, eleven instances of one shape. Assigned to section 6.
- B48-B51 (orig L155-170 → cand L156-171): the blockquote exhibit, the table exhibit, and the font specimen lines. Assigned to section 6.
- B52 (orig L172-173 → cand L173-180): the source-code section seam: the @@ @@ separator, the translator's note (section 10), the + ソースコード heading, the footnoteblock's relocation (section 8), and the collapsible opening. Assigned to sections 6, 8, and 10.
- B53's TRANS-UNANCHORED label: the code-block head region, whose substance is sections 3, 4, and 10. B55's CSS-BODY label: the font stacks, section 4. B65's TRANS-UNANCHORED label: the license-box block, section 1. B5's TRANS-UNANCHORED label: the head-zone block, sections 1-2.

## License and attribution

- **Title:** Old Money Theme
- **Author:** Woedenaz
- **Source:** https://scp-wiki.wikidot.com/theme:old-money-theme — revision 89
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
