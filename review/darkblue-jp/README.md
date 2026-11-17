# Review package — theme:darkblue-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:darkblue-jp — origin CN, population #179 [GOSIGN2-LEDGER (b) row 179]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 1a7a096c0904bccca2bd742e556640620f1a3f53f5771743f02d5668022578e4); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 2 infos (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 214; GOSIGN2-LEDGER (b) row 179]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page T2 no machine verdict (exit 2, no summary); sample page-overflow 387–389px@320/375 + sidebar-unreachable at ≤375 (both engines) + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 178, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 178]
- FIX5 re-judgement: items 50 (class B) FIXED, 51 (class D) FIXED, 52 (class F) DISPOSITIONED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed; darkblue class-D item fixed (per lane commit) FIX5-FURNB (no edit): theme-owned off-canvas toggle (#side-bar:is(:hover,:focus-within) plus tab pseudo-elements) byte-identical to the original over the toggle regions (diff empty); the machine check only looks for .open-menu a; T3 recorded no visual finding [GOSIGN2-LEDGER-SUPPLEMENT (a) items 50–52]
- Computed against: canonical commit 050817e10987f9070493e17f10ff30b587631985; candidate file pages/theme:darkblue-jp.txt sha256:1a7a096c0904bccca2bd742e556640620f1a3f53f5771743f02d5668022578e4; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


Status: complete — hand-written explanation below; the generated verdict stamp above reads STALE because the candidate changed after the verdict's bytes (the FIX5 wave's own edits and the usage-example sweep), so the per-theme record re-derives all three of the theme's FIX5 items from the packaged bytes
Candidate: review/darkblue-jp/candidate.txt (sha256 0e1659f1f61abc9ad4a108a0e11a6515e603a8f0fbde8b1ab851d0989f78bbe3)
Original: theme:darkblue — scp-wiki-cn, revision 3 (sha256 0c7fb425fd4637a83d446bb367c603c6bf6c441f6828b55b185ae4e1fc904374)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Provenance

- Original (theme:darkblue): https://scp-wiki-cn.wikidot.com/theme:darkblue — origin CN, reference revision 3 (revision id not exposed by wikidot.py; the mirror class is the provenance).
- Candidate (theme:darkblue-jp): pages/theme:darkblue-jp.txt — no production JP counterpart; the port is the campaign's own.
- Kind: standard (no SPECIAL-ROWS shape). The theme is a full Sigma-10 site theme: one head delivery module, one large code block (about 4,970 lines of CSS), one tail module.
- Mirror: review-mirrors/store/darkblue__scp-wiki-cn__r3.txt, class COPY (byte-true copy of the S2 cache artifact), SHA-256 verified equal to the sources.tsv row at package build.
- Provenance route: derived from the original at the reference revision. The follow-up diff artifact (diff-darkblue-from3.txt) records upstream rev 3 to rev 3, no changes; the mirror is the current upstream text as well as the reference text. The sources.tsv note for this row claims the original was superseded upstream; that claim is wrong (the artifact it cites records no changes), and the correction is recorded in the per-theme record for the coordinator's harvest fix.

## Summary

A large CN Sigma-10 theme (5,185 lines) carried over with its delivery topology intact: same head module, same single code block, same tail module, self-delivery address /1 correct on both sides. The port repoints delivery to the JP hosts and the draft host, swaps the credit block for the JP preview form with a full TASL set, localizes the tag gate, translates the documentation body and the visible CSS strings, re-hosts the original's personal-host assets onto the candidate's own draft host, and JP-ifies the header text variables. Two campaign waves then edited the file: FIX5 removed the duplicated bare Rate (item 50) and added the Noto Sans JP load with its four stack fallbacks (item 51), and the usage-example sweep aligned the file's self-name specimens to the -jp posting form. The theme's third FIX5 item (52) is a disposition: the sidebar toggle rules the render check charged are byte-identical to the original's, re-derived here region by region with hashes. The byte pass found one silent drop no record names (the scpnet-interwiki frame rules, defect D1) and one wrong provenance note (the sources.tsv supersession claim); both are recorded in the per-theme record, and the candidate is packaged as it stands.

## 0. Header / provenance

- Delivery: no relocation between the sides; each side's components match by kind (head module-css, one code-css block, tail module-css), and the classifier's topology pass confirms no moves. Unlike the small themes, this one's structure is the original's own, kept.
- Scale note for the reader: of 5,185 original lines, the diff touches 196 (generator count +90/-106 over 17 hunks). The CSS body is the original's, with the edits concentrated in the head furniture, the font layer, and the specific loci the sections below name.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 5 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 5 |
| EXHIBIT-RESTRUCTURE | 3 |
| GLYPH-FORM | 5 |
| HEADERVAR | 3 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 4 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 15 |
| TRANSLATION-ANCHORED | 17 |
| WS-ONLY | 4 |

Counts: 49 blocks, 31 specific, 15 heuristic, 3 residue, 0 skipped (comment text).

## 1. Credit and attribution

- B7 (orig L20-23 -> cand L18-27, CREDIT-PREVIEW + TASL-FIELDS + CREDIT-PROSE, with a BARE-RATE-DEL span). What: the original's credit pair (`:scp-wiki-cn:credit:start` / `credit:end`, orig L20 and L25) is replaced by the JP `credit:start-preview` / `credit:end-preview` pair, the credit body becomes the eight-field TASL set (cand L19-26), and the original's own bare `[[module Rate]]` (orig L22, inside a centering block at orig L21-23) is deleted.
  Why: the swap is pattern 3 (P3/T1) — the branch credit module does not render in the JP environment; the preview form is the rate-bearing JP form (KB-32). The field set is the campaign's TASL record (owner ruling 3 of 2026-11-16). The Rate deletion is the FIX5 closure of item 50: the preview credit block already carries the rating module, so the original's second, bare Rate was a duplicate (the ledger's class B shape; FIX5-FURNB, commit 25bb0b4, removed exactly the three wrapper lines after credit:end-preview).
  Verify: grep the candidate for `[[module Rate]]` — zero occurrences; the original has one, at L22. The FIX5 checker line for this file: 5 errors / 1 warn / 2 infos before, 5 / 1 / 1 after (the double-rate finding is the one that closes).
  Judgment: the author field is right — 著作権者 [[*user Agent FS]] (cand L23) matches the original's own authorship statement ([[user agent-fs]] in its intro prose, orig L28). The source link's host is right: scp-wiki-cn.wikidot.com is the recorded host in sources.tsv. Two field values a reader might question are both correct, with evidence: 作成年 2026 (cand L24) — a fetch for this package (2026-11-17) shows the CN page was created 2026-08-17 (rev 0) and reached rev 3 on 2026-08-18, so 2026 is the creation year, not a porter's slip; and タイトル 藏青 版式 (cand L19) copies the original's title because the candidate's body supplies no Japanese theme name (there is no ダークブルー anywhere in the file) — the recorded no-edit shape (the supply-n-demand F2 ground), not the steam-guide shape, which applies only where the body supplies the form.
  Disposition: ledger (c3) P3 FIXED, re-judged as (e) item 50 FIXED by FIX5-FURNB; re-derived in the per-theme record.

## 2. Includes and components

- B6 (orig L18 -> cand L16, IFTAGS). What: the page gate localizes, `[[iftags +版式]]` -> `[[iftags +テーマ]]`.
  Why: pattern 2 (KB-08) — iftags conditions name JP tags in the JP environment; the original's condition named the CN word for the theme tag itself.
  Verify: KB-08 recipe — the candidate's one gate names +テーマ.
  Disposition: pattern 2 applied by the localize lane; no separate ledger item.
- The two interwiki-style includes (B2, orig L6-10 -> cand L6-9; B4, orig L12-16 -> cand L11-14; INCLUDE-REPOINT spans inside blocks the skeleton files under section 8). What: both includes repoint from `:scp-wiki-cn:component:interwiki-style` to `:scp-jp:component:interwiki-style`, their theme arguments repoint with them (section 3), and the `type=sidebar` argument is dropped from both.
  Why: the repoint is the population's component form; the argument drop is the localize lane's pattern 6, recorded APPLIED — the JP interwiki-style component accepts only priority and theme, so the CN-only argument has no counterpart to carry.
  Verify: read cand L6-14 against orig L6-16; the priority values (0 and 1) are unchanged.
  Judgment: the skeleton's EXHIBIT-RESTRUCTURE label on B2/B4 is a false fire — these are live delivery includes in the head furniture, not exhibits; nothing was dropped except the one recorded argument. Adjudicated against the include census: both includes survive, in place, with their priorities.
- B9's include half (orig L32 -> cand L35-39 region). What: the usage section's theme-squares include repoints from `component:theme-squares` (CN form) to `:scp-jp:component:theme-squares`. The block's growth is the translated intro prose around it (section 6), not an include change.
- The skeleton's COMPONENT-SWAP block (B42) is not an include at all: it is the CSS banner string that tells readers how to include this theme, repointed inside a `content:` string. It is argued with the other visible strings in section 6.

## 3. Delivery and code loading

- B1 (orig L2-3 -> cand L2-3, DELIVERY-HOST + DRAFT-HOST + SELF-DELIVERY). What: the head module's two imports are repointed: the Basalt normalize stylesheet moves from cdn.scpwiki.com (the EN Basalt CDN path) to the candidate's own draft-host local--files copy (basalt-normalize.min.css), and the theme's own code import moves from scp-wiki-cn.wdfiles.com/local--code/theme%3Adarkblue/1 to the draft host's theme%3Adarkblue-jp/1.
  Why: pattern 4 — delivery is served from the JP environment's hosts; the self-import is the population's draft-stage form for a candidate's own code block (class (iii), section 11).
  Verify: the candidate has exactly one code block (cand L175 to its close at L5143, counted over every code-block form), so the /1 address names the stylesheet on both sides; the FIX-CODEADDR audit's classes do not touch this theme. Brace-depth scan of the code block: ends at depth 0, never negative.
- B3 (orig L9 -> cand L8) and B5 (orig L14-15 -> cand L13): the two interwiki includes' theme arguments take the same repoints as B1 (the /1 self-delivery URL for priority 1, the normalize URL for priority 0).
- B13 (orig L94-95 -> cand L101-102, DRAFT-HOST). What: the usage section's image-block exhibit, whose image was the Basalt logo on cdn.scpwiki.com, now names the draft-host local--files copy. Same re-host as B1's first import, applied to the exhibit so the documentation shows the asset the delivery actually uses.
- B34 (orig L194-195 -> cand L192-193, DRAFT-HOST). What: inside the code block, the theme's --logo-image and --body-bg-image URLs move from the author's personal host (wangstorage.oss-cn-hangzhou.aliyuncs.com/fendsfox/...) to the candidate's own draft-host local--files. The original served its two main surfaces from a personal OSS bucket; the port re-hosts them onto the theme's own files, the population's asset form.
  Verify: grep the candidate for `wangstorage` and `fendsfox` — zero; both variables name sigma10-jp-test.wdfiles.com/local--files/theme%3Adarkblue-jp/ paths.
- Dual-channel note: the head module and the two interwiki includes load the same two files (the module by @import, the includes by their theme arguments). That is the original's own delivery shape, kept; the localize lane's rollup records it as a posting-time cleanup note (merge the duplicate load at posting), not a defect.

## 4. Fonts and assets

- B33 (orig L177-185 -> cand L183, JPFONT-LOAD). What: a Noto Sans JP @import is added to the code block's import group (cand L183), after the four Latin imports (Inter, K2D, JetBrains Mono, Jost — all kept from the original, Google Fonts). This is the FIX5 closure of item 51.
  Why: pattern 7 (KB-16) — the original loads no JP typeface; Japanese text in the JP environment needs one loaded, and the resolved base does not supply it for this standalone theme.
  Verify: the import stands inside the live code block (cand L175-5143), i.e. in operative CSS, not in an exhibit; and it is applied — all four font stacks carry 'Noto Sans JP' as their trailing fallback (section 8, B35/B36). No named-but-unloaded and no loaded-but-unapplied gap stands for this family.
  Disposition: ledger (c3) P7, re-judged as (e) item 51 FIXED by FIX5-FURNB ("darkblue D fixed" in its commit subject); re-derived in the per-theme record.
- The same block's removed side carries a deliberate removal the classifier gives no signature: the original's RedactRect @font-face (orig L178-186, src on cdn.scpwiki.com, unicode-range U+2588 only) is gone, and its name is gone from --UI-font-primary (B35). This is not a silent drop: the localize lane's pattern 4 records it as APPLIED with its ground — RedactRect is a joke redaction face covering exactly one glyph (the full block U+2588), and the port removes both the load and the stack reference together. Recorded here so the removal has a name in the package; the lane record is its disposition.
- No other font change: the four Latin families load identically on both sides, and the theme's stacks name nothing else that is unloaded.

## 5. Header, sidebar, site furniture

- B37 (orig L245-246 -> cand L243-244, HEADERVAR). What: the header text defaults are JP-ified at definition: --header-title 'SCP基金会' -> 'SCP財団', --header-subtitle '控制 - 收容 - 保護' -> '確保 - 収容 - 保護' (the SCP-JP motto form).
  Why and judgment: pattern 9 (KB-57) governs this surface. These two values are the site's name and motto as rendered on every page that does not override them; the port translated them, and did so consistently (B39/B40 below). Under the main chat's boundary (names and marks stay as identity strings; prose a reader reads gets translated), a motto is the borderline case; the population's localized candidates translate these defaults, and this file's choice agrees with its own credit and prose localization. Recorded as the theme's standing choice, not charged in either direction.
- B39 (orig L807 -> cand L805) and B40 (orig L816 -> cand L814), HEADERVAR: the two `var()` fallbacks for the same variables, deep in the code block, take the same JP values, so no code path renders the CN strings.
  Verify: grep the candidate for 基金会 and 控制 — zero; the JP forms occur at the definition and at both fallbacks.
- The sidebar surface is item 52's ground: the off-canvas toggle rules are byte-identical to the original's (measured in the per-theme record), which is why no sidebar block fires in the classifier at all. The one sidebar-adjacent loss, the scpnet-interwiki frame rules that sit between the :is(#side-bar, #interwiki) rules, is a dropped CSS block and is argued in section 8 (defect D1).

## 6. Text translation

- The documentation body (orig L28-167 -> cand L35-174) is translated in full: the intro (B8/B9's region), the usage instructions (B10-B16), and the long specimen section (B17-B31). The anchored pairs (TRANSLATION-ANCHORED: B12, B17-B23) are one-to-one translations whose anchors (heading levels, specimen markup, user links) confirm the pairing; the unanchored pairs (B10, B14-B16, B25-B31) are the same translation mass where the script change defeats the anchor test, resolved line by line in the appendix. The specimen content survives translation intact, including its jokes (the divider specimens at cand L106-110 keep their footnote and their targets, [[*user placeholder-mcd]] among them — user links are branch-neutral and correctly untranslated).
  Why: pattern 10 (KB-18) — reader-visible text localizes.
  Verify: read any pair; the appendix resolves each unanchored block by shape.
- B42 (orig L1733 -> cand L1722, skeleton label COMPONENT-SWAP; CONTENT-STRING by mechanism). What: the announcement banner the theme injects into pages that use it — `#page-content:not(:has(a.-override-warning))::before { content: ... }` — has its instruction string translated and its include target repointed: "请使用 [[include :scp-wiki-cn:theme:darkblue]] 引用此版式。" -> "「[[include :scp-jp:theme:darkblue-jp]]」でこの版式を引用してください。"
  Why: the string renders for every reader of every page using the theme, so it is visible text (KB-18's reader-visible half); its include instruction must name the page a JP reader can actually include, which is the candidate itself in its posting form.
  Judgment: this is the sweep-era form of the theme's self-name, consistent with the file's specimens (section 7). The banner itself is the original's design, and the candidate keeps its self-suppression: the hidden `-override-warning` anchor at cand L5174 (the file's last line) is what keeps the banner off the theme's own page, exactly as in the original. The localize lane recorded the banner as a staff-approval standing item; it is carried here as a record, not a defect.
- B43 (orig L1737 -> cand L1726, CONTENT-STRING): the banner's second string (the ACS-component warning) translated the same way.
- B46/B47 (orig L4008/L4013 -> cand L3997/L4002, CONTENT-STRING): the pager strings, English in the original (« previous / next »), translated to « 前へ / 次へ » — visible navigation text.
- B49 (orig L4504 -> cand L4493, CONTENT-STRING + GLYPH-FORM): a string-valued label （無題） carried with its glyph form localized.
- Terminology record: the candidate renders the original's 版式 as 版式 throughout (credit title cand L19, intro L35, usage L92, the banner strings), where SCP-JP's own vocabulary for a theme is テーマ. The localize lane recorded this as its T5 (c) standing terminology item. It is consistent inside the file and it is the original's word carried literally; recorded here as the lane left it, not charged as a defect.
- One lane-era string does not stand in the current bytes: the S2-D report's T5 (b) residue named a CN string （漏洞） at its candidate L288; grep finds that string in neither the current candidate nor the mirror original (the region is CSS variable definitions on both sides). Whatever wave removed it, no residue stands to adjudicate.

## 7. Links

- B24 (orig L126 -> cand L133, LINK-REPOINT). What: the link specimen row's visited-link example names the candidate's own posting form: `[[[theme:darkblue-jp | アクセス済みのリンク]]]` where the original's specimen named theme:darkblue.
  Why and judgment: the specimen teaches what a visited link looks like in a page using this theme; in the JP environment the page a reader visits is the -jp page. The localize lane's own call was the opposite (its T5 (b) residue proposed reverting the specimen to theme:darkblue); the later usage-example sweep (commit b5cb724, in this file's history) settled the population premise the other way — self-name specimens take the posting form — and this line is one of its repairs. The package follows the bytes and the settled premise, and records the lane's contrary call as superseded.
- B11 (orig L88 -> cand L95, residue). What: the usage example's include line takes the same form: `@@[[include :scp-jp:theme:darkblue-jp]]@@` (the original's line escapes its own include the same way, with the CN name). Same ground as B24; the pair is the file's self-name in its two specimen shapes.
- No other prose-link block fires, and the census agrees: the body's remaining links are user links (branch-neutral) and the credit source link (section 1, host verified against sources.tsv); the file carries no other external prose references. No plain-form reference naming a page that will not exist stands in this file.

## 8. Structure

- B35 (orig L235 -> cand L233) and B36 (orig L238-240 -> cand L236-238), CSS-BODY by label, P7 font-stack rewrites by mechanism. What: the four font stacks gain 'Noto Sans JP' as trailing fallback (cand L233, L236, L237, L238), and --UI-font-primary additionally loses the RedactRect name (section 4). These are the application half of item 51; the load half is B33.
  Why: pattern 7 — a load nobody applies is inert; FIX5-FURNB's edit applied the family in all four stacks the theme defines.
  Verify: grep the candidate for `'Noto Sans JP'` — the import (L183) plus the four stack lines; the original has zero JP font lines anywhere.
- B41 (orig L1664-1672 -> cand at L1662, CSS-BODY). What: two rules are deleted with no counterpart:

  ```
  div.scpnet-interwiki-wrapper { margin: 0; min-height: 0; }
  iframe.scpnet-interwiki-frame { height: 0; }
  ```

  Why this is a flag and not churn: the rules are the theme's sizing for the scpnet interwiki frame, sitting between the :is(#side-bar, #interwiki) rules in the original's furniture region. Grep finds no `scpnet`, `interwiki-frame`, or `interwiki-wrapper` anywhere in the candidate. The deletion is already present in the CN4 integrate commit (cad7c86), so it happened in the initial port; no campaign record names it — the localize lane's pattern 8 line claims no sidebar-related hunk, and item 52's byte-identity (per-theme record) covers the toggle regions only, which these rules are not part of. Defect D1 in the per-theme record.
- Exhibit decisions (the skeleton's EXHIBIT-RESTRUCTURE blocks): B2 and B4 are the head interwiki includes, adjudicated in section 2 (repointed, one recorded argument dropped, nothing else). B9 is the theme-squares include plus the translated intro around it (sections 2 and 6). No exhibit was dropped or replaced in this theme; the one deletion with an exhibit shape is the bare Rate inside B7, which is item 50's sanctioned fix (section 1), not an exhibit decision.

## 9. Formatting only

- WS-ONLY blocks: 4 (B38, B44, B45, B48 — whitespace-only lines inside the code block, carried or adjusted without content change).
- B32 (orig L167 -> cand at L174, residue): a blank line's difference immediately before the code block — formatting only, no content on either side.
- Re-indentation pairs: 0.

## 10. Porter annotations

none — checked explicitly over the whole candidate, per the standing rule that annotations hide inside other labeled blocks: the file carries no porter comment, no 訳注 block, and no `[!--` annotation anywhere. Its comments are the original's own CSS comments, translated where they changed as part of the blocks above. The ground is the grep census (zero matches for the annotation forms), not the absence of a signature.

## 11. Dispositions and exceptions

- Item 52 (class F) DISPOSITIONED — the theme's sidebar item; re-derived and argued in full in the per-theme record. Ground in one line: the theme-owned off-canvas toggle rules are byte-identical to the original's over the toggle regions, and the machine check that charged them looks for a selector this theme's design hides unconditionally in both versions.
- The (c2) composite's other two members are dispositioned cross-cutting classes, not theme items: the sample page-overflow at 320/375 belongs to the KB-33/KB-34 responsive classes, and the runtime-hotlink member is the site-theme chain, class (ii). Both were dispositioned at the register level for the whole population; nothing in this package's bytes distinguishes this theme's instance.
- The (c2) T2 coverage caveat: the theme page's T2 run produced no machine verdict (exit 2, no summary). The disposition is a coverage statement, restated here so it is checkable: this theme's go-sign evidence is T1 (baseline below), the T3 walk (which produced item 52's finding and its disposition), and T4/T5. No T2 machine PASS is claimed anywhere in the record, and this package does not create one.
- HTTP-KEPT stub (48 occurrences): the derived-presence stub fires on `http` strings inside the candidate's CSS. Its own example is the tell — the occurrences are W3C namespace strings inside SVG data URIs (a grep census finds only two http forms in the file: http://www.w3.org/2000/svg and http://www.w3.org/1999/xlink). Those are not links and cannot be repointed; the signature's known false-fire class (recorded in the patterns proposals of earlier batches). Any genuine kept http reference would be class (ii), a posting rewrite; the census here finds none — the file's real URLs are the delivery and asset addresses argued in section 3, all https.
- T1 standing classes (register c1): the baseline's 5 errors are all pseudo-refs, the draft-host local--code imports' checker shape — the sanctioned draft-stage form, class (iii) in substance. No class (i) error stands.

## 12. Verification

- T1 (source check): baseline 2026-11-16, exit 1, 5 errors / 1 warn / 2 infos (pseudo-ref x5) [T1-ROWS row 214]. After the FIX5-FURNB edit: 5 / 1 / 1 (the double-rate info closes with item 50).
- T2/T3 (render): FINDINGS — the page T2 run gave no machine verdict (the coverage caveat of section 11); the sample carried the overflow and sidebar findings that became the (c2) composite, whose sidebar member is item 52 [RENDER-ROWS-2, RENDER-S2-E (CN4)].
- T4 (localize patterns): FINDINGS, display-affecting findings 4 [LOCALIZE-ROWS row 178, source LOCALIZE-S2-D]; verdicts in the ledger (c3) row (P3 and P7, re-judged as items 50 and 51) and the lane applications recorded in the sections above.
- T4 follow-up diff: the S2 artifact records upstream rev 3 to rev 3, no changes; the mirror is current. (The sources.tsv note claiming supersession contradicts its own artifact; see the per-theme record.)
- T5 (translation text): judged jointly with T4 by the source lane; its standing items in the current bytes are the 版式 terminology record (section 6) and the closed 漏洞 residue (section 6).
- Package checks, run at build: candidate.txt byte-identical to pages/theme:darkblue-jp.txt (cmp); original.txt SHA-256 equal to the sources.tsv row; CSS brace-depth scan ends at depth 0; `python3 review/build_review.py --check` passes for this package (its stamp reads STALE for the reason stated in the Status line and the per-theme record).

## Per-theme record — theme:darkblue-jp

### Verdict chain

- Ledger (b) row 179: NOT PASS. (c2) RENDER-S2-E (CN4): one DISPOSITIONED member (the page's T2 no-verdict coverage caveat) and one OPEN composite (sample overflow + sidebar-unreachable + runtime-hotlink), whose sidebar member became (e) item 52 and whose other members are the dispositioned cross-cutting classes of section 11. (c3) LOCALIZE-S2-D: P3 FIXED and P7 charged, becoming (e) items 50 and 51.
- FIX5 re-judgement (supplement (a) items 50-52): 50 FIXED and 51 FIXED (both by FIX5-FURNB, commit 25bb0b4), 52 DISPOSITIONED (FIX5-FURNB, no edit).
- Go-sign: issued 2026-11-17 (COMPLETION-REPORT section 10) over the population with these items closed.
- The generated stamp above reads STALE, and correctly: the verdict was computed against the 435a6bb-era candidate, and the current file also carries FIX5's own two edits (25bb0b4) and the usage-example sweep's specimen lines (b5cb724, the stamp's computed-against commit). No PASS is carried onto changed bytes; the three re-derivations below are against the packaged bytes.

### Item 50 re-derived (class B, FIXED)

Claim: the candidate carries no bare `[[module Rate]]`; the original's own bare Rate (its L22) was the duplicate the preview credit block made redundant.
Measured here: grep census — candidate 0 occurrences, original 1 (L22, inside the centering block at L21-23, between the credit pair). The FIX5-FURNB commit 25bb0b4 is in canonical history with the subject naming this closure class, and its checker line (5/1/2 -> 5/1/1) matches the removal of exactly the double-rate finding. CONFIRMED against the current bytes.

### Item 51 re-derived (class D, FIXED)

Claim (ledger class D: a JP font the port lacked): FIX5 added the Noto Sans JP load and its stack fallbacks.
Measured here: the @import stands at candidate L183, inside the delivered code block (L175-5143), after the four Latin imports the original already carried; the original has no JP font line anywhere. All four stacks carry the family: --UI-font-primary (cand L233), --mono-font (L236), --title-font (L237), --sans-serif-font (L238). Load and application are both present and both in operative CSS. CONFIRMED.

### Item 52 re-derived (class F, DISPOSITIONED)

Claim (FIX5-FURNB, no edit): the theme-owned off-canvas toggle — `#side-bar:is(:hover,:focus-within)` plus the tab pseudo-elements — is byte-identical to the original over the toggle regions; the machine check only looks for `.open-menu a`; T3 recorded no visual finding.
Measured here, region by region from this package's two files (SHA-256 prefixes of the joined lines):
- the hide rules: orig L1118-1128 = cand L1116-1126 (d5b86331cec5ee15);
- the mobile re-show rules: orig L1390-1405 = cand L1388-1403 (5ed7998ddff16722);
- the drawer and tab region: orig L1425-1500 = cand L1423-1498 (166acf75d805d4ad).
The operative hover/focus rule stands at orig L1451 = cand L1449, inside the third region. And the check's mismatch is visible in the bytes: `.open-menu a` is display:none unconditionally in both versions (orig L1122-1123 = cand L1120-1121, inside the first region) — the theme's design never uses the element the checker looks for, so "sidebar-unreachable" is the checker's vocabulary for a sidebar this theme opens by hover/focus-within instead. CONFIRMED, exactly as stated, over exactly the regions the disposition names.

### Second-reviewer walk

Item 52's ground passes the third-party test in the same way raisa's did: it names the mechanism, the regions, and the checker's blind spot, and every part re-measures from this package (done above). Items 50 and 51 are FIXED claims, and both re-derive from the bytes in one grep each. The walk then checked the disposition's neighborhood, as it must: item 52's identity claim covers the toggle regions, and a reader could easily take it as covering the sidebar furniture generally. It does not — two rules in that furniture, the scpnet-interwiki frame sizing at orig L1664-1672, are absent from the candidate, and no record names their removal (defect D1 below). The disposition stands; its scope is narrower than its phrasing suggests, and the package states the scope rather than letting the identity claim cover a drop it never measured.

### Defect flag (candidate packaged as it stands; no edits made by this lane)

- D1 — the scpnet-interwiki frame rules are dropped silently. Original L1664-1672: `div.scpnet-interwiki-wrapper { margin: 0; min-height: 0; }` and `iframe.scpnet-interwiki-frame { height: 0; }`. Candidate: no counterpart (grep for scpnet, interwiki-frame, interwiki-wrapper: zero). The rules size the interwiki frame the theme's own includes load; without them the frame takes its default height where the original collapses it. The drop predates every wave (already absent at the CN4 integrate commit cad7c86), and no lane report, ledger line, or disposition names it: the localize lane's pattern 8 line claims no sidebar-related hunk, and item 52's identity covers the toggle regions only. Classifier block B41 carries the deletion as unclassified CSS-BODY heuristic mass, which is how it passed the waves. Restore shape, for the coordinator: the two rules re-enter the code block at the original's position (after the :is(#side-bar, #interwiki) region, at the point corresponding to orig L1664).

### Record items (verified, not flags)

- The RedactRect @font-face removal (orig L178-186 and its stack name) is deliberate and recorded by the localize lane (pattern 4 APPLIED, section 4); it is not part of D1's silent-drop shape, and the package names it so the two removals are not confused.
- 作成年 2026 in the credit block is correct: a one-time wikidot.py fetch for this package (2026-11-17) shows the CN page created 2026-08-17 (rev 0), rev 3 on 2026-08-18, four revisions total. The mirror at rev 3 is one revision short of the page's full history and is nonetheless the reference revision the port was made from, with the follow-up diff recording no changes since.
- The credit title field （藏青 版式） copies the original's title because the body supplies no Japanese form (section 1); recorded under the supply-n-demand F2 ground, not flagged.
- The `type=sidebar` argument drop on both interwiki includes is the localize lane's recorded pattern 6 application (the JP component accepts only priority and theme), not drift.
- The head module and interwiki includes load the same two files twice by design of the original; the lane's rollup records the merge as a posting-time cleanup note.
- The sources.tsv supersession note for this row is wrong, in the ambrose shape: the note claims "original superseded upstream since the reference revision", but its own cited artifact (diff-darkblue-from3.txt) records rev 3 to rev 3, no changes. Correct form, recorded for the coordinator's harvest correction (this lane does not edit sources.tsv): "Upstream latest remains rev 3; the S2 artifact records rev3 to rev3, no changes; follow-up diff artifact diff-darkblue-from3.txt in the campaign record (K5a-i)".

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:darkblue-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP4, landing `050817e` (report `R/review-scout/FIX-RDISP4.md`).** One candidate repair (+9 lines), postdating this package's build at `b5cb724`.
- **D1 — scpnet-interwiki frame rules restored verbatim.** The two rules (original L1664–1672) now stand in the candidate's code block at the original's corresponding position — after the `:is(#side-bar, #interwiki) ::before` rule and before `a.close-menu` (candidate L1662–1670) — byte-identical to the original's nine lines including spacing (confirmed by direct comparison). Nothing else in the file changed.
Checker per the report: plain error 5 / warn 0 / info 1 → 5 / 2 / 1 and links error 5 / warn 1 / info 1 → 5 / 3 / 1. The five errors are the identical class (iii) pseudo-refs; the two added warns are the checker's standing `interwiki-touched` note, one per restored rule (rok-gov-base-jp carries the same warn), and no class (i) error is new.

## Appendix — residue blocks

- R1 = B8 (orig L28 -> cand at L32, residue). Resolution: the intro paragraph pair. The aligner shows only the removed side because the translation restructured the paragraph and its pairing landed in B9's added region: the translated intro stands at cand L35 (これは[[*user Agent FS|Agent FS]]が作った版式です。彼自身も何を土台にしたのか分からず、基底と玄武岩（Basalt）から大量のコードを写し取ったとのこと…), carrying the authorship credit and the bedrock/basalt borrowing statement. Argued in section 6.
- R2 = B11 (orig L88 -> cand L95, residue). Resolution: section 7 — the usage example's self-name include, in the sweep's settled posting form.
- R3 = B32 (orig L167 -> cand at L174, residue). Resolution: section 9 — a blank-line difference before the code block; formatting only.
- R4 = B10 (orig L85 -> cand L92, heuristic). Resolution: section 6 — the usage instruction line's translation ("ページの先頭に以下のコードを追加すると、この版式を適用できます："). The anchor test fails on the script change alone.
- R5 = B14 (orig L99 -> cand L106, heuristic). Resolution: section 6 — the six-hyphen divider specimen, translated with its [[*user placeholder-mcd]] joke intact.
- R6 = B15 (orig L101 -> cand L108, heuristic). Resolution: section 6 — the 67-hyphen specimen, footnote and all.
- R7 = B16 (orig L103 -> cand L110, heuristic). Resolution: section 6 — the heading specimen instruction, translated.
- R8 = B24 (orig L126 -> cand L133, heuristic). Resolution: section 7 — the visited-link specimen in the posting form.
- R9-R15 = B25-B31 (orig L130-157 -> cand L137-164, heuristic). Resolution: section 6 — the specimen section's remaining translation pairs (link, image, and formatting specimens), each one-to-one against the mirror; the heuristic label is the script delta, nothing else.
- R16 = B35 (orig L235 -> cand L233, heuristic) and R17 = B36 (orig L238-240 -> cand L236-238, heuristic). Resolution: section 8 — P7 font-stack rewrites by mechanism (item 51's application half, plus the recorded RedactRect name removal in B35), not unclassified churn.
- R18 = B41 (orig L1664-1672 -> cand at L1662, heuristic). Resolution: section 8 — the dropped scpnet-interwiki rules, defect D1. The CSS-BODY heuristic label is precisely the gap: a two-rule drop with no signature reads as churn.
