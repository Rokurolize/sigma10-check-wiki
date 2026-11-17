# Review package — theme:horn-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:horn-jp — origin CN, population #197 [GOSIGN2-LEDGER (b) row 197]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 831d08df26cc3876a3b7b313a8e30a0e16f1e9a41ed4393aa711ede519d431fe); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 2 infos (hotlink×4, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 227; GOSIGN2-LEDGER (b) row 197]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample hidden-* cluster confined to webkit-1366, whose only hotlink host is http.cat = transient 503 capture, not a result; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 196, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 196]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 197]
- Computed against: canonical commit 1c96ee4f6dbe58243d8c4ba0136a4a4dde806972; candidate file pages/theme:horn-jp.txt sha256:831d08df26cc3876a3b7b313a8e30a0e16f1e9a41ed4393aa711ede519d431fe; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 197) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×4 + pseudo-ref ×1 (classes (ii)/(iii), section 11); the render row's items (KB-40 / KB-44, section 11); the T4 items P5 and P11 (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:horn | theme:horn-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 5 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-horn.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:horn-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 514 lines / 12,301 bytes | 533 lines / 14,297 bytes |
| SHA-256 | f90b2558bc3f575a346bb92556d8b0b396267c18a3618ab7453ac0e66d552ab4 | fff7bbdcccc780f9384df18b8688b4eb1c78f9b278b8fdfc30caae3d172d2d71 |

Wave history: the candidate was created by the Stage 2 CN8 integration (commit e469417, the LOCALIZE-S2-F wave's port) and touched once since, by 1869877 (FIX-CREDIT-D, translator-attribution normalization). No production JP counterpart exists, so the R4 adoption question does not arise.

## Summary

A CN Sigma-9-family port （号声， "horn sound") whose credit furniture is part of its specimen: the page demonstrates its own rate module and credit module under labeled headings, so the port keeps the labeled Rate in place, replaces the CN credit-module trio with the JP preview credit block, and translates the labels. The rest is the standard set, completely applied: own-code delivery repointed to the draft host, the Chinese font load (Noto Serif SC, with a double-escaped ampersand in its URL) replaced by the JP faces (Noto Serif JP + Noto Sans JP, clean URL), the license box repointed to the JP component with its entries translated, the specimen body translated with its simplified-Chinese glyph forms converted to Japanese forms, and the usage include repointed to the candidate's own name. Two recorded items stand by disposition: the four asset references that remain on the author's CN sandbox host (KB-58) and one red link to the author's setting page (the sibling/batch-posting class). Measured churn (diff.md, the generator's difflib count with autojunk off: +160/−146, 306 changed lines in 77 change blocks / 12 diff hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 77 change blocks — 35 specific (45.5%), 42 heuristic (54.5%), 0 residue, 0 skipped. The heuristic mass is the specimen body's translation and its nine CSS comment translations, resolved by shape in the appendix. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| ASSET-REHOST | 1 |
| COMMENT-TEXT | 9 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 3 |
| GLYPH-FORM | 4 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 4 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 45 |
| TRANSLATION-ANCHORED | 25 |

Adjudication for this README (every specific block was read against the bytes): the three EXHIBIT-RESTRUCTURE primaries (B17, B75, B77) are an asset-line scheme upgrade and the two license-box include repoints, not restructures (section 8). The four GLYPH-FORM blocks are named one by one in section 6, because R5 conversions are exactly the changes a reviewer cannot afford to have summarized away. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:horn-jp; original theme:horn on scp-wiki-cn at reference revision 5; candidate `pages/theme:horn-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard). The candidate's head keeps the original's shape: the own-code import module (candidate L1–3), the interwiki frame (L5–8), then the localized gate `[[iftags +テーマ]]` (L10) over the credit furniture and body. There is no base-theme include in this theme on either side; its Sigma-9 base arrives with the usage pattern the page demonstrates.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for horn-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** This theme's credit furniture is demonstrative, and the candidate preserves the demonstration. The original opens with a labeled bare Rate (`**评分：**` over `[[>]]` / `[[module Rate]]` / `[[/>]]`, original L7–10), an empty labeled wrapper for the credit module (`**评分模块与著作信息模块：**`, original L12–14 — empty in the original too; it is the heading under which the credit module stands), and the CN credit trio (`:scp-wiki-cn:credit:start` / `:more` / `:end` with 页面信息/更多页面信息， original L16–21). The candidate translates both labels （評価モジュール：, candidate L12; 評価モジュールとクレジットモジュール：, L17), keeps the Rate module and the empty wrapper exactly as the original had them, and replaces the CN trio with the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L20–31) carrying the ruling-3 fields in this wave's variant order （タイトル 号声テーマ; 原題 号声 版式; 著者 [[*user hoah2333]]; 翻訳責任者 AI; 翻訳年 2026; 著作権者 hoah2333 & nmscxj; 作成年 2021; 初訳時参照リビジョン 5; 元記事リンク to scp-wiki-cn.wikidot.com/theme:horn) plus a font-attribution line （使用フォント: Noto Serif JP、Noto Sans JP（Google Fonts、SIL OFL 1.1）) that records the section 4 substitution inside the credit record itself. The license box stands at the tail inside the hidden conditional div (candidate L523–532): its includes are repointed to `:scp-jp:component:license-box`/`license-box-end` (B75, B77, dropping the original's `|lang=CN` parameter, keeping `|author=hoah2333 & nmscxj`), and its entries are translated （ファイル名/画像の帰属/ライセンス/ソースリンク） with the file names kept in their original Chinese forms, because those are the files' actual names on the host (section 4); the license link is upgraded to https. T7 credit-module CSS: 2 matching lines on each side, inherited unchanged.
- **Why:** P3/T1 with a specimen caveat: KB-09's rule (the preview module replaces the bare Rate) applies to a page's working credit furniture; here the Rate is a labeled exhibit of the theme's own furniture, and deleting it would delete part of the specimen the theme exists to show. The swap that matters — CN credit trio to JP preview block — is applied in full. Ruling 3 fixes the fields; the font line is this candidate's own addition to the record, and a good one.
- **Verify:** Read candidate L11–31 against the description above and original L7–21; `grep -n 'credit:start' candidate.txt` shows only the preview pair.
- **Disposition:** Applied.

### 2. Includes and components

- **What:** The live include changes: the frame to `:scp-jp:component:interwiki-style` (candidate L5), the credit pair (section 1), the license pair (section 1), and the usage line's self-include — inside its blockquote, `> [[include :scp-wiki-cn:theme:horn]]` becomes `> [[include theme:horn-jp]]` (candidate L42, B10), the candidate naming itself in the bare form. One include keeps the original's bare form: the specimen's `[[include component:image-block` (candidate L67, B17), whose change is its asset's scheme upgrade (http → https), not a repoint; the other packages in this batch repointed that include, and the difference is recorded here rather than smoothed over — no campaign record charges it, and its asset is one of the dispositioned sandbox references (section 4). The candidate's remaining includes are the escaped usage forms of the same set.
- **Why:** P1 (KB-15) for the repoints that were made; the record distinguishes them from the one that was not, so the next sweep can decide the image-block form with full information.
- **Verify:** `grep -n '\[\[include' candidate.txt` against the list above.
- **Disposition:** Applied (repoints); the image-block form stands as recorded.

### 3. Delivery and code loading

- **What:** One delivery layer, the theme's own: the original imports its code from CN storage (`https://scp-wiki-cn.wikidot.com/local--code/theme%3Ahorn/1`, original L2) and names the same URL through its interwiki frame at priority=3 (original L5–8). The candidate repoints both to its own code on the draft host (candidate L2, B1; frame at candidate L5–8), keeping the frame's priority. The delivered body is the candidate's own `[[code]]` block (the /1 index), as in the original. One exhibit line belongs to the base's delivery rather than the theme's: the usage section's raw CSS exhibit shows the base's logo rule, and its asset URL is repointed from the CN tech mirror (cdn.jsdelivr.net/gh/scp-cn-tech/sigma9) to the JP BHL files path (candidate L49, B12, ASSET-REHOST) — the exhibit now shows the delivery a JP user actually gets.
- **Why:** P6/T3: the own layer must name the candidate's own code, and on the draft wiki that is the draft-host form (KB-41, class (iii)).
- **Verify:** `grep -n 'local--code' candidate.txt` — the two lines above, both draft-host.
- **Disposition:** DISPOSITIONED (class (iii) draft-wiki form).

### 4. Fonts and assets

- **What:** Fonts (P7): the original loads its Chinese faces from Google Fonts — Noto Serif SC at weights 500 (original L178), its URL carrying a double-escaped `&amp;amp;`. The candidate substitutes the JP faces at the same station: `family=Noto+Serif+JP:wght@500&family=Noto+Sans+JP…` with a clean ampersand (candidate L198, B63) — the SC→JP face substitution and the URL-grammar repair in one line, and the credit block records the substitution (section 1). Assets: four references stay on the author's CN sandbox host (scpsandboxcn, in its wikidot.com and wdfiles.com forms): the specimen image in the image-block exhibit (candidate L67), the logo background (candidate L202), and the two header backgrounds (candidate L225). These are the T1 row's four hotlink errors and the T4 row's pattern-5 items (its L67/L202/L225, the same lines in the row's numbering). One scheme upgrade stands inside the class: the specimen image's URL is https in the candidate where the original's was http (B17).
- **Why:** P7/T5 for the face substitution (a Chinese display face is not a fallback for Japanese text; the JP faces are the port). P5/KB-58 for the assets: sandbox-host hosting is the deferred state — re-upload is barred by owner order, and posting is where the hosting question is settled.
- **Verify:** `grep -n '@import' candidate.txt` — the delivery import of section 3 plus the font load above. `grep -cn 'scpsandboxcn' candidate.txt` — the four asset lines (one line carries two URLs).
- **Disposition:** DISPOSITIONED (assets, class (ii) / KB-58; section 11); the font substitution is applied.

### 5. Header, sidebar, and site furniture

- **What:** This theme sets no `--header-title`/`--header-subtitle`/`--logo-image` variables on either side (grep returns 0/0). Its masthead text lives in two CSS content strings inside the usage section's raw exhibits, and both are translated with glyph conversion (candidate L53 and L57, B13/B14): the foundation name `SCP基金会` becomes `SCP財団`, and the motto `控制 收容 保护` becomes `確保 収容 保護` — the strings a JP site running this theme would actually render. The hidden conditional div at the tail localizes its gate with the rest of the page (`[[iftags -版式]]` → `[[iftags -テーマ]]`, candidate L521, B74). Sidebar and topbar rules are inherited unmodified.
- **Why:** P9/T6 is the furniture class; content strings are reader-visible text (KB-18), and here they are the theme's rendered masthead, so they are translated, not dispositioned.
- **Verify:** `grep -n 'content: "##' candidate.txt` — the two strings above.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The specimen body is translated in full: the descriptive prose (candidate L34–40), the usage prose, the heading specimens (レベル2見出し through レベル6, L82–90), the tab specimens (L96–166, including the very long empty-tab name, translated entire at L162), the blockquote and table specimens (L182–184), and the code sections (L186–188). The R5 glyph-form conversions are named individually, because they are the changes a summary would hide: (1) `SCP基金会` → `SCP財団` (B13, a content string, section 5); (2) `控制 收容 保护` → `確保 収容 保護` (B14 — 収容 and 保護 are the Japanese glyph forms of the simplified originals, and 控制 becomes the JP foundation's own word 確保）; (3) the section heading `示例` → `例` (B16, candidate L65); (4) the image caption's glyph forms inside B17 (candidate L67). The 45 TRANS-UNANCHORED label occurrences and the 9 COMMENT-TEXT blocks (CSS comment translations) are the remaining mass, resolved by shape in the appendix. Chinese survives as live text in the license entries' file names (section 1 — the files' actual names), the credit block's 原題 field (号声 版式, the original's title as a title), and the sandbox URLs' encoded file names — each a name or a citation, none an untranslated instruction or label.
- **Why:** P10, KB-18, and R5: simplified-Chinese glyph forms in reader-visible Japanese text are converted to their Japanese forms; names and citations are not text in that sense and stand.
- **Verify:** diff.md's body sections in order; `grep -n '基金会\|示例' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself); the retained Chinese is itemized above, each item with its ground.

### 7. Links

- **What:** The candidate's live outbound links are the credit block's source link (candidate L30), naming scp-wiki-cn.wikidot.com/theme:horn, the original's recorded host in sources.tsv — the serving form, not a defect — and one item that is charged and dispositioned: the prose link `[[[caromati|カルマティ（Caromati）]]]` (candidate L36), naming the author's setting hub page. No page by that name exists on SCP-JP, so the link renders red; the original's link named the same page on the CN side, where the setting lives. The T4 row records it as its pattern-11 item, and the ledger dispositions it in the sibling/batch-posting class: the setting's own pages are a sibling batch, and the link resolves when that batch posts. The T4 row's own assessment is that this theme could reach PASS grade by localizing the direct links and handling this link — the ledger's disposition is the handling it received.
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve and no disposition covers it; here the target's absence is a posting-order fact with a named class, not a port error.
- **Verify:** `grep -n 'caromati' candidate.txt` — candidate L36, as above.
- **Disposition:** DISPOSITIONED (P11, sibling/batch-posting class; GOSIGN2-LEDGER §(c3) line for this theme).

### 8. Structure

- **What:** No structural change. The classifier's three EXHIBIT-RESTRUCTURE primaries do not survive contact with the bytes: B17 is the image-block asset's scheme upgrade, and B75/B77 are the license box's include repoints — no exhibit added, removed, or reordered. The exhibit census (image block, headings, tabs, blockquotes, table, code) stands in the original's order on both sides. The R3 question (a silent structural deletion) does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a repoint share a diff shape; here the census, not the label, decides.
- **Verify:** Compare the exhibit sequence via `grep -n 'image-block\|見出し\|タブ' original.txt candidate.txt` and the three blocks in diff.md.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** None as a class: the classifier finds no WS-ONLY block, no re-indentation, and no line-ending conversion (0, 0, 0), and there are no residue blocks in this package at all. The section stands so the absence is on record.
- **Why:** Formatting churn is disclosed as its own class (R7); a clean zero is a finding, not a gap.
- **Verify:** classification.json's formatting counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None in the banner sense: this candidate carries no `Ported for SCP-JP` banner and no `[JP]` markers. Its one annotation-class element is functional, the credit block's 使用フォント line (section 1), which records the font substitution where a porter would look for it. No translator-note comments stand in the body.
- **Why:** R2: annotations are recorded where they exist, and their absence is recorded where they do not.
- **Verify:** `grep -n 'Ported for\|\[JP\]\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items. (1) T1's four hotlink errors: class (ii) — the sandbox-host asset lines of section 4, posting-time hosting state (KB-58); the ledger's §(c1) hotlink line dispositions the class. (2) T1's one pseudo-ref error: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3). (3) The render row's two items: the page's runtime-hotlink site-theme chain (KB-40, environment-layer, not charged) and the sample's WebKit 1366px hidden cluster, whose recorded cause is an http.cat transient 503 (KB-44, a transient third-party response, not a theme defect). (4) T4's P5 and P11 items: P5 (the sandbox direct links) DISPOSITIONED, class (ii) / KB-58, and P11 (the caromati red link) DISPOSITIONED in the sibling/batch-posting class, both per the ledger's §(c3) line.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer and transient lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all four items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 227): exit 1, 5 errors / 1 warn / 2 infos (hotlink×4, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-F (CN8)): FINDINGS, the two items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 196): FINDINGS jointly, display-affecting count 2 (the sandbox links; the red link), with the row's §3 structural checks recorded 8/8 ✓ and its credit preview sound; the ledger's §(c3) line dispositions P5 and P11 for this theme. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +160/−146 in 77 change blocks / 12 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:horn-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 197; go-sign, COMPLETION-REPORT §10).

## Appendix — heuristic and residue mass, resolved by shape

Class M treatment: the 42 heuristic blocks are not listed one by one; they fall into the shapes below, each verified against the bytes at the cited ranges. There are no residue blocks in this package.

| Shape | Blocks | Where | Resolution |
|---|---|---|---|
| Specimen sentence translation (unanchored) | The TRANS-UNANCHORED body mass (45 label occurrences across heuristic and mixed blocks) | candidate L34–200 | P10 translation (section 6) |
| CSS comment translation | COMMENT-TEXT ×9 | the delivered CSS body | Expected heuristic mass; comments carry no behaviour |
| Glyph-form conversion inside translated lines | B13, B14, B16, B17 (specific-anchored, listed here for completeness) | candidate L53, L57, L65, L67 | R5 conversions, named in section 6 |

## Per-theme record

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:horn-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RATES — head-zone bare Rate removed (landing `1c96ee4f6dbe58243d8c4ba0136a4a4dde806972`, "pages: head-zone bare Rates removed in five themes", 2026-11-17; record `FIX-RATES.md`).** +0/−5. The five-line head-zone bare-Rate block (right-floated `[[>]]` wrapper, `**評価モジュール:**`, `[[module Rate]]`, `[[/>]]`, trailing blank) is removed from inside the `[[iftags +テーマ]]` gate, directly above the rate-bearing preview credit block — head furniture beside the credit block, not a specimen. Residue kept, not edited: the remaining combined heading `**評価モジュールとクレジットモジュール:**` now heads the credit block alone (a wording call for the coordinator). Checker 5/1/2 → 5/1/1 (the `double-rate` info clears); every other finding unchanged in kind and count; class (i) 0.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-horn-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments and no inbound-link repairs in other candidates for this theme; the caromati link's resolution depends on a sibling batch's posting, which is a campaign scheduling fact, not a change in another file.
