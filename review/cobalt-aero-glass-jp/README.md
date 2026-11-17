# theme:cobalt-aero-glass-jp — review package

A Chinese glass theme by Mercuresphere, built on theme:aero-glass (itself a Basalt modification), made for the Wanderers' Library canon Paradigm Shift. The candidate keeps the original's two-channel delivery (a head preset module plus one code block), repoints the base include to the SCP-JP production aero-glass page, replaces the CN credit block with the preview credit block carrying all eight ruling-3 fields, and translates the body and the CSS's visible strings. The theme carried one blocking item, ledger item 47 [F] (sidebar unreachable at ≤375px in both engines), re-judged DISPOSITIONED by FIX5-FUNC §3 on the ground that the sidebar mechanism is inherited unchanged from the base; the disposition is re-derived from this package's bytes in the per-theme record below and confirmed exactly, including the byte-identical #side-bar windows. Two flags stand: a .logo rule the candidate drops without a record (section 8), and the body stack's JP faces named but loaded nowhere in the file or its base page (section 4, minor). The sources.tsv note for this row misstates the upstream state; a correction is recorded in section 0 for the coordinator's harvest.

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:cobalt-aero-glass-jp — origin CN, population #175 [GOSIGN2-LEDGER (b) row 175]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4d223fb0e2e8e48ebf7427a72aada5475f3ef0de6d2c86f25e7792ddeedab9c0); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 10 errors / 1 warn / 1 info (pseudo-ref×10); standing classes dispositioned in register c1 [T1-ROWS row 200; GOSIGN2-LEDGER (b) row 175]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-* cluster confined to chromium-768, whose only hotlink host is http.cat = transient 503 capture, not a result; page sidebar-unreachable at ≤375 (both engines); sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 174, source LOCALIZE-S2-D]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 174]
- FIX5 re-judgement: item 47 (class F) DISPOSITIONED — FIX5-FUNC §3 (no edit): sidebar mechanism inherited from base theme:aero-glass exactly as the original inherits it; candidate #side-bar rules byte-identical to original (diff IDENTICAL); no candidate-side cause [GOSIGN2-LEDGER-SUPPLEMENT (a) item 47]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:cobalt-aero-glass-jp.txt sha256:4d223fb0e2e8e48ebf7427a72aada5475f3ef0de6d2c86f25e7792ddeedab9c0; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

- Package: review/cobalt-aero-glass-jp. Candidate: theme:cobalt-aero-glass-jp. Original: theme:cobalt-aero-glass on scp-wiki-cn (CN), reference revision 56 (also the first-translation reference).
- original.txt: byte copy of the S2 lane cache named in the sources.tsv row's source column (gosign2-lanes/lane-oc-gs-localize-s2-D/orig-cobalt-aero-glass.txt, fetched 2026-11-16), SHA-256 b125e1a132cdc5aa4f66161317b53ee97fbe99ca55ae7c17a20a2f614f78bff4, 29,477 bytes, 1,139 lines plus a final unterminated line (diff.md counts 1,140). The hash equals the sources.tsv row's mirror_sha256.
- candidate.txt: byte copy of pages/theme:cobalt-aero-glass-jp.txt, SHA-256 4d223fb0e2e8e48ebf7427a72aada5475f3ef0de6d2c86f25e7792ddeedab9c0, 31,288 bytes, 1,142 lines.
- The verdict stamp above reads STALE, and the reason is one line long: `git diff 435a6bb..HEAD` for this file is a single hunk, the usage-example self-include at candidate L105 gaining its -jp posting name in the population sweep (commit b5cb724; SWEEP-USAGE.md). The only earlier touches are the CN3 integration (6a8eb9d) and FIX-CREDIT-D (1869877), both verdict-era. The stamp therefore does not carry the PASS onto the changed bytes; the disposition's evidence sits at candidate L583–614, untouched by the sweep line, and was re-measured against the current bytes for this package (per-theme record).
- sources.tsv note correction (recorded here for the coordinator's harvest; sources.tsv is not edited in this package): the note claims the original was "superseded upstream since the reference revision", citing follow-up diff artifact diff-cobalt-aero-glass-from56.txt. The cited artifact (campaign record, gosign2-lanes/lane-oc-gs-localize-s2-D/diff-cobalt-aero-glass-from56.txt, read in full) records rev56 → rev56, no changes, with an empty revision table. The correct standard form is: "Upstream latest remains rev 56; the S2 artifact records rev56 to rev56, no changes; follow-up diff artifact diff-cobalt-aero-glass-from56.txt in the campaign record (K5a-i)". The ambrose-chapter-two-jp package records the same note shape and its correction.
- Kind: standard.

## Class summary

91 classifier blocks: 65 specific, 25 heuristic, 1 residue (appendix). Tier 2 diff: +112 / −110 lines (222 changed) in 31 sections, 0 of the added lines are review-stage comments. Label counts: TRANS-UNANCHORED 48, DELIVERY-MOVE 37, TRANSLATION-ANCHORED 26, COMMENT-TEXT 20, DRAFT-HOST 11, INCLUDE-REPOINT 4, CONTENT-STRING 3, IFTAGS 2, EXHIBIT-RESTRUCTURE 2, and single instances of SELF-DELIVERY, BARE-RATE-DEL, CREDIT-PREVIEW, CREDIT-PROSE, TASL-FIELDS, COMPONENT-SWAP, JPFONT-STACK, GLYPH-FORM. The 37 DELIVERY-MOVE labels are a classifier cross-match artifact, adjudicated in section 3: the :root preset stands in both channels (head module and code block) on both sides, so the topology matcher cross-paired same-content regions (similarity 0.741); every sampled DELIVERY-MOVE block is an ordinary in-place, same-channel change, and the code-block selector census (section 8) proves no module was dropped behind the label (one rule, .logo, was; it is flagged on its own evidence in section 8).

## 1. Credit and attribution

- What: the candidate's credit block (candidate L48–58) is the preview pair carrying the eight ruling-3 fields: タイトル Cobalt Aero Glassテーマ (L49); 翻訳責任者 AI (L50); 翻訳年 2026 (L51); 原題 「钴玻璃 主题版式」 (L52); 著作権者 [[*user Mercuresphere]] (L53); 作成年 2022 (L54); 初訳時参照リビジョン 56 (L55); 元記事リンク (L56); plus a background-image credit (L57: pixabay id-1572988, Pixabay License). The 著作権者 field matches the original's credit 作者 (original L50, [[*user Mercuresphere]]) and the code banner "By Mercuresphere" (original L237 / candidate L242); the banner's second attribution line, the Basalt base-work credit ("Based on Basalt Theme by Liryn & Placeholder McD"), is byte-identical on both sides (original L238 / candidate L243), and the original's own background-image credit line is carried into the L57 field. The original's bare [[module Rate]] inside [[>]] (original L43–45) is removed (BARE-RATE-DEL, block B7) and its CN credit:start/end pair is replaced by the preview pair. The source link's host is scp-wiki-cn.wikidot.com, the host sources.tsv records for the original. Neither file carries an info:start block or a license box.
- Why: ruling 3 (the TASL record: a campaign translation is credited to the campaign with the original's author preserved) and KB-63 (attribution lines beyond the author field, here the background-image credit and the banner's base-work line, survive).
- Verify: read candidate L46–58 against original L41–53, and both code banners (original L237–238, candidate L242–243).
- Disposition: T4 PASS and T5 PASS (the stamp above; LOCALIZE-ROWS row 174, source LOCALIZE-S2-D, lane record part-CN3.md).

## 2. Includes and components

- What: the candidate carries 7 includes against the original's 6. The base is repointed (:scp-wiki-cn:theme:aero-glass → :scp-jp:theme:aero-glass; block B1, L1 on both sides; section 3). The credit pair is swapped (section 1). The theme-squares include is repointed :scp-wiki: → :scp-jp: (block B10; original L59 → candidate L64). The usage-example self-include names the -jp posting form (candidate L105; the sweep line of section 0). The image-block include stays prefix-less (component:image-block) exactly as the original carries it (block B17; original L102 → candidate L107), with its image re-hosted (section 4). The candidate adds the interwiki-style frame (candidate L41–44, section 3). No include is duplicated on either side.
- Why: patterns P3/P6: includes name the JP environment's pages; an include form inherited byte-identical from the original (the prefix-less image-block) is the original's own form, not drift.
- Verify: `grep -n '\[\[include' ` on both files.
- Disposition: T4 PASS.

## 3. Delivery and code loading

- What: both sides deliver in two channels: a head [[module CSS]] preset (37 lines, L3–39 on both sides) and one [[code type="CSS"]] block (original L234–1138, 905 lines; candidate L239–1140, 902 lines). The candidate adds an interwiki-style frame at priority=1 (candidate L41–44) whose theme= parameter names the draft host's local--code/theme%3Acobalt-aero-glass-jp/1. Census, counting every code form: exactly one code block per side, so the address /1 names the candidate's 902-line stylesheet, the block that holds the CSS (the self-delivery census records this theme's address as matching; no remedy applies). The base include names theme:aero-glass in production form: no theme:aero-glass-jp candidate exists (a pages/ census finds only this theme, frutiger-aero-jp, and decoration samples naming aero-glass), and the production page stands at pages-existing/existing:theme-aero-glass.txt, so the include resolves to the production base exactly as the original resolves to the CN base. Brace-depth scan: both files end at depth 0 and never go negative.
- What, the DELIVERY-MOVE labels: the :root preset stands in the head module and again in the code block on BOTH sides, so the classifier's topology matcher cross-paired the two copies (similarity 0.741) and labeled in-place changes as moves. Sampled blocks (B2, B3, B4 in the head module; B58–B66 in the code block) are asset re-hosts, the title localization, the font stack, and comment translations, all in the same channel and position on both sides. Components sit in the same positions and channels on both sides; no module moved and none was dropped behind the label (the one dropped rule is section 8's, on census evidence).
- Why: patterns P4/P6 and KB-07 (a single priority-1 frame for a single code layer over a production base), and the T9 self-delivery census rule (the named block must be the stylesheet).
- Verify: the greps in section 12; `grep -c 'code type' ` on both files.
- Disposition: T4 PASS; the localize lane (part-CN3.md) judged the delivery patterns APPLIED on the base-delegation design.

## 4. Fonts and assets

- What, fonts: neither file carries an @import or an @font-face. The head preset's code stack names 'Fira Code' on both sides (candidate L34 = original L35), a face the base chain carries (the production base page source names Fira Code). One font item is flagged, minor: the code block's body rule gains 'Noto Sans JP', 'Noto Sans CJK JP' ahead of sans-serif (candidate L279; block B61, JPFONT-STACK), but no @import or @font-face in the candidate, and none in the production base page source, loads either face, so as far as the in-repo chain shows the supplement is inert and rendering falls through to sans-serif, the original's own form. The sibling aero-glass port (frutiger-aero-jp) loads the JP faces its stacks name; this candidate does not. Flagged for coordinator adjudication (add the load, or record the family form); the package is written against the candidate as it stands.
- What, assets: the head preset's --logo and --background-image move from the author's personal host (evernight-aquarium.wdfiles.com) to the candidate's own draft-host local--files (candidate L20, L22; blocks B2, B3, DRAFT-HOST); the code block's --logo moves from a fastly.jsdelivr.net/gh/Crimone URL to scp-jp.wdfiles.com (block B58; original L254 → candidate L259), with further draft-host asset lines at blocks B59, B68, B69, B87, B89, B91. These are T1 class (iii) draft forms, re-hosted at posting.
- Why: pattern P5 (asset delivery inside the JP environment) and pattern P7 (a stack must not name a face nothing loads, the named-but-unloaded shape).
- Verify: `grep -n '@import\|@font-face\|Fira Code\|Noto Sans' ` on candidate.txt and on pages-existing/existing:theme-aero-glass.txt.
- Disposition: T4 PASS stands for the delivery patterns; the font-load item is this package's flag, not a ledger item.

## 5. Header, sidebar, site furniture

- What: the head preset localizes --title and --subtitle: the original's " PARADIGM SHIFT" and " 范式转移" both become " パラダイムシフト" (block B4; candidate L26–27), the Japanese form of the canon's name, which is the form the candidate's own prose uses throughout; a name functioning as a mark, recorded, not charged. The #side-bar rules are the disposition's evidence and are enumerated in the per-theme record: 9 lines per side, all identical modulo line shift. Neither file defines an .open-menu rule (the toggle arrives from the base and site layer on both sides). The .logo deletion is section 8's flag.
- Why: the ruling-2 boundary as refined (names and marks stay identity strings in either direction; the file's own usage governs the form), and section 11's disposition for the sidebar mechanism itself.
- Verify: candidate L20–38 against original L20–38; the census in the per-theme record.
- Disposition: ledger item 47 [F] DISPOSITIONED (section 11); T4/T5 PASS.

## 6. Text translation

- What: the documentation body is translated in full (26 TRANSLATION-ANCHORED blocks; the TRANS-UNANCHORED mass is prose lines and CSS comments translated without anchors, resolved by shape here). The CSS comments are translated with the body (20 COMMENT-TEXT blocks; e.g. block B79, /* table */ → /* 表 */, and block B80, 颜色调整 → 色調整， carrying the GLYPH-FORM simplified-to-shinjitai conversion). The CSS's visible strings are translated (3 CONTENT-STRING blocks: the page-lock notice at candidate L936, L951, L957). The specimen footnote inside the nested-blockquote exhibit stands on both sides (original L217 / candidate L222) with no footnoteblock on either side: parity, not a drop.
- Why: T5 translation text, and KB-18 (visible strings in CSS content: translate with the body).
- Verify: the block list in classification.json against the diff.
- Disposition: T5 PASS.

## 7. Links

- What: the credit source link names scp-wiki-cn.wikidot.com, the original's recorded host (candidate L56). One relative link stands as the localize lane left it: [[[wanderers:paradigm-shift-hub|パラダイムシフト]]] (candidate L97); whether a JP hub page exists under that name is unverified in the record, T4 passed the row, and a relative link is not charged as dead on this evidence, so it is recorded as a standing observation at the localize lane's weight. No other plain-form reference names a page that will not exist: the usage example names the -jp form (candidate L105).
- Why: the credit-link host rule, and the probe-before-flag rule for plain-form prose links.
- Verify: `grep -n 'http\|\[\[\[' ` on candidate.txt.
- Disposition: none charged.

## 8. Structure

- What (flag): the original's code block carries `.logo { transform-origin: 50% 33.333%; }` (original L389–391). The candidate has no .logo rule anywhere (`grep -n '^\.logo\|\.logo {' ` on candidate.txt: zero lines). A selector census of the two code blocks (top-level selectors, compared as sets) gives candidate 110 against original 111, and .logo is the only difference. The drop is not subsumption by the base: the production base's .logo rule is a different declaration (`.logo { top: 6px; }`, pages-existing/existing:theme-aero-glass.txt L329–331), transform-origin appears nowhere else in the candidate or the JP base page, and no transform applies to .logo anywhere in the JP chain as this repo shows, so the declaration is inert in the JP rendering on the available evidence. But no record dispositions the drop (the CN3 localize record is silent on it; the ledger's T4/T5 are PASS), so it stands as an undocumented deletion, flagged for coordinator adjudication (restore the rule, or record the drop with its ground). The classifier's block B64 carries this deletion under a DELIVERY-MOVE label.
- What, other structure: the collapsible and exhibit structure is otherwise carried; the body region's includes and specimens stand in the same positions and channels on both sides (sections 2 and 6).
- Why: the content-presence rule (a dropped CSS rule is a flag with line ranges on both sides; a base default is not the theme's override).
- Verify: the selector census in section 12; read original L389–391.
- Disposition: flagged; the candidate is packaged as it stands.

## 9. Formatting only

- What: the package's single residue block (B5, appendix) is one added blank line before the head module's close. Beyond it, this pair's diff is content-bearing almost throughout; there is no whitespace-only mass of the WS-ONLY kind.
- Why: formatting class.
- Verify: candidate L36–39 against original L36–39.
- Disposition: no verdict attaches.

## 10. Porter annotations

- What: none. Every comment block in the candidate pairs with a comment in the original (the 20 COMMENT-TEXT blocks are translations of the original's own comments); no porter comment stands in the file, and no annotation makes a claim the bytes could refute.
- Why: annotations are evidence about intent; a false one is a flag. None here.
- Verify: `grep -n '/\*' ` on both files and compare.
- Disposition: none.

## 11. Dispositions and exceptions

- Ledger item 47 [F], the theme's only blocking item: DISPOSITIONED by FIX5-FUNC §3 (no edit). Re-derived from the package bytes in the per-theme record below; confirmed exactly on every leg.
- The render row's other lines are dispositioned in ledger register (c2): the page hidden-* cluster is a transient Wikidot 503 capture (KB-44; its only hotlink host is http.cat), and the sample T2 run returning no machine verdict (exit 2, no summary) is a coverage caveat, not a theme defect (ledger (a) caveat 2).
- T1: the baseline is 10 errors / 1 warn / 1 info, all 10 errors pseudo-ref class, dispositioned in register (c1) as class (iii) draft-host forms; FIX5-FUNC's checker re-run reported the identical 10 / 1 / 1 before and after (no edit was made).
- T4/T5: PASS (LOCALIZE-ROWS row 174; lane record part-CN3.md).
- The STALE stamp is explained in section 0: the verdict's substance is re-derivable against the current bytes because the only post-verdict change is the sweep line at candidate L105.

## 12. Verification

- What a reader can re-run from this repo alone: `python3 review/build_review.py --check` (diff.md and the stamp above are current); `sha256sum` on original.txt and candidate.txt against section 0; `git diff 435a6bb..HEAD -- pages/theme:cobalt-aero-glass-jp.txt` for the STALE line; the #side-bar census and window hash in the per-theme record; the code-block selector census (top-level selectors compared as sets); the brace-depth scan, which ends at depth 0 on both files and never goes negative.
- Why: the package's claims are only worth what a reader can re-derive; every load-bearing claim above names its check.
- Disposition: verification route stands; the T1 baseline counts are the stamp's, and FIX5-FUNC's checker record agrees with them.

## Per-theme record: ledger item 47 [F] re-derived

The charge (GOSIGN2-LEDGER (e) item 47): the candidate page's sidebar is unreachable at ≤375px in both engines (a machine finding on every mobile combo); no T3 clearance was recorded and no fix wave addressed it. The supplement's re-judgement (GOSIGN2-LEDGER-SUPPLEMENT item 47): DISPOSITIONED, FIX5-FUNC §3, on the ground that the sidebar mechanism is inherited from base theme:aero-glass exactly as the original inherits it, that the candidate's #side-bar rules are byte-identical to the original's, and that there is no candidate-side cause.

Re-derivation from the bytes, measured for this package:

1. The FIX5 window: candidate L583–614 against original L581–612, 1,035 bytes, byte-identical (SHA-256 fade512beda1be56e936ec81bb08be47d54ab1d6c142aae460fb22821d0fd6be on both sides). The window carries the main #side-bar cluster.
2. The complete #side-bar census: 9 lines per side, every line identical modulo line shift. Head preset: candidate L34 = original L35 (the preset font rule). Code block: candidate L347/L351 = original L342/L346 (the #extra-div-1::before / #extra-div-2::before / #side-bar::before font rule and the #side-bar::before word-spacing rule). Main cluster: candidate L583/588/594/599/606/612 inside the verified window of leg 1.
3. .open-menu: zero lines in BOTH files. Neither side defines its own sidebar toggle; it arrives from the base and site layer on both sides.
4. Base inheritance: candidate L1 includes :scp-jp:theme:aero-glass; original L1 includes :scp-wiki-cn:theme:aero-glass. The mechanism the machine finding charges is the base's, inherited in the same form by both files; no theme:aero-glass-jp exists for the candidate to have diverged through (section 3).
5. Checker: FIX5-FUNC reported 10 errors / 1 warn / 1 info before and after, unchanged (no edit); the stamp's T1 baseline agrees.

Second-reviewer walk. Is the ground stated in terms a reader who did none of the work can check? Yes: legs 1–3 verify from this package's own two files; leg 4 needs the pages/ census for the absence of a JP base candidate and pages-existing/existing:theme-aero-glass.txt for the base itself, both in this repo. The walk confirms the ground exactly as stated: the candidate-side file contributes no sidebar mechanism of its own beyond byte-identical inherited rules, so a candidate edit was not the right outcome. The walk also surfaces what the disposition does not cover: the .logo deletion (section 8) sits outside the sidebar mechanism and outside this disposition's claim, and is flagged separately rather than folded into this judgement. Walk outcome: the disposition stands.

## Appendix — residue blocks

- B5 (insertion at candidate L38): one added blank line in the candidate before the head module's [[/module]] (candidate L37–38 both blank against original L38; [[/module]] at L39 on both sides). No signature fired; whitespace-only, adjudicated as formatting. No action.
