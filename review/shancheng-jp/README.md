# Review package — theme:shancheng-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:shancheng-jp — origin CN, population #225 [GOSIGN2-LEDGER (b) row 225]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 6e14d11e4cd13b8606a4ef204008e1701f9cd1be17a50d6eaa774f57dbc2bd32); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 1 info (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 190; GOSIGN2-LEDGER (b) row 225]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 505–519px@≤375 + 854–859px@768 (page) and 517–531px@≤375 + 951px@768 (sample), both engines, + runtime-hotlink site-theme chain; sample credit-modal (preview-form); T3 page overflow confirmed, decorative images 404 (deferred); full-engine coverage (sample via the full-engine re-run, over-ceiling WebKit full-page screenshots skipped). [RENDER-ROWS-G (CN13)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN13)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 224, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 224]
- FIX5 re-judgement: item 80 (class H) FIXED — FIX5-TEXTA §9, commit 6f6b349: Chinese tags chrome label translated [GOSIGN2-LEDGER-SUPPLEMENT (a) item 80]
- Computed against: canonical commit 7e0fce743729c11754e7e60232b234e1d9a8c4f8; candidate file pages/theme:shancheng-jp.txt sha256:6e14d11e4cd13b8606a4ef204008e1701f9cd1be17a50d6eaa774f57dbc2bd32; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | PASS (go-sign re-run; 286 of 286 pass-eligible themes, theme:amethyst-v2 the named exception) |
| Blocking items at ledger time | 1 — GOSIGN2-LEDGER §(e) item 80 (class H) |
| Re-judgment | FIXED (GOSIGN2-LEDGER-SUPPLEMENT, FIX5-TEXTA §9, commit 6f6b349); re-derived from this package's bytes in §Per-theme record |
| Standing items | T1 pseudo-ref ×8 (class (iii) draft-stage deliveries, dispositioned at register (c1)); FIX-P4 §9 named exception (the fossil/1 sidebar address, adjudicated posting-correct); the un-deduplicated sigma-plus lines (coordinator-accepted as behavior-identical, ledger §(c3)); render-row dispositions (page and sample overflow, site-theme chain, credit-modal preview form) |
| Defect flags raised by this package | 2 — the credit author field is a pointer in both carriers (§1), and the JP font faces are loaded but applied by no delivered stack while the theme's documentation claims them (§4). Neither is charged by any ledger item; both are flagged for the coordinator, and the candidate is not edited |
| Go-sign basis | GOSIGN2-LEDGER-SUPPLEMENT §(c) (ledger (c1)–(c3) + spot checks) |
| Named exception | FIX-P4 §9: theme:fossil/1 (the base theme's address in the sidebar frame) |

The stamp above reads STALE by design: it was computed against canonical commit b5cb7241f527a44933e45599b41df210690771c4, whose candidate bytes differ from the frozen verdict bytes (canonical 435a6bb) by exactly one line, the usage-example sweep's repair of the Fossil prose link (candidate line 37, commit b5cb724). The stamp therefore does not carry the PASS onto changed bytes; the frozen ledger remains the verdict record. The sweep line is recorded in §7.

## Provenance

| | |
|---|---|
| Page | theme:shancheng (CN) → theme:shancheng-jp |
| Wiki | scp-wiki-cn (CN) |
| Reference revision | 14 (first-translation revision). The sources.tsv note claims the original was superseded upstream; the cited follow-up artifact records rev14 → rev14 with no changes, so the claim is wrong — see the discrepancy note below |
| Source of this copy | Mirror store, `orig-shancheng-rev14.txt` (class COPY in the mirror INDEX) |
| original.txt | 2,464 lines, 68,089 B, SHA-256 bdd5040756a58e689f0d0fcf402dbc685613d8beca086c411e435265206bf45f (equals the sources.tsv value; last line unterminated, `wc -l` 2,463) |
| candidate.txt | 2,425 lines, 69,390 B, SHA-256 18378266f530d3cc9d4840e2bb24b89edcebcf82e7a4dbe9c705e1d5196fadf7 (byte-identical to the canonical candidate) |

Discrepancy note (sources.tsv): the row's note reads "original superseded upstream since the reference revision; follow-up diff artifact diff-shancheng-from14.txt in the campaign record (K5a-i)". The artifact (campaign record, `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-shancheng-from14.txt`) records "scp-wiki-cn:theme:shancheng rev14 → rev14 変更: なし" — no changes. The correct form is: upstream latest remains rev 14; the S2 artifact records rev14 to rev14, no changes. Recorded here and in the batch report for the coordinator's harvest correction; sources.tsv itself is not edited by this package.

Wave history: Stage 2 (CN13) integration → FIX-P4 → FIX4-SIGMA → FIX5-TEXTA (the blocking item) → the usage-example sweep. Full commit list in §Multi-wave provenance.

## Summary

Shancheng （山城） is a CN theme derived from the EN Fossil theme. The original page delivers its CSS twice: a 1,172-line live `[[module CSS]]` and a near-identical 1,160-line code exhibit, behind a sigma-plus include and a sidebar frame that names the Fossil stylesheet. The candidate consolidates the two copies into a single 2,270-line delivered code block (the classifier's topology move scores the pair at 0.992 similarity), puts its own delivery frame and credit block at the head, translates the gated documentation body, and closes with a license box the original never had. The diff is +1,250/−1,289 lines in only 10 change blocks, because the consolidation aligns as bulk movement rather than line edits. The theme's one blocking item — a Chinese chrome label left in a CSS `content:` string — is re-derived in §Per-theme record and its closure holds. Two further defects surfaced from the bytes and are flagged, not narrated away: the credit author field names nobody in both of its carriers (§1), and the JP font supplement loads two faces that no delivered stack uses, while the theme's own documentation says the stacks carry them (§4).

## Standing sections

### 0. Provenance and header comments

**What.** The original's head is two deliveries: the sigma-plus include (original line 1) and, inside a sidebar div (lines 2–8), an interwiki frame naming the Fossil stylesheet (`theme:fossil/1` on scp-wiki.wdfiles.com, with the encoded `css=` filter parameter). The candidate's head is the port's own apparatus: sigma-plus-jp (candidate line 1), a head module importing its own code block from the draft host (lines 2–4), its own interwiki frame at priority=1 naming the same (lines 6–9), the gate (line 10) and the credit block (lines 12–21) — after which the original's head content follows, with sigma-plus-jp again at line 23 and the sidebar div and its fossil frame at lines 24–31. The porter's provenance statement stands at the head of the delivered code block (§10).

**Why.** The candidate must be self-delivering on SCP-JP (pattern P3 delivery pair; class (iii) draft-stage form per FIX-CODEADDR.md). The fossil frame in the sidebar is the original's own furniture, kept and repointed (§2, §11) rather than replaced.

**Verify.** `sed -n '1,31p'` on both files.

**Disposition.** Standing class (iii) deliveries at register (c1); the fossil address is the FIX-P4 §9 named exception (§11).

### 1. Credit block, license box, rating and credit CSS (T1 / T7)

**What.** The candidate carries the T1 preview-form credit block inside the gate (candidate lines 12–21): タイトル 「山城 テーマ」, 翻訳責任者 AI, 翻訳年 2026, 原題 「山城 版式」, 作成年 2025, 初訳時参照リビジョン 14, and the 元記事リンク naming the original page on scp-wiki-cn.wikidot.com, the host sources.tsv records. **Defect flag:** the 著作権者 field (line 17) reads `原語版ページの作成者に同じ（scp-wiki-cn の theme:shancheng）` — "same as the creator of the original-language page" — a pointer that names nobody. The original names its author in its own prose (original line 1194): 这是 `[[*user Odeo]]`为关注地点「山城」和其相关的所有东西制作的版式 — the theme was made by Odeo, modified from the Fossil theme — and the candidate's own translated prose names the same person (candidate line 37: `[[*user Odeo]]`が…制作したテーマ). The same pointer stands in the second carrier: the T4 license box at the tail (candidate lines 2417–2423) carries `|author=scp-wiki-cn theme:shancheng の作者` (line 2420). The original carries no credit block with fields and no license box (its `credit:start` / 示例 / `credit:end` at original lines 1188–1190 is a specimen exhibit, §8), so both pointer values are the port's own entries, not inherited text. The repair form, for the coordinator: name Odeo in each carrier's population form. Rating: the original's only rating furniture is a gated `[[module rate]]` (original line 1185, beside the credit specimen); the candidate has no module rate — its rate is the preview block's embedded one (P3), so no duplication arises. T7: the credit-module CSS is inherited, not supplemented — `div.creditButton p a` rules stand in both of the original's copies (original lines 749, 2016) and in both of the candidate's consolidated copies (candidate lines 816, 1982), byte-inherited, with the rate-box rules beside them (candidate lines 790, 1956). The descendant form (`p a`, not KB-11's canonical `> a`) is the original's own form; this theme was not in the FIX4-CREDIT supplement set. Recorded as a standing observation for adjudication, on the nameless precedent (inherited descendant-form rules recorded, untouched), not as a repair flag.

**Why.** Ruling 3's TASL form exists so the credit names the rights holder; a pointer field fails the form's purpose even though every other field is complete (the pointer-form defect family). Pattern P3 covers the block and its embedded rate.

**Verify.** `sed -n '12,21p' candidate.txt`; `sed -n '2417,2423p' candidate.txt`; `sed -n '1194p' original.txt`; `grep -n 'creditButton' candidate.txt original.txt`.

**Disposition.** The credit block and license box are part of the PASS bytes as supplements; the two pointer values are flagged here and in the batch report as an open repair item for the coordinator. The item is not a ledger charge — no (e) item covers this theme's credit fields — and the package is written against the candidate as it stands.

### 2. Includes and gates

**What.** Sigma-plus: the original's `:scp-wiki-cn:component:sigma-plus` (line 1) becomes `component:sigma-plus-jp` at candidate line 1 — and again at candidate line 23, where the original's body content repeats the include position after the port's inserted head (duplication dispositioned in §11). The candidate's own interwiki frame (lines 6–9) is new; the original's sidebar frame is repointed from `:scp-wiki-cn:` to `:scp-jp:component:interwiki-style` with its fossil target rewritten (§3). The image-block exhibit is repointed to `:scp-jp:component:image-block` (candidate line 60). The usage exhibit shows the posting form `@@[[include :scp-jp:theme:shancheng-jp]]@@` (candidate line 42). The gate localizes: `[[iftags +版式]]` → `[[iftags +テーマ]]` (candidate line 10).

**Why.** Include repoints keep the delivery inside the JP namespace (pattern P4; ruling 4 for component ports — sigma-plus-jp is the JP port of the base component). The gate value is the JP tag name (KB-08).

**Verify.** `grep -n 'include' candidate.txt | head -20`; `sed -n '10p' candidate.txt`.

**Disposition.** Standard mechanics; the duplicated sigma-plus is dispositioned, not charged (§11).

### 3. CSS delivery (imports, code blocks, cross-imports)

**What.** The structural core of the port. Original delivery: sigma-plus (line 1) + a live `[[module CSS]]` at lines 11–1182 (copy A) + a `[[code type="css"]]` exhibit at lines 1302–2461 (copy B, near-identical). Candidate delivery: the head module (lines 2–4) imports the candidate's own draft-host `local--code/theme%3Ashancheng-jp/1`, the priority=1 frame (lines 6–9) names the same address, and a single `[[code type="css"]]` block at lines 146–2415 (2,270 lines) holds the consolidated stylesheet — the classifier's topology records the move module-css [10,1182] → code-css [145,2415] at 0.992 similarity. The named block is the stylesheet (the navla test passes: the address names the block that holds the CSS, and it is the large one). The Fossil base is carried inline inside that block (the porter's annotation, §10, records the integration and its ground: fossil does not exist on SCP-JP); the fossil/1 URL survives only in the sidebar frame, repointed to the production files host `https://scp-jp.wdfiles.com/local--code/theme%3Afossil/1` (candidate line 28, unencoded-colon host form). The base's two page images are re-hosted from the author's CN sandbox wiki into the candidate's own draft-host attachments: `--fossil-header` → `chaotianmen.jpg` and `--fossil-footer` → `rock1.jpg` (candidate lines 1326–1329, blocks B7/B8). The exhibit copy's five duplicate `@import` lines were deduplicated in the consolidation (classifier DUPIMPORT-DEL, original lines 1303–1307).

**Why.** Pattern P1/P2 delivery localization with the KB-20 inlined-base shape: where the base theme has no JP page to import, the base CSS is integrated into the candidate's own delivery and the fact is declared in the porter annotation. The sidebar frame's fossil address is the adjudicated exception (FIX-P4 §9), because the frame is a sidebar-type delivery whose target the supervisor record judged posting-correct.

**Verify.** `grep -n 'local--code' candidate.txt`; `sed -n '146,153p' candidate.txt`; brace-depth scan: both files end at depth 0, never negative.

**Disposition.** Delivery repoint and consolidation stand in the PASS bytes; the fossil sidebar address is the §9 named exception (§11).

### 4. Fonts and assets

**What.** The consolidated block's import head (candidate lines 147–153) does four things: adds Noto Sans JP and Noto Serif JP loads first (lines 147–148); re-hosts the three Latin faces (Półtawski Nowy, Public Sans, Sometype Mono) from `api.fonts.coollabs.io` to `fonts.googleapis.com` with identical family and axis parameters; and keeps the Noto Sans SC and Noto Serif SC loads (lines 152–153). **Defect flag (KB-16 mirror shape, compounded by a documentation claim):** no delivered stack names either JP face. The module-derived copy's `:root` (candidate lines ~212–215) dropped `'Noto Sans SC'` from `--body-font` and `'Noto Serif SC'` from `--mono-font` without substituting a JP face, leaving `'Public Sans', Inter, Nanum Gothic` and `'Sometype Mono', 'Courier New'`; the exhibit-derived copy's `:root` (candidate lines 1257–1260) keeps `'Noto Sans SC'` and `'Noto Serif SC'` verbatim, and because it stands later in the single delivered block it wins the cascade for those two variables. The SC faces remain loaded (lines 152–153), so the delivered page renders its CJK text in the SC faces — the state the JP supplement exists to replace. The candidate's own documentation contradicts the delivered bytes: candidate lines 131–135 state ヘッダーフォントはPółtawski Nowy / Noto Sans JPです。本文フォントはPublic Sans / Noto Sans JPです。等幅フォントはSometype Mono / Noto Serif JPです. The base theme's JP port shows the intended forms: `theme:fossil-jp` lines 210–212 carry `"Noto Sans JP"` in all three variables (`--header-font`, `--body-font`, `--mono-font`), replacing the SC names. The classifier corroborates the shape: this package has a JPFONT-LOAD span and no JPFONT-STACK span. Repair, for the coordinator: give the delivered `:root` variables the fossil-jp forms (JP faces in the stacks the documentation claims); the package is written against the candidate as it stands. Assets: §3's two re-hosted images, plus the image-block exhibit's `odeo.png`, re-hosted from the author's sandbox files into the candidate's own draft-host files (candidate line 60).

**Why.** Pattern P7 / KB-16: the supplement is the pair (load + stack). A load no stack names is dead weight, and a stack naming an unlocalized face defeats the supplement's purpose; where the theme's documentation asserts the JP form, the bytes and the prose cannot both stand.

**Verify.** `sed -n '147,153p' candidate.txt`; `grep -n 'Noto Sans JP\|Noto Serif JP' candidate.txt` (hits only at lines 147–148 and in the documentation prose); `sed -n '1257,1260p' candidate.txt`; compare `pages/theme:fossil-jp.txt` lines 210–212.

**Disposition.** Flagged as an open repair item (this package); not charged by ledger item 80 or any (e) item. The Latin-face re-host (coollabs → Google Fonts, parameters unchanged) is a host-form normalization in the PASS bytes.

### 5. Page furniture (header, sidebar, topbar)

**What.** The header identity is variable-driven: `--header-title: 0` stands in the candidate exactly once (line 1257) — the original carried it in both copies (original lines 24, 1315), and the classifier's HEADERVAR span (original [1314,1315], candidate none) records the deduplication in consolidation, not a drop. `--header-font` keeps Półtawski Nowy first (candidate line 213). The sidebar furniture is the original's own div and fossil frame (§0, §3). The page-tags chrome label is a `content:` string and is §6/§Per-theme record (item 80).

**Why.** Header and identity variables are the theme's rendered furniture (KB-57 family); the zero title is the original's own setting (the theme shows no text title), carried unchanged.

**Verify.** `grep -n 'header-title' candidate.txt original.txt`; `sed -n '1257,1260p' candidate.txt`.

**Disposition.** No furniture item charged.

### 6. Text translation

**What.** The gated documentation body is translated throughout (the region between the credit block and the code block, candidate lines 32–145): the author's introduction (naming Odeo and the Fossil derivation), the usage instructions, the font documentation (§4), and the feature exhibits, including the image-block exhibit with its re-hosted `odeo.png` and translated caption (candidate line 60). The one charged string: the page-tags chrome label `content: "标签"` became `content: "タグ"` (candidate line 1270) — item 80, re-derived in §Per-theme record. The same rule's English form `content: "TAGS"` stands in both files (original lines 1039, 2306 → candidate lines 1106, 2272): the original itself carries the rule in both language forms across its copies, the English form is the Fossil base's variant, and no record charges it; it stands as delivered. CSS comments inside the consolidated block translate with the code (COMMENT-TEXT mass inside block B5; §Appendix).

**Why.** KB-18: body prose and rendered chrome strings are visible text. The tags label is chrome UI text, which the ledger ruled outside ruling 2's header-language scope — the ground of item 80's charge.

**Verify.** `grep -n 'content: "' candidate.txt | grep -i 'タグ\|TAGS'`; `grep -c '标签' candidate.txt` (0).

**Disposition.** Item 80 FIXED (§Per-theme record); the "TAGS" copies are standing, uncharged.

### 7. Links

**What.** Two link shapes. The Fossil prose link (candidate line 37) names the base theme's JP port in external-URL form, `https://scp-jp.wikidot.com/theme:fossil-jp` — the usage-example sweep's repair (commit b5cb724; the pre-sweep line named `theme:fossil`). The 「山城」 hub links keep their CN URLs (candidate lines 37, 41): the setting's hub is a CN page, no JP counterpart is named in any record, and the labels are translated while the targets stand as the original's. The credit block's 元記事リンク matches the recorded host (scp-wiki-cn.wikidot.com); no host defect.

**Why.** Pattern P11 is counterpart-driven: the Fossil link repoints because the JP port exists (and this candidate's own delivery depends on it, §3); the hub links keep because the reference is the CN setting page itself.

**Verify.** `sed -n '37p;41p' candidate.txt`; `git show b5cb724 -- pages/theme:shancheng-jp.txt`.

**Disposition.** The sweep line is the stamp's STALE cause; the kept CN targets are standing.

### 8. Structure and exhibits

**What.** The gated body's order is preserved (documentation, exhibits, code block, license box, gate close), with the port's head apparatus inserted before it (§0) and the license box added at the tail (§1). Two original exhibits have no candidate counterpart, both adjudicated: the credit specimen (original lines 1188–1190 — `credit:start`, the word 示例 ("specimen"), `credit:end`) is replaced by the candidate's real credit block at the head, and the escaped `@@[[module css]]@@` specimen (original lines 1206–1214) lapses with the delivery change it documented (the original's module delivery is now the candidate's code-block delivery, §3). The classifier's RESTORATION label on the consolidated block (B5) is its name for the block's match against the original's earlier region; adjudicated as consolidation (§3), not a restoration of deleted content. Its three EXHIBIT-RESTRUCTURE labels (B1, B2, B9) record the head insertion and the gated tail's reorganization, adjudicated against the exhibit census above.

**Why.** The content-presence rule cuts both ways: a dropped exhibit is a flag, and a specimen whose referent the port replaced is recorded as replaced, with the replacement named.

**Verify.** `sed -n '1183,1214p' original.txt` against the candidate's head and tail.

**Disposition.** No structural item charged; the two lapsed specimens are recorded here so the census is complete.

### 9. Formatting

**What.** The generator counts 1 mechanical block (2 lines) and no re-indentation (reindent count 0). The bulk churn (+1,250/−1,289) is the consolidation alignment (§3), not formatting.

**Why.** Formatting-only change is reported as its own class so it is not mistaken for content change.

**Verify.** diff.md's summary table; classification.json's WS-ONLY absence (no span of that label fires for this pair).

**Disposition.** Mechanical; uncharged.

### 10. Porter annotations

**What.** One load-bearing annotation, at the head of the delivered code block (candidate lines 155–160, in Japanese): the original is based on EN theme:fossil by EstrellaYoshte; the theme's CSS stands in the page's module CSS (code file 1 has identical content, so the module side was adopted as the source copy); fossil does not exist on SCP-JP, so the base CSS is integrated into this file and the base's four images are attachments. A one-line comment follows at line 161 marking the JP font import group (§4). The annotation's delivery claims check against the bytes: the delivered block is the module copy's lineage (§3), and the base CSS is inline.

**Why.** Pattern P1's inlined-base shape (KB-20) requires the integration to be declared where a reader of the delivered file will find it; this annotation is that declaration, and §3/§4 cite it as the porter's record.

**Verify.** `sed -n '155,161p' candidate.txt`.

**Disposition.** The annotation stands as the porter's provenance statement; §4 flags where the delivered font bytes diverge from the body documentation (a different text from this annotation).

### 11. Cross-cutting dispositions

**What.** The standing records touching this theme: (a) the duplicated sigma-plus include (candidate lines 1 and 23) — the ledger §(c3) recorded keeps accept this theme's un-deduplicated sigma-plus lines as behavior-identical (FIX4 mop-up record), so the pair is dispositioned, not a defect; (b) the sidebar frame's fossil/1 address on the production files host — FIX-P4 §9's named exception, adjudicated posting-correct in the supervisor record; (c) this theme's duplicate-priority frame form belongs to the KB-07 family the ledger records as adjudicated posting-correct for shancheng (the candidate resolves the duplication by giving its own frame priority 1 and keeping the sidebar frame's form); (d) T1's eight pseudo-ref errors are the class (iii) draft-host addresses (§0, §3); (e) the render row records page overflow 505–519px at ≤375px and 854–859px at 768px, sample overflow 517–531px / 951px, both engines, the site-theme chain (KB-40), the sample's preview-form credit modal (KB-32 / ruling 5), and T3's decorative-image 404s (KB-58 deferred assets). The T7 descendant-form observation is §1.

**Why.** These are settled in their registers; restating them keeps the package from re-charging settled shapes, and keeps the two genuinely open flags (§1, §4) distinct from them.

**Verify.** The verdict stamp's row citations (T1-ROWS row 190; RENDER-ROWS-G (CN13); LOCALIZE-ROWS row 224); ledger §(c3) and §9 of FIX-P4 as cited.

**Disposition.** All dispositioned as stated; the §1 and §4 flags are the package's only open items.

### 12. Verification

**What.** This package's own checks: original.txt SHA-256 equals the sources.tsv value (bdd5040…206bf, §Provenance); candidate.txt is byte-identical to the canonical candidate (`cmp` against `pages/theme:shancheng-jp.txt`); classification.json regenerates cleanly (`classify_hunks.py --check`); the item-80 re-derivation below is checkable from the two files plus commit 6f6b349; the §4 flag is checkable by the greps cited there. Campaign-side: the stamp's T1 baseline (8 errors / 1 warn / 1 info, pseudo-ref ×8) and the render/localize rows.

**Why.** The reader must be able to re-run the cheapest deciding check from this repo alone, for the closure and for each flag.

**Verify.** `sha256sum original.txt`; `cmp candidate.txt pages/theme:shancheng-jp.txt`; `python3 review/build_review.py --check`.

**Disposition.** PASS stands on the frozen ledger for the charged item; the two flags await coordinator repair.

## Per-theme record

**Ledger item 80 — class H (untranslated chrome text).** The ledger (§(e) item 80, from LOCALIZE-S2-E) charged: the page-tags chrome label stood in Chinese, `content: "标签"`, at ledger-time candidate line 1270 — chrome UI text, which ruling 2's header-language scope does not cover (pattern P9 family). The supplement records it FIXED (FIX5-TEXTA §9) at commit 6f6b349. Re-derived from the bytes: `git show 6f6b349` changes exactly one line in this file, `"标签"` → `"タグ"` in the `#main-content.page-tags::before` rule, and the current candidate line 1270 reads `content: "タグ";`. The copy census, for completeness: the original carries the rule four times across its two copies — 标签 at original lines 37 and 1328, "TAGS" at lines 1039 and 2306; the candidate's consolidated block carries it three times — "TAGS" at line 1106, タグ at line 1270, "TAGS" at line 2272 — one Chinese copy having been deduplicated in the consolidation and the survivor translated. (The differ's alignment between the original's identical copies is ambiguous, so the census is stated as counts per file, not as a copy genealogy.) Control: `grep -c '标签' candidate.txt` = 0 — no Chinese form of the label remains anywhere in the delivered file. Closure holds.

**The stamp's STALE cause.** Commit b5cb724 (the usage-example sweep) changed exactly one line after the verdict bytes: candidate line 37, the Fossil prose link completed from `theme:fossil` to the `theme:fossil-jp` URL form (§7). No other post-verdict change exists in the file's history.

## Post-package repairs (REFRESH3-J)

The items above describe this package as built. The repairs recorded below postdate the package build; `candidate.txt` has been recopied from the current canonical `pages/theme:shancheng-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RFIX12 Item 1 — credit pointer, both carriers named (landing 7e0fce7, "pages: R-fix-12 flags repaired (shancheng, share-future)"; record FIX-RFIX12.md).** As built, the credit block (candidate L17) read `**著作権者:** 原語版ページの作成者に同じ（scp-wiki-cn の theme:shancheng）` and the license-box author parameter (candidate L2419) read `|author=scp-wiki-cn theme:shancheng の作者]]`; neither named anybody. The original names its author in prose (original L1194, `[[*user Odeo]]`) and so does the candidate's own translated prose (L36). The remedy (one line each): credit L17 → `**著作権者:** [[*user Odeo]]`, license-box parameter → `|author=Odeo]]`, the population's repaired single-author forms (plugsoft / past-oriented precedents).

**FIX-RFIX12 Item 2 — JP font loads and the delivered stacks reconciled (landing 7e0fce7; record FIX-RFIX12.md).** As built, the consolidated code block loads Noto Sans JP (candidate L147) and Noto Serif JP (L148) but no delivered stack named either face; the later `:root` copy at L1256–1260 (the `--header-title: 0` copy descended from the original's small `:root`) still named only the SC faces. The remedy aligns that `:root` to the loaded JP faces, verbatim in fossil-jp's form where applicable: L1258 `--header-font` → `'Poltawski Nowy', "Noto Sans JP", Garamond, …`; L1259 `--body-font` → `'Public Sans', 'Noto Sans JP', 'Noto Sans SC', Inter, …`; L1260 `--mono-font` → `'Sometype Mono', 'Noto Serif JP', 'Noto Serif SC', …`. The SC loads stand as the named fallbacks' loads; no other stack was touched. The FIX-RFIX12.md cascade note is recorded, not acted on: three `:root` setters exist (L213–215, L1258–1260, L1312–1314) and this lane aligned only the L1256 copy the batch report names; the last setter is left in the original's no-CJK form for the coordinator's judgement. Per FIX-RFIX12.md the T1 finding set is byte-identical before and after (shancheng error 8 / warn 1 / info 1, all eight errors the standing pseudo-ref family); class (i) 0 → 0.

## Change set outside the two diffed files

- `pages/theme:fossil-jp.txt` — the JP port of the base theme, whose stacks supply the comparison forms cited in §4 and whose delivery this candidate inlines (§3).
- The candidate's own attachments on the draft host: `chaotianmen.jpg`, `rock1.jpg` (the fossil header/footer images) and `odeo.png` (the exhibit image), re-hosted from the author's CN sandbox files.
- `pages/theme-decoration-sample-shancheng-jp.txt` — the render-check sample the T2/T3 rows measured.

## Multi-wave provenance

| Commit | Wave | Change to this candidate |
|---|---|---|
| 816deb1 | Stage 2 (CN13) integration | The port created: consolidation, translation, credit block |
| f1138e4 | FIX-P4 | Delivery repair; §9 fossil exception recorded |
| 1cdad38 | FIX4-SIGMA | Sigma-side repair |
| 6f6b349 | FIX5-TEXTA | Item 80 repaired (§Per-theme record) |
| b5cb724 | Usage-example sweep | Line 37 Fossil link form (the stamp's STALE cause) |

## Appendix: residue and heuristic resolution

Residue blocks: 0 of 10 — every block in this pair carries a specific signature, an unusually clean classification that reflects the port's shape (one consolidation move, one head insertion, one tail supplement). Heuristic blocks: likewise 0. The classification's work is done by its 10 specific blocks; block B5 (the consolidated stylesheet, 2,270 lines) is labeled RESTORATION by the classifier and adjudicated as consolidation in §3/§8, and its COMMENT-TEXT spans are the original's CSS comments carried and translated inside the moved block (R1 porter-visible mass, resolved by shape).
