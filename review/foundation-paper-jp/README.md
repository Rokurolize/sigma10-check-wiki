# Review package — theme:foundation-paper-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:foundation-paper-jp — origin KO, population #264 [GOSIGN2-LEDGER (b) row 264]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4f8327d1d5a15142aa958401e507b1356733f3a82a7fab3234d6b81eae7dfabb); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 2 warns / 0 infos (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 283; GOSIGN2-LEDGER (b) row 264]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample credit-modal (preview-form) + sidebar-not-opening + page-overflow 371–378px@320/375 + 780px@768; page runtime-hotlink site-theme chain only; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 263, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 263]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 264]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:foundation-paper-jp.txt sha256:4f8327d1d5a15142aa958401e507b1356733f3a82a7fab3234d6b81eae7dfabb; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 264) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×1 (class (iii)); the render row's sample-layer items (section 11); the `news` link (P11, sibling / batch-posting class, section 7). **One defect flag from this package:** the usage snippet names a page that is not this candidate (candidate L25; per-theme record below) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:foundation-paper | theme:foundation-paper-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 7 (first translation; the candidate's credit block records 初訳時参照リビジョン: 7) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-foundation-paper.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:foundation-paper-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 230 lines / 5,793 bytes | 245 lines / 6,693 bytes |
| SHA-256 | 3debbfa9c1822377d1a53c06f56c4919751ba5f696c3fdcbf1bfcb56fff649a4 | 44fd0ec716ab7b47e8d167a10f659e0ebeb7392970000bb92865971708e91c7b |

Wave history: the candidate was created by the Stage 2 KO4 integration (commit 56b9d1a, the LOCALIZE-S2-F wave's port); FIX-CREDIT-D (1869877) normalized its translator field; FIX4-IWA (8c62b7b) added the interwiki-style frame, and is the stamp's computed-against commit. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A newspaper theme for a branch news page: a Sigma-9-era port whose CSS travels inline in a `[[module CSS]]` inside the closing collapsible, with a long specimen body (headings, tabviews, quotes, tables) ahead of it. The port is correspondingly prose-heavy and CSS-light: it swaps the KO credit furniture (a right-aligned bare Rate and an unprefixed info pair) for the JP preview credit block, adds the interwiki-style frame, repoints the one component include and the one image the theme owns, and translates the specimen body entire — including the three CC attribution footnotes for the composite logo, whose handling the T4 lane called exemplary. Measured churn (diff.md, the generator's difflib count with autojunk off: +77/−71 in 30 change blocks). One defect flag arises, on the usage snippet's page name (per-theme record); the intro's `news` link is a ledger disposition, not a flag (section 7).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 30 change blocks — 22 specific (73.3%), 6 heuristic (20.0%), 2 residue (6.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 18 |
| TRANS-UNANCHORED | 7 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 2 |
| DRAFT-HOST | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| INFO-DEL | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 25 translation labels are the specimen body and intro prose, counted in section 6; the single EXHIBIT-RESTRUCTURE primary (B26) is an include repoint plus a tag localization inside the closing furniture, not a restructuring (section 8); the 2 residue blocks are one-line translations (B22, a quote specimen; B30, the header `content:` string), both written into section 6; the DELIVERY-HOST label inside B1 pairs the frame's `theme=` line against the head it replaced and is read as part of the frame addition (section 3). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:foundation-paper-jp; original theme:foundation-paper on scpko at reference revision 7; candidate `pages/theme:foundation-paper-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The theme is a dedicated skin for the branch's news page (original L9: the KO wiki's `news` page), and its CSS is delivered inline — a `[[module CSS show="true"]]` inside the closing collapsible (original L87–89), not from a code page; the candidate preserves that shape exactly (candidate L100–101).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the inline delivery shape decides how section 3's frame is read (the frame points at the page's own first code block, which is that module).
- **Verify:** The sources.tsv row for foundation-paper-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a right-aligned bare `[[module Rate]]` (original L2–4) plus an unprefixed branch-local `[[include info:start]]`/`info:end` pair (original L5–8) whose body carries the title and the author ([[*user Denevola]]). The candidate deletes both (block B1) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying the eight ruling-3 fields (title 財団紙テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 재단지 테마; 著作権者 Denevola; 作成年 2021; 初訳時参照リビジョン 7; the source link, section 7) — the 著作権者 field names the same author the original's info block names, so no one is dropped. The translator field took its ruling-3 form in FIX-CREDIT-D (1869877). The original's richer attribution prose survives outside the credit block: the intro's logo paragraph (candidate L20) carries all three of the original's CC footnotes translated (the logo by Denevola, CC BY-SA 3.0; the emblem by Aelanna, CC BY-SA 3.0; the newspaper icon by Vectorstall, CC BY 3.0), with the license deed links localized (deed.ko → deed.ja) — the handling LOCALIZE-ROWS row 263 calls exemplary. There is no T7 credit-module CSS on either side and no license box on either side.
- **Why:** P3/T1 (KB-09): the preview credit module is rate-bearing, so the bare Rate is deleted rather than duplicated, and the branch info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields and the translator credit form; the footnote attributions are TASL substance the port must not lose, and it does not.
- **Verify:** `grep -n 'module Rate\|include info:' candidate.txt` returns nothing; read candidate L8–17 against the eight fields and candidate L20 against original L10.
- **Disposition:** Standing (present from creation; the T4 row charges nothing against this section and praises its attribution handling).

### 2. Includes and components

- **What:** Two repoints and one flag. (1) The closing furniture's component include repoints from `:scpko:component:toggle-sidebar` to `:scp-jp:component:toggle-sidebar` (original L88 → candidate L100, inside block B26). (2) The frame and credit includes (sections 3 and 1). (3) The usage snippet (block B3, candidate L25): the original's `@@[[include :scpko:theme:foundation-paper]]@@` becomes `@@[[include :scp-jp:theme:foundation-paper]]@@` — the wiki prefix is repointed but the page name keeps the original's form, without the `-jp` suffix that this candidate's own name, its file name, and its frame `theme=` URL all carry. This is flagged, not edited (per-theme record below). Every other named include in the candidate is `:scp-jp:`.
- **Why:** P1 (KB-15): includes name the JP component or theme page that actually exists. The toggle-sidebar repoint follows it; the usage snippet, on the bytes, does not name this candidate.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the toggle-sidebar, and candidate L25.
- **Disposition:** Repoints applied; the usage snippet is the package's defect flag (per-theme record).

### 3. Delivery and code loading

- **What:** Neither side loads CSS from a code page: the theme's CSS is the inline `[[module CSS show="true"]]` inside the closing collapsible on both sides (original L89, candidate L101), and its text is carried over apart from the changes in sections 4–6 and 10. **Frame paragraph (the M-frame addition):** the original carried no interwiki-style frame (LOCALIZE-ROWS row 263, 型 6, its one display-affecting T4 charge); the candidate adds one at candidate L1–4 with `priority=1` and `theme=` naming its own `local--code/theme%3Afoundation-paper-jp/1` on the draft host — the single-layer own-code form, whose /1 index is the page's own first code block, the inline module above. The ledger records the outcome as P6 FIXED (frame waves; checker-verified); the frame arrived in FIX4-IWA (commit 8c62b7b, "missing interwiki frames added to 31 themes (KB-07a)").
- **Why:** P6/T3 (KB-07): the frame is the environment's standard delivery supplement; here it wraps an inline-delivered theme rather than replacing its delivery, which is why the module survives untouched beside it. KB-41 covers the frame URL's draft-host form (class (iii), rewritten to the production host at posting).
- **Verify:** Read candidate L1–4 and L100–101; `grep -n 'scpko.wdfiles' candidate.txt` returns nothing.
- **Disposition:** FIXED (P6); the draft-host frame URL is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts: none — neither side loads a webfont or names a text face; the theme inherits the site theme's fonts, and its single `font-family` line (`'FontAwesome'`, candidate L159, the icon stack) is carried byte-identical from the original. Assets: the theme owns exactly one image, the header logo (logo.min.svg), repointed from `scpko.wdfiles.com/local--files/theme%3Afoundation-paper/` to the candidate's own draft-host file area (block B28, candidate L113), file name unchanged. The intro's two outbound image-source links (Wikimedia Commons, The Noun Project) are attribution links, not assets; they are section 7.
- **Why:** P7 is checked and absent (no stack names a face, so no KB-16 gap can arise); P5/KB-17 for the one asset's re-hosting to the JP side.
- **Verify:** `grep -n 'font-family\|googleapis\|font-face' candidate.txt` — the FontAwesome line only; `grep -n 'wdfiles' candidate.txt` against the asset above.
- **Disposition:** Asset repoint applied; its draft-host form is DISPOSITIONED (class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** No header variables are overridden on either side (no `--header-title` / `--header-subtitle` / `--logo-image`); the theme's header identity is carried by CSS instead: the logo background (section 4) and the two `content:` strings that replace the site title and subtitle visually (original L107, L116 → candidate L122, L131), translated in section 6. The `#header h1 a` / `h2 span` visibility pair that makes those strings the header is byte-identical on both sides. No sidebar or topbar rule changes: the toggle-sidebar include is repointed (section 2) and the yui-navset rules are carried unchanged. The render row's sidebar-not-opening reading is a sample-layer item, recorded in section 11, not a change in this file.
- **Why:** P8/P9 are checked and absent as edits: the furniture the theme declares is string content, which is P10/KB-18 and is counted there.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; read candidate L118–132 against original L103–117.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The specimen body and intro are translated throughout, in the classifier's counts: 18 TRANSLATION-ANCHORED and 7 TRANS-UNANCHORED primary blocks (B2, B4–B25, B27), plus the 2 residue blocks adjudicated here. In groups: the intro prose (candidate L19–20, including the logo attribution paragraph of section 1); the usage prose (candidate L22–23, L28–29); the heading-level specimens and their collapsible labels (B6–B11: 見出し一覧, 見出しレベル2–6); the three tabviews' tab titles (B12–B20: タブビュー, 空のタブ); the quote, table, and rule specimens (B21–B25); and the two reader-visible CSS strings (B29: `content: 'SCP 뉴스'` → `'SCPニュース'`, a spacing localization; B30, residue: `content: '신속, 정확, 신뢰'` → `'迅速、正確、信頼'`, translated with Japanese punctuation forms). The one-line residue block B22 (`> 글자` → `> 文字`, a quote specimen) belongs to the same group. In-CSS comment text (R1): the module's banner comment is carried in English on both sides; its two added lines are porter annotations (section 10). Korean survives in the candidate only as quotation: the credit block's original-title field (candidate L12). R5 glyph-form conversion: none — the source is Korean.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including the `content:` pair, which *are* this theme's header title and subtitle). The unanchored and residue groups are where a silent deletion would hide, which is why each was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's body sections in order; a Hangul scan of candidate.txt returns only candidate L12.
- **Disposition:** Standing (the port itself); the ledger records the theme's P10 class as DISPOSITIONED (lane-recorded severity / specimen class), which is the specimen-body convention, not an open item.

### 7. Links

- **What:** Three link matters. (1) The intro's page link: the original's `[[[news|이달의 소식]]]` becomes `[[[news|今月のニュース]]]` (candidate L19) — the same relative page name, its label translated. The T4 row charged this link as display-effective (型 11/型 10: the `news` page 404s on scp-jp today); the ledger dispositions it P11 DISPOSITIONED (sibling / batch-posting class): the theme exists to skin the JP news page, which is a sibling deliverable of the same posting batch, so the link's target arrives with the batch rather than being this candidate's defect. (2) The attribution links (candidate L20): the Commons emblem file and the Noun Project icon page, kept on their serving original hosts, with the CC deed links localized to their Japanese deed forms (section 1). (3) The credit block's source link (candidate L16) names `https://scpko.wikidot.com/theme:foundation-paper` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises.
- **Why:** P11 under the dead-reference evidence standard: a link is a defect when its target serves nowhere; the `news` target is a named sibling posting, the attribution targets serve today, and the source link names the recorded host.
- **Verify:** Compare candidate L16's host against the sources.tsv row's original_url host (scpko.wikidot.com) — identical; read candidate L19–20 against original L9–10.
- **Disposition:** Standing; the `news` link is DISPOSITIONED (P11, sibling / batch-posting).

### 8. Structure

- **What:** The localize.md closing rule holds. The candidate preserves the original's whole shape: gate, credit zone, intro, usage, specimen body, and the closing collapsible with its component include and inline CSS module, in the original's order; the JP additions (frame, credit block) sit at the head, and no inherited CSS rule was edited in place apart from the asset line (section 4) and the two `content:` strings (section 6). The classifier's one EXHIBIT-RESTRUCTURE primary (B26) adjudicates to furniture, not restructuring: its spans are the hidden div's tag gate (`[[iftags -테마]]` → `[[iftags -テーマ]]`, the negative-tag half of P2) and the toggle-sidebar repoint of section 2 — the standing false-fire shape for this label (include repoints inside exhibit regions). An exhibit census confirms the shape: the heading collapsible, all three tabviews, the quote and table specimens, and the code collapsible are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise for this theme.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[collapsible\|\[\[module\|\[\[include' original.txt candidate.txt` — the sequences correspond one to one, with the head furniture the only additions.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 30 blocks, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, inside the CSS module's banner comment (block B27, candidate L110–111): two lines appended to the original's English banner — "SCP-JP版: 2026年に日本語版へ移植。作成者: Denevola（韓国支部）。翻訳: SCP-JP。" The banner itself ("Foundation Paper Theme / [2021 Wikidot Theme] / Created by Denevola. / Based on Sigma-9 Theme created by Aelanna and Dr Devan.") is the original's, carried unchanged above them. The annotation is porter-visible only; the TASL record proper is the credit block (section 1), whose translator field carries the ruling-3 form (AI) — the banner line's collective wording is the porter's provenance note, not a second credit record, and the two are recorded here so a reviewer is not left to reconcile them unaided. The candidate has no `[!-- --]` notes; the skeleton's per-section text for this section is superseded by this census.
- **Why:** R2: porter-added text is part of the change record and is enumerated wherever it rides, including inside a carried comment block.
- **Verify:** Read candidate L102–111 against original L91–96.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's one pseudo-ref error: class (iii), draft-form — the frame's `theme=` URL (section 3); the posting procedure rewrites it to the production host. (2) The render row's items (RENDER-ROWS-2, RENDER-S2-H (KO4)): the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5), the sample's sidebar-not-opening reading, the page-overflow readings (371–378px at 320/375, 780px at 768), and the page's runtime-hotlink site-theme chain (KB-40) — sample and environment layer, recorded as not charged to the candidate. (3) The `news` link: DISPOSITIONED (P11, sibling / batch-posting class; section 7). (4) The P10 specimen class: DISPOSITIONED (lane-recorded severity / specimen class; section 6). The usage-snippet flag (per-theme record) is not in this list: no ledger line dispositions it, which is why it is flagged rather than dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–4 as stated).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 283): exit 1, 1 error / 2 warns / 0 infos; the one error is pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO4)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 263): FINDINGS jointly, display-affecting findings 1 — the row's charges are 型 6, the absent interwiki-style frame (since FIXED by FIX4-IWA), and the 型 11/型 10 `news` link (dispositioned, section 7); the same row records the CC attribution handling as exemplary. The ledger §(c3) line records the outcomes: P6 FIXED (frame waves, checker-verified), P10 DISPOSITIONED, P11 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +77/−71 in 30 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:foundation-paper-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 264; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports 2 residue blocks; both were adjudicated against the bytes and are written into section 6:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B22 | 73-73 → 85-85 (body → body) | no signature | One-line quote specimen translation (`> 글자` → `> 文字`); section 6 |
| B30 | 116-116 → 131-131 (body → body) | no signature | The header subtitle `content:` string translated (`'신속, 정확, 신뢰'` → `'迅速、正確、信頼'`); sections 5–6 |

The 6 heuristic blocks are the one-line prose and specimen translations counted in section 6 (B5, B20, B21, B23, B24) and the banner-comment annotation block (B27, section 10).

## Per-theme record — the usage snippet names a different page (defect flag)

The usage snippet is the one line a reader copies to adopt the theme, and on the bytes it names the wrong page. Candidate L25 reads `> @@[[include :scp-jp:theme:foundation-paper]]@@`. This candidate is theme:foundation-paper-jp: its canonical file is `pages/theme:foundation-paper-jp.txt` and its frame `theme=` URL names `theme%3Afoundation-paper-jp`, and the batch's other candidates with usage snippets name their own `-jp` pages in theirs. Probes run for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:foundation-paper` returns 404 and `https://scp-jp.wikidot.com/theme:foundation-paper-jp` returns 404 — neither page is posted yet, so the probe cannot settle intent; what the bytes settle is that the snippet is inconsistent with the candidate's own identity, and if the candidate posts under its canonical name the snippet will point at a page that does not exist. No ledger line dispositions the snippet's name (the T1 pseudo-ref class (iii) covers references to the not-yet-posted page itself, which this is not, on the bytes). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if the coordinator confirms it, is the one-line repoint of candidate L25 to the candidate's own page name, after which this package's diff.md and stamp need no change beyond regeneration (the candidate file's hash in the stamp would change).

## Per-theme record


### Post-package repairs (REFRESH3-D)

Recopy brought one post-package repair in: built at `6e17ffa` before 722ceb5, the candidate still carried the dead frame parameter; the recopy removed exactly that line (6,696 → 6,610 bytes).

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Afoundation-paper-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- **Original evidence:** no original frame, no `theme=`, no local--code (KO integration). No other repair touches this file.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-foundation-paper-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 재단지 테마
- **Author:** Denevola
- **Source:** https://scpko.wikidot.com/theme:foundation-paper — revision 7
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
