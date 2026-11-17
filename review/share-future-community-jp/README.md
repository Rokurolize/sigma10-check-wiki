# Review package — theme:share-future-community-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:share-future-community-jp — origin CN, population #226 [GOSIGN2-LEDGER (b) row 226]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 5f744298d4395987ef454a0f9fe493834b99c698543c10bfa17ffc4b9def8c86); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 3 warns / 0 infos (pseudo-ref×2, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 191; GOSIGN2-LEDGER (b) row 226]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 505–507px@≤375 (page) and 517–519px@≤375 + 881px@768 (sample), both engines, + runtime-hotlink site-theme chain + candidate host hoah.backroomswiki.cn (judgment-required); sample credit-modal (preview-form); T3 page overflow confirmed, penumbra-tb.png 404 (deferred); full-engine coverage (sample via the full-engine re-run, over-ceiling WebKit full-page screenshots skipped). [RENDER-ROWS-G (CN13)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN13)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 225, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 225]
- FIX5 re-judgement: item 81 (class I) FIXED — FIX5-STRUCTB §4, commit 435a6bb: personal-domain import repointed to the new fragment:share-future-community-base-css-jp, which vendors the fetched main.css (HTTP 200, 34,171 B) under a TASL header (ruling 4 / KB-14); spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) item 81; (c) check 3]
- Computed against: canonical commit 7e0fce743729c11754e7e60232b234e1d9a8c4f8; candidate file pages/theme:share-future-community-jp.txt sha256:5f744298d4395987ef454a0f9fe493834b99c698543c10bfa17ffc4b9def8c86; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | PASS (go-sign re-run; 286 of 286 pass-eligible themes, theme:amethyst-v2 the named exception) |
| Blocking items at ledger time | 1 — GOSIGN2-LEDGER §(e) item 81 (class I) |
| Re-judgment | FIXED (GOSIGN2-LEDGER-SUPPLEMENT, FIX5-STRUCTB §4, commit 435a6bb; spot-verified at supplement §(c) check 3); re-derived from this package's bytes in §Per-theme record |
| Standing items | T1 pseudo-ref ×2 and hotlink ×1 (dispositioned at register (c1)); the KB-11 credit-CSS restoration by FIX4-CREDIT (ledger §(c3)); render-row dispositions (page and sample overflow, site-theme chain, credit-modal preview form, deferred 404 image) |
| Defect flags raised by this package | 2 — the credit author field is a pointer in both carriers (§1), and a prose link names the plain `component:sigma-plus` page that will not exist on SCP-JP while the file's own delivery uses the -jp form (§7). Plus two observations for adjudication: the duplicated sigma-plus include (§2) and the load-only JP font supplement (§4). The candidate is not edited |
| Go-sign basis | GOSIGN2-LEDGER-SUPPLEMENT §(c) (ledger (c1)–(c3) + spot checks; check 3 is this theme's import line) |
| Named exception | None |

The stamp above reads STALE by design: it was computed against canonical commit b5cb7241f527a44933e45599b41df210690771c4, whose candidate bytes differ from the frozen verdict bytes (canonical 435a6bb) by exactly one line, the usage-example sweep's posting-name completion (candidate line 39, commit b5cb724). The stamp therefore does not carry the PASS onto changed bytes; the frozen ledger remains the verdict record. The sweep line is recorded in §2.

## Provenance

| | |
|---|---|
| Page | theme:share-future-community (CN) → theme:share-future-community-jp |
| Wiki | scp-wiki-cn (CN) |
| Reference revision | 1 (the original's first revision). The sources.tsv note claims the original was superseded upstream; the cited follow-up artifact records rev1 → rev1 with no changes, so the claim is wrong — see the discrepancy note below. The note's other content (the candidate ships the companion fragment; the original delivers its body from the external host hoah.backroomswiki.cn main.css) is accurate |
| Source of this copy | Mirror store, `orig-share-future-community-rev1.txt` (class COPY in the mirror INDEX) |
| original.txt | 620 lines, 17,169 B, SHA-256 dabd8baaedd6f8b49ced510590ce8f1a332ee9fd5ada3d320467c7cae5bdef83 (equals the sources.tsv value; last line unterminated, `wc -l` 619) |
| candidate.txt | 231 lines, 8,883 B, SHA-256 8311c84d548260c8cc1c20a7d3cab2552b0b1cd4080533bd6c39711e62e37770 (byte-identical to the canonical candidate) |

Kind: K5b-4 + K5b-5 (sources.tsv / SPECIAL-ROWS) — the candidate ships a companion fragment page, and the original delivers its body from an external host. The fragment is half of this theme's delivery and is treated in §Change set outside the two diffed files.

Discrepancy note (sources.tsv): the row's note claims "original superseded upstream since the reference revision; follow-up diff artifact diff-share-future-community-from1.txt in the campaign record (K5a-i)". The artifact (campaign record, `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-share-future-community-from1.txt`) records "scp-wiki-cn:theme:share-future-community rev1 → rev1 変更: なし" — no changes. The correct form is: upstream latest remains rev 1; the S2 artifact records rev1 to rev1, no changes. Recorded here and in the batch report for the coordinator's harvest correction; sources.tsv itself is not edited by this package.

Wave history: Stage 2 (CN13) integration → rework2-p4 → FIX-P4 → FIX4-CREDIT (the KB-11 restoration) → FIX5-STRUCTB (the blocking item; this commit is itself the canonical 435a6bb verdict head) → the usage-example sweep. Full commit list in §Multi-wave provenance.

## Summary

Share Future Community （命运共同体） is a Sigma+ skin whose original page is a documentation shell: its entire stylesheet lived outside the wiki, as `main.css` on the author's personal domain, imported by the head module and named again by the sidebar frame; the page's own code block held only the SCSS source as an exhibit. The candidate reverses that topology. The compiled CSS is vendored into a companion fragment page inside the JP delivery, the head module imports the fragment first and the candidate's own small code block second, and that block holds only the JP supplement — the JP font loads and the credit-module rules FIX4-CREDIT restored from the original's SCSS. The Sigma+ sample body is translated in place. The diff is +137/−526 lines in 72 blocks; the removed mass is the 447-line SCSS exhibit, whose compiled form is the fragment. The theme's one blocking item — the live delivery from the author's personal domain — is re-derived in §Per-theme record and its closure holds, spot check included. Two defects are flagged from the bytes: the credit author field names nobody in both carriers (§1), and a prose link still names the plain sigma-plus component page (§7).

## Standing sections

### 0. Provenance and header comments

**What.** The original's head declares the external delivery twice: the sigma-plus include (original line 1), then a `[[module css]]` whose only content is the `@import` of `https://hoah.backroomswiki.cn/SCP/theme-share-future-community/main.css` (lines 2–4), then the sidebar interwiki frame at priority=1 naming the same URL as its `theme=` with the encoded `css=` transparency parameter (lines 6–11). The candidate's head is the port's own apparatus: sigma-plus-jp (candidate line 1), a head module importing first the vendored fragment's draft-host `local--code` address and then its own code block's (lines 2–5), its own interwiki frame at priority=1 naming its own stylesheet (lines 7–10), the gate (line 11) and the credit block (lines 13–22) — after which the original's head pair follows, with sigma-plus-jp again at line 24 and the sidebar frame at lines 25–30, its theme target neutralized and its priority resolved to 2 (§2, §3). The provenance of the vendored CSS is declared in the fragment's own header and in the candidate's porter annotation (§10, §Change set).

**Why.** Pattern P4 / KB-14 with ruling 4: a theme's live CSS must be delivered from inside the port's own namespace, not from a third party's host; the vendoring route (fetch the external file, carry it as a companion page under a TASL header) is the campaign's settled remedy for the external-delivery shape.

**Verify.** `sed -n '1,30p'` on both files.

**Disposition.** The head's deliveries are class (iii) draft-stage forms at register (c1); the personal-domain import is item 81 (§Per-theme record).

### 1. Credit block, license box, rating and credit CSS (T1 / T7)

**What.** The candidate carries the T1 preview-form credit block inside the gate (candidate lines 13–22): タイトル 「運命共同体 テーマ」, 翻訳責任者 AI, 翻訳年 2026, 原題 「命运共同体 版式」, 作成年 2023, 初訳時参照リビジョン 1, and the 元記事リンク naming the original page on scp-wiki-cn.wikidot.com, the host sources.tsv records. **Defect flag:** the 著作権者 field (line 18) reads `原語版ページの作成者に同じ（scp-wiki-cn の theme:share-future-community）` — a pointer naming nobody — and the T4 license box at the tail (candidate lines 224–229) repeats the shape in its author parameter (line 225): `|author=scp-wiki-cn theme:share-future-community の作者`. The work names its authors in both files: the original's prose (line 30) reads 这是由 `[[*user hoah2333]]` 为 `[[*user Agent Phage]]` 制作的命运共同体版式 (made by hoah2333 for Agent Phage), its SCSS banner (line 177) reads "By hoah2333, Agent Phage", the candidate's own translated prose (line 36) names both users, and the vendored fragment's TASL header names 作者： hoah2333, Agent Phage. The repair form, for the coordinator: name hoah2333 and Agent Phage in each carrier's population form. Rating: the original's gated `[[module Rate]]` stood in a `[[>]]` div (original lines 15–18) beside a label div and a `credit:start`/`more`/`end` specimen with placeholder texts (original lines 20–28); neither stands in the candidate — its rate is the preview block's embedded one (classifier BARE-RATE-DEL, block B6; pattern P3), and the translated label lines survive as prose (candidate lines 32, 34). T7: the credit-module rules are this theme's KB-11 case — the port had dropped them, and FIX4-CREDIT (commit 9fbcd94) restored them into the candidate's code block (lines 204–220) from the original's SCSS exhibit, flattened from SCSS nesting, with the two modal rules lifted out of the original's `#page-content` scope because the JP credit modal is a sibling of `#page-content`; the restoring comment stands at candidate lines 197–203 and cites its source (the repo's copy of the original page, lines 492–519; in this package's original.txt the corresponding rules stand at lines 504–519). The license box's source note (candidate line 227) records that attachments on external hosts are re-hosted on the candidate page and that images without license statements in the original need author confirmation before posting.

**Why.** Ruling 3's TASL form requires the credit to name the rights holder (the pointer-form defect family, §0 of the batch report). KB-11 is the campaign's credit-CSS rule: a theme whose original styles the credit module must keep those rules in the port, or the JP credit modal renders unstyled.

**Verify.** `sed -n '13,22p' candidate.txt`; `sed -n '224,229p' candidate.txt`; `sed -n '30p;177p' original.txt`; `sed -n '197,220p' candidate.txt`.

**Disposition.** Credit block, license box and the KB-11 restoration stand in the PASS bytes (the restoration is ledger §(c3)'s KB-11 FIXED record, FIX4-CREDIT 9fbcd94). The two pointer values are flagged here and in the batch report as an open repair item; no ledger item charges this theme's credit fields, and the package is written against the candidate as it stands.

### 2. Includes and gates

**What.** Sigma-plus-jp stands twice (candidate lines 1 and 24) where the original included sigma-plus once (line 1): the port's inserted head took the first position and the original's body position kept its own copy. The duplication was visible to the waves — FIX4-CREDIT's commit record states it repointed *both* sigma-plus includes and resolved the sidebar frame's priority to 2 — so the pair stands as the waves left it; recorded here as an observation for adjudication (the parallel pair in theme:shancheng-jp was expressly accepted by the coordinator as behavior-identical). The candidate's own interwiki frame (lines 7–10) is new. The usage exhibit shows the posting form `@@[[include :scp-jp:theme:share-future-community-jp]]@@` (candidate line 39; the -jp completion is the sweep's line). The image-block include keeps the original's bare form (candidate line 46; §4). The gate localizes: `[[iftags +版式]]` → `[[iftags +テーマ]]` (candidate line 11).

**Why.** Ruling 4 / pattern P4 for the component port (sigma-plus-jp); KB-08 for the gate value. A duplicated base include is behavior-identical (the second include re-delivers the same component) but is recorded wherever it stands so the population census stays honest.

**Verify.** `grep -n 'sigma-plus' candidate.txt original.txt`; `sed -n '39p' candidate.txt`.

**Disposition.** The pair is an observation, not a charge; the sweep line is the stamp's STALE cause.

### 3. CSS delivery (imports, code blocks, cross-imports)

**What.** The delivery reversal described in §Summary. Candidate: head module imports (line 3) the fragment's draft-host `local--code/fragment%3Ashare-future-community-base-css-jp/1` and (line 4) its own `local--code/theme%3Ashare-future-community-jp/1`; the priority=1 frame names the candidate's own address. The candidate's own code block (lines 183–221, 39 lines) holds only the JP supplement (§1, §4) — it is not the theme's stylesheet, and no address claims it is: the stylesheet address (the fragment's /1) names the fragment's first code block, which holds the vendored CSS (the navla test passes on the fragment). The sidebar frame's `theme=` is a prose placeholder, `（作者の個人ドメインのCSS）` ("the author's personal-domain CSS", candidate line 28): the S2 porter neutralized the personal-domain URL there rather than repointing it, its `css=` transparency parameter survives byte-identical, and FIX4-CREDIT resolved the frame's priority from 1 to 2 when the candidate's own frame took priority 1. The CSS that frame used to name reaches the page through the line-3 fragment import instead. The personal domain survives only in provenance text: the porter annotation (candidate line 190) and the fragment's header — no live import names it anywhere in the delivery.

**Why.** KB-14 / pattern P4 (blocking form): first-position live delivery from an author's personal domain is the charge of item 81; the vendored fragment is its remedy (§Per-theme record). A frame left naming that domain would re-open the charge in a second carrier, so the neutralization is part of the same remedy's shape, with the priority resolution recorded by FIX4-CREDIT.

**Verify.** `sed -n '2,5p' candidate.txt`; `grep -rn 'hoah.backroomswiki.cn' candidate.txt pages/fragment:share-future-community-base-css-jp.txt` (provenance text only); brace-depth scan: both files and the fragment end at depth 0, never negative.

**Disposition.** Item 81 FIXED (§Per-theme record; supplement §(c) check 3 spot-verified the same facts).

### 4. Fonts and assets

**What.** This theme sets no font stacks of its own: neither the original's SCSS exhibit nor the vendored CSS contains a `font-family` declaration — typography is the Sigma+ base's. The candidate's code block loads Noto Sans JP and Noto Serif JP at its head (candidate lines 184–185, under the 日本語フォント comment). Observation (KB-16 mirror shape, weaker form): no stack in the candidate, in the fragment, or in `component:sigma-plus-jp`'s file names either face, so within this repo the loads are a load-only supplement; recorded for adjudication rather than flagged as a contradiction — unlike theme:shancheng-jp, no documentation in this file claims JP stacks, and no delivered stack names an unlocalized CJK face either. Assets: the sample image was re-hosted — the original's image-block borrowed `tb.png` from theme:penumbra's CN files (original line 40); the candidate's names `penumbra-tb.png` in its own draft-host files (candidate line 46), caption translated, width kept. The theme's remaining images stay direct-linked to their original hosts (7bye.com etc.), as the porter annotation records (candidate line 193) — the license box's re-hosting note (§1) and the annotation differ in scope: the note states the rule for attachments on external hosts such as sandbox wikis, the annotation states this theme's image policy; the one exhibit image in the pair was in fact re-hosted.

**Why.** Pattern P7's supplement is load + stack; where a theme's typography is entirely its base's, the load-only form is recorded so the census can judge it. The asset re-host follows the campaign's rule for images borrowed from another page's files.

**Verify.** `grep -n 'font-family' candidate.txt pages/fragment:share-future-community-base-css-jp.txt` (no hits); `sed -n '184,185p' candidate.txt`; `sed -n '46p' candidate.txt`.

**Disposition.** T3 recorded the re-hosted `penumbra-tb.png` as a 404 (deferred asset, KB-58 family) — the attachment-side half of the record. The font observation is open for adjudication.

### 5. Page furniture (header, sidebar, topbar)

**What.** The theme is a Sigma+ skin: header, sidebar and topbar are the base component's furniture. Its identity variables live in the vendored CSS: `--header-title: ""` and `--header-subtitle: ""` (fragment lines 14–15) — empty identity strings in the original's compiled CSS, carried verbatim into the fragment. The candidate page itself sets no header variables.

**Why.** Ruling 2 / KB-57: identity strings are the work's own marks; empty in the source, they stay empty. No furniture rule of the theme's own exists to localize.

**Verify.** `sed -n '10,16p' pages/fragment:share-future-community-base-css-jp.txt`.

**Disposition.** No furniture item charged.

### 6. Text translation

**What.** The Sigma+ sample body is translated throughout: headings, tabs, collapsibles, the link specimen table (its baidu and CN-host anchors kept as specimens, labels translated), quote and formatting specimens, and the SCSS note (candidate line 177), which keeps the author's GitHub link to the theme's SCSS repository as a source reference. Two GLYPH-FORM blocks record retained-string glyph conversion inside translated exhibits: the specimen heading 示例 → 例 (block B10) and the image caption 图像。 → 画像。 (B11). The author line is translated with both names kept as user links (candidate line 36; §1).

**Why.** KB-18 for the body; R5 glyph conversion for retained CN strings in translated matter (the converted forms are the Japanese glyph forms of the same characters).

**Verify.** diff.md's translation blocks (21 blocks, 52 lines by the generator's count); `sed -n '36p;177p' candidate.txt`.

**Disposition.** No mistranslation charged; T4 recorded 1 display-affecting finding for this theme, judged with its row.

### 7. Links

**What.** **Defect flag:** candidate line 41 reads 「運命共同体」テーマは`[[[component:sigma-plus|Sigma+]]]`テーマです — a prose link naming the plain `component:sigma-plus` page, which will not exist on SCP-JP. The file's own delivery includes `component:sigma-plus-jp` (lines 1, 24). The original's identical form (original line 36) resolved on scp-wiki-cn, where `component:sigma-plus` is that wiki's own page; carried over unchanged it is dead on SCP-JP — the snippet audit's drift class (a plain-form reference while the file's delivery uses the -jp form). One locus; the repair, for the coordinator, is the -jp form the delivery already uses. Kept links: the GitHub SCSS repository link (§6, a source reference to the author's archive), the specimen-table anchors (§6), and the credit block's 元記事リンク, which matches the recorded host (scp-wiki-cn.wikidot.com; no host defect).

**Why.** A theme page's prose is its documentation; a link in it that names a page the target wiki will not have is a broken instruction (the usage-reference rule, applied to prose by the snippet audit's classes).

**Verify.** `sed -n '41p' candidate.txt`; `sed -n '36p' original.txt`; `grep -n 'component:sigma-plus' candidate.txt`.

**Disposition.** Flagged as an open repair item (this package); uncharged by any ledger item.

### 8. Structure and exhibits

**What.** The gated body's order is preserved (rating labels, author line, usage, exhibits, source note, code collapsible, license box, gate close), with the port's head apparatus inserted before it (§0). The one large absence is the original's SCSS source exhibit (original lines 172–618, 447 lines inside the `[[code type="css"]]` block): it was not carried into the candidate page. Its compiled form is the vendored fragment (§Change set), and the collapsible that presented it survives (candidate lines 176–182) with its note translated — the "ソースコード" section now displays the candidate's own supplement block, while the SCSS source itself remains at the author's GitHub, linked in the note (candidate line 177). The classifier's three unlabeled heuristic blocks over the exhibit region (B68, B70, B71) are this absence aligning against the restored credit rules. The shape is the K5b-5 topology stated plainly: the original's live body was always external (main.css), so the exhibit was source documentation, and its live counterpart in the port is the fragment — the exhibit in the candidate is a pointer to that delivery, not a copy of the source.

**Why.** The content-presence rule requires the absence to be stated with its counterpart named, not absorbed into a delivery label; the DELIVERY-MOVE/exhibit adjudication is exactly this check.

**Verify.** `wc -l original.txt candidate.txt`; `sed -n '172,178p' original.txt`; `sed -n '176,182p' candidate.txt`; the fragment's line count (§Change set).

**Disposition.** Recorded as the theme's delivery shape; no item charges the exhibit's non-carriage, and the vendored fragment is the supplement of record for item 81.

### 9. Formatting

**What.** The generator counts 1 mechanical block (2 lines) and no re-indentation. The remaining churn is translation, the head insertion, and the exhibit absence (§8).

**Why.** Formatting-only change is reported as its own class.

**Verify.** diff.md's summary table.

**Disposition.** Mechanical; uncharged.

### 10. Porter annotations

**What.** Two annotations, both load-bearing. The code-block header comment (candidate lines 187–194, in Japanese) records the delivery history: the original served its CSS from the author's personal domain (hoah.backroomswiki.cn), the personal-domain delivery is a problem under KB-14 / pattern 4 and ruling 4, the CSS is therefore vendored into the fragment page which the head module imports, and the theme's images remain direct links to their original hosts. The FIX4-CREDIT restoration comment (candidate lines 197–203, in English) records the KB-11 restoration's source and its two scope adaptations (§1). The first annotation's history matters: before FIX5-STRUCTB it stated that the CSS was imported from the original URL as-is; commit 435a6bb rewrote it to the vendored account in the same commit that changed the import — the record and the bytes agree, which the reader can check in that commit.

**Why.** An annotation that contradicts the delivered bytes is itself a flag; here the wave updated the prose with the bytes, which is the correct shape and worth recording as verified.

**Verify.** `sed -n '187,203p' candidate.txt`; `git show 435a6bb -- pages/theme:share-future-community-jp.txt`.

**Disposition.** Both annotations stand as the port's delivery record.

### 11. Cross-cutting dispositions

**What.** The standing records touching this theme: T1's baseline (3 errors: pseudo-ref ×2 — the class (iii) draft-host addresses of §0/§3 — and hotlink ×1) dispositioned at register (c1). The render row (RENDER-ROWS-G, CN13) records page overflow 505–507px at ≤375px and sample overflow 517–519px / 881px at 768px, both engines; the runtime-hotlink site-theme chain (KB-40); the candidate host hoah.backroomswiki.cn as judgment-required — that judgment is item 81, closed by its fix (§Per-theme record), not dispositioned; the sample's preview-form credit modal (KB-32 / ruling 5); and T3's `penumbra-tb.png` 404 (§4). This theme belongs to the KB-11 confirmed set of five (ledger §(c3)), closed by FIX4-CREDIT (§1).

**Why.** Settled shapes are restated so the package does not re-charge them, and kept distinct from the package's two open flags (§1, §7) and two observations (§2, §4).

**Verify.** The verdict stamp's row citations (T1-ROWS row 191; RENDER-ROWS-G (CN13); LOCALIZE-ROWS row 225).

**Disposition.** All dispositioned as stated.

### 12. Verification

**What.** This package's own checks: original.txt SHA-256 equals the sources.tsv value (dabd8ba…5e83, §Provenance); candidate.txt is byte-identical to the canonical candidate (`cmp` against `pages/theme:share-future-community-jp.txt`); the classifier ran with the fragment declared as a companion (`--companions`), and classification.json regenerates cleanly; the item-81 re-derivation below is checkable from the two files, the fragment, and commit 435a6bb. Campaign-side: the stamp's T1 baseline and the supplement's §(c) check 3.

**Why.** The reader must be able to re-run the cheapest deciding check from this repo alone, for the closure and for each flag.

**Verify.** `sha256sum original.txt`; `cmp candidate.txt pages/theme:share-future-community-jp.txt`; `python3 review/build_review.py --check`.

**Disposition.** PASS stands on the frozen ledger for the charged item; the two flags await coordinator repair.

## Per-theme record

**Ledger item 81 — class I (personal-domain live delivery).** The ledger (§(e) item 81, from LOCALIZE-S2-E) charged: the theme's first CSS import delivered live from the author's personal domain — candidate line 3 named `https://hoah.backroomswiki.cn/SCP/theme-share-future-community/main.css` — pattern P4 in its blocking form, expressly not in the FIX-P4 set and not in the KB-14 verbatim-import set. The supplement records it FIXED (FIX5-STRUCTB §4) at commit 435a6bb, and its §(c) check 3 spot-verified the result. Re-derived from the bytes: `git show 435a6bb` changes candidate line 3 to `@import url('https://sigma10-jp-test.wdfiles.com/local--code/fragment%3Ashare-future-community-base-css-jp/1');`, rewrites the porter annotation to the vendored account (§10), and creates the fragment file — the current candidate line 3 is that import, and `grep` finds the personal domain in the delivery only inside provenance text (candidate line 190; the fragment's header). The vendored file: the fetched main.css measured 34,171 B (the wave's record); the fragment file in this repo is 13,744 B / 392 lines, and its header states that the build artifact's `sourceMappingURL` comment was removed — the byte difference is the removed build comment, as the header records. The fragment opens with the original's banner ("Share Future Community Theme / [2023 Wikidot Theme] / Based on Sigma+ / By hoah2333, Agent Phage") under its TASL header naming 作者 hoah2333, Agent Phage and the source page. Closure holds, including the supplement's spot check.

**The stamp's STALE cause.** Commit b5cb724 (the usage-example sweep) changed exactly one line after the verdict bytes: candidate line 39, the escaped usage include completed from `theme:share-future-community` to `:scp-jp:theme:share-future-community-jp` (§2). Note the adjacency the sweep left behind: the repaired exhibit at line 39 now names the -jp form while the prose link two lines below (line 41) still names the plain component page — the §7 flag.

## Post-package repairs (REFRESH3-J)

The items above describe this package as built. The repairs recorded below postdate the package build; `candidate.txt` has been recopied from the current canonical `pages/theme:share-future-community-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RFIX12 Item 3 — credit pointer, both carriers named (landing 7e0fce7, "pages: R-fix-12 flags repaired (shancheng, share-future)"; record FIX-RFIX12.md).** As built, the credit block (candidate L18) read `**著作権者:** 原語版ページの作成者に同じ（scp-wiki-cn の theme:share-future-community）` and the license-box author parameter (candidate L225) read `|author=scp-wiki-cn theme:share-future-community の作者]]`. The work names its authors in the original prose (original L30, L177 banner), the candidate's own prose (L36) and the companion fragment's TASL header. The remedy (one line each): credit L18 → `**著作権者:** hoah2333 & Agent Phage`, license-box parameter → `|author=hoah2333 & Agent Phage]]`, the population's repaired two-author form (path-of-jinin / FIX-JININ precedent).

**FIX-RFIX12 Item 4 — prose link completed to the -jp posting name (landing 7e0fce7; record FIX-RFIX12.md).** As built, candidate L41 read 「運命共同体」テーマは[[[component:sigma-plus|Sigma+]]]テーマです, naming the plain `component:sigma-plus` page that will not exist on SCP-JP, while the file's own delivery includes `component:sigma-plus-jp` (L1, L24) and the sweep had already repaired the usage exhibit two lines above (L39). The remedy changed L41 to `component:sigma-plus-jp`, label `Sigma+` and the rest unchanged; under `--check-links` the warning is now the known link-target-missing posting-resolution class for the not-yet-posted candidate name. The batch's two observations were deliberately left untouched (duplicated sigma-plus include L1/L24; load-only JP font supplement L184–185). Per FIX-RFIX12.md the T1 finding set is byte-identical before and after (share-future-community error 3 / warn 1 / info 0, all three errors pseudo-ref); class (i) 0 → 0.

## Change set outside the two diffed files

- `pages/fragment:share-future-community-base-css-jp.txt` — the vendored base CSS: 392 lines, 13,744 B. Header (lines 1–7, Japanese): the page is the vendored copy of the `main.css` the original served from hoah.backroomswiki.cn; source `https://scp-wiki-cn.wikidot.com/theme:share-future-community`; 作者 hoah2333, Agent Phage; image and font license statements follow the candidate page's credit; the fetched file's `sourceMappingURL` comment was removed. Body: the compiled stylesheet, opening with the original's banner and its `:root` (including the empty `--header-title` / `--header-subtitle`, §5), closing with the hovertip rules. This page is the theme's actual stylesheet delivery (§3).
- `pages/theme-decoration-sample-share-future-community-jp.txt` — the render-check sample the T2/T3 rows measured.
- The candidate's own draft-host attachment `penumbra-tb.png` (§4).
- A note for readers of the FIX4-CREDIT record: the repo's `pages/theme:share-future-community.txt` is byte-identical to this package's original.txt — the campaign's canonical copy of the CN page, and the file the restoration comment (§1) cites as its source.

## Multi-wave provenance

| Commit | Wave | Change to this candidate |
|---|---|---|
| 816deb1 | Stage 2 (CN13) integration | The port created: translation, credit block, sidebar neutralization |
| 7d9877c | rework2-p4 | Base-separation rework |
| f1138e4 | FIX-P4 | Delivery repair |
| 9fbcd94 | FIX4-CREDIT | KB-11 credit rules restored; both sigma-plus includes repointed; sidebar priority resolved to 2 |
| 435a6bb | FIX5-STRUCTB | Item 81 repaired: fragment vendored, line-3 import repointed, annotation rewritten (§Per-theme record). This commit is the canonical verdict head |
| b5cb724 | Usage-example sweep | Line 39 posting-name completion (the stamp's STALE cause) |

## Appendix: residue and heuristic resolution

Residue blocks: 0 of 72. Heuristic blocks: 42 of 72, in three shapes. (1) Translation mass over the Sigma+ sample body (TRANS-UNANCHORED and TRANSLATION-ANCHORED blocks B9–B67) — §6. (2) The SCSS exhibit region's three unlabeled blocks (B68: original lines 268–384 → candidate 207–208; B70: 391–448 → 213–215; B71: 450–616 → 217–219), which are the exhibit absence of §8 aligning against the restored credit rules — resolved there, not waived. (3) CSS-BODY spans inside the candidate's supplement block — the restored credit rules of §1, whose content is adjudicated there. No heuristic block hides a delivery or credit change beyond those adjudicated in §1, §3 and §8.
