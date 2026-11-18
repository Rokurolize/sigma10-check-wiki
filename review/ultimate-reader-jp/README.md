# Review package — theme:ultimate-reader-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ultimate-reader-jp — origin CN, population #241 [GOSIGN2-LEDGER (b) row 241]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 5d6fa9440ebc42f79a9709f257edbb60e1e67db570d37402ab0b52f4f328e651); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 206; GOSIGN2-LEDGER (b) row 241]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 778px at 320/375/768 (page) and 790px at 320/375/768 (sample) + runtime-hotlink site-theme chain; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN16)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN16)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 240, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 240]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 241]
- Computed against: canonical commit f4488f2d2948824238a2d06479f104f4aab0cf5d; candidate file pages/theme:ultimate-reader-jp.txt sha256:5d6fa9440ebc42f79a9709f257edbb60e1e67db570d37402ab0b52f4f328e651; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 241) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (ii), section 11); the render row's items (page and sample overflow at three widths, KB-33/KB-34; credit-modal preview form, KB-32; runtime chain, KB-40; chromium-only coverage); T4 display-affecting 1. **Three items are flagged by this package beyond the ledger's record: the credit field defers to "the original page's author" although the carried banner names him (Dr Hormress); a documentation code listing the original carries is dropped while the sentence promising it survives; and two JP fonts are imported but applied by no stack in the file (per-theme record).** The verdict stamp reads STALE because the candidate changed after the verdict in the usage-example sweep commit b5cb724 (section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ultimate-reader | theme:ultimate-reader-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 8 (first translation; the candidate's credit block records 初訳時参照リビジョン: 8) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-ultimate-reader.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ultimate-reader-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 999 lines / 24,892 bytes | 1,008 lines / 26,402 bytes |
| SHA-256 | 8610f62462cdda873f30b2eebcc4bf1e8082efba9f282f3c3f5cc67296a618b9 | fa7fee42f90f1868758a06f4e90aa4bd7fa2fb976990b8c7ad20d5a55a0db062 |

Wave history: the candidate was created by the Stage 2 CN16 integration (ddf2c89, the LOCALIZE-S2-E wave's port), then touched by FIX-CREDIT-D (1869877), by FIX4-SIGMA (1cdad38, which unified the sigma-plus include form across 8 themes), and by the usage-example sweep (b5cb724). Provenance note (sources.tsv, class K5a-i): the original is recorded as superseded upstream since the reference revision, with a follow-up diff artifact in the campaign record — that artifact's actual content is reported in section 12, because it does not say what the note implies.

## Summary

A reader theme built on Sigma+, whose port performs the batch's most consequential delivery conversion: the original's CSS is not a code block at all but a live `[[module CSS]]` of some 880 lines standing outside its documentation gate, and the candidate converts it into a delivered code block, externalizes delivery to a head module plus frame, and wraps the whole page in the gate. That conversion is done correctly — census, order, and content all check out — and the base include becomes the JP sigma-plus candidate. The package's findings are not in the conversion but around its edges, and all three are the kind a form-level checker cannot see: the credit field, instead of naming the author, defers to "the original page's author" — while the CSS banner carried verbatim in both files names Dr Hormress (and EstrellaYoshte for the Sigma+ base, Woedenaz for the logo); the documentation's `:root` defaults listing, a 28-line code exhibit in the original, is dropped, while the sentence that promises the listing survives in translation and now dangles; and the two JP fonts the candidate imports at its code head are applied by no font stack anywhere in the file — the variables still name the SC faces, and the documentation's promise of a Japanese Mincho body font in ultimate mode is one the CSS never keeps. Measured churn (the generator's difflib count, autojunk off): +91/−87, 178 changed lines in 30 change blocks / 2 diff hunks; a GNU-diff count gives 165 changed lines (+87/−78) — small numbers for a conversion this size, because the converted CSS is carried nearly verbatim. All three flags are set out with both sides' evidence in the per-theme record; this package changes nothing.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 30 change blocks — 24 specific (80.0%), 6 heuristic (20.0%), 0 residue (0%), 0 skipped — the batch's highest specific share, because a conversion's blocks carry delivery signatures. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 11 |
| TRANSLATION-ANCHORED | 9 |
| INCLUDE-REPOINT | 5 |
| COMPONENT-SWAP | 4 |
| DRAFT-HOST | 4 |
| IFTAGS | 4 |
| ESCAPED-INCLUDE | 3 |
| EXHIBIT-RESTRUCTURE | 3 |
| SELF-DELIVERY | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DUPIMPORT-DEL | 1 |
| GLYPH-FORM | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: six blocks — documentation translations, the sigma-plus usage region, and one import block (B27) whose DUPIMPORT-DEL reading adjudicates to the import relocation of section 3. There are no residue blocks (appendix). The three EXHIBIT-RESTRUCTURE primaries are the delivery conversion's own blocks and the usage-example reordering of section 8, adjudicated there against the census.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ultimate-reader-jp; original theme:ultimate-reader on scp-wiki-cn at reference revision 8; candidate `pages/theme:ultimate-reader-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard, with the K5a-i provenance note of the Provenance table). Two frame facts govern everything below: the theme is a layer over Sigma+ (its first line, both sides, is the base include), and the original's gate (`+版式`, original L4) wraps only its documentation — the live CSS module stands outside it. The candidate's gate (`+テーマ`) wraps the whole page, with delivery externalized to the head (section 3): the campaign's standard form, recorded here so the gate-scope difference is not misread as a structural loss.
- **Why:** Section 0 declares the route and the frame; the gate tag's localization is P2, the base swap is section 2.
- **Verify:** The sources.tsv row for ultimate-reader-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block (candidate L15–24) with the eight ruling-3 fields — but its 著作権者 field (candidate L20) reads `原語版ページの作成者に同じ（scp-wiki-cn の theme:ultimate-reader）` — "same as the original page's author" — a deferral, not a name. The original names its author plainly, in the CSS banner that *both files carry verbatim* (original L121–125 = candidate L121–125): "ULTIMATE READER Theme / by Dr Hormress / Based on Sigma+ by EstrellaYoshte / SCP Logo by Woedenaz". The candidate's own license box (candidate L996) repeats the deferral in its author parameter. The source-link field names the recorded host (scp-wiki-cn), so the host check passes and no probe was needed; the failure is only the author value. The base attribution (EstrellaYoshte, Woedenaz) survives in the banner and nowhere else.
- **Why:** P3/T1 and ruling 3 fix the form, and the ledger's class outcome records the credit fields FIXED — at form level (eight fields present, checker-verified). The standing credit check (field against the original's info block, license box, and banner) is a value check, and the value fails it: a field that defers to a page the reader cannot see, when the name is present in the same file, is the deferral form of the credit defect family. **Flagged** — per-theme record.
- **Verify:** Candidate L20 against candidate L121–125 (the banner is in the same file, twenty lines below the code block's head); the license box parameter is candidate L996.
- **Disposition:** Form FIXED (ledger §(c3) class outcomes: credit fields FIXED by the credit waves); **the author value is FLAGGED by this package** (per-theme record).

### 2. Includes and components

- **What:** The base include swaps at candidate L1: the original's `[[include :scp-wiki-cn:component:sigma-plus]]` becomes `[[include component:sigma-plus-jp]]` — the JP base candidate, in the bare form the FIX4-SIGMA wave unified across 8 themes (SIGMA-PLUS-JP). The credit pair (section 1) and the tail license-box components (LICENSE-BOX: `license-box-backend` with entries, `license-box-end`, candidate L996–1006 — the FIX4-LICENSE form, added; the original has no license box) complete the live set besides the delivery frame (section 3). COMPONENT-SWAP ×4 covers the base swap, the credit conversion, the license box, and the image-block example: the original's example names a third-party sandbox file (`ah-sandbox.wdfiles.com/…/ARED_2_i.svg`); the candidate's names the draft host's own `ared-2-i.svg`. The three escaped usage examples are reordered to match their prose (plain, then `ultimate-mode=*`, then `toggle-header=*`) — presentation, section 8.
- **Why:** P1 (KB-15) and KB-01's family for the base: a dependent theme imports the base's JP candidate delivery. The license box is the campaign's attribution instrument — which is why its deferring author parameter (section 1) matters.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the full live set.
- **Disposition:** Applied; no foreign include kept.

### 3. Delivery and code loading

- **What:** The conversion: the original's main CSS is a live `[[module CSS show="true"]]` (original L120, ~880 lines) whose content the page renders directly; the candidate turns that module's content into a `[[code type="css"]]` block (candidate L109–993) and delivers it the campaign's way — a head module importing the draft host's `local--code/theme%3Aultimate-reader-jp/1` (candidate L5) plus an interwiki-style frame naming the same /1. Census check: the candidate has exactly one `[[code]]` block, so the /1 address names the block that holds the CSS — correct. (The original also carried a small documentation code exhibit; that exhibit is the subject of flag 2, section 8 — it is not the delivered block on either side.) One classifier reading needs adjudication here: its DUPIMPORT-DEL block (B27, on original L126–128) sits on the original module's head imports — in the candidate, each of those faces is imported exactly once, at the code block's head (candidate L112–113). The block records the relocation's removal half; no import is lost and none is duplicated in the candidate.
- **Why:** P6/T3 (the frame) and the conversion class generally: a live module cannot be framed, so the module becomes a delivered block; the census is the check that the delivered block is the converted one.
- **Verify:** `grep -n 'local--code\|module CSS\|\[\[code' candidate.txt original.txt` — the module on one side, the block and its two delivery lines on the other.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the conversion itself is applied and verified.

### 4. Fonts and assets

- **What:** Imports (candidate L110–113, JPFONT-LOAD): Noto Sans JP and Noto Serif JP are *added* ahead of the original's Noto Serif SC and Noto Sans SC, all four from Google Fonts, under a porter comment (section 10). The application half fails: no font-family stack and no variable anywhere in the candidate names either JP face — `grep` finds "Noto Sans JP" and "Noto Serif JP" only at the import lines, the porter comment, and the license box's font entry (candidate L1003). The theme's own variables keep the SC faces: `--ur_title-font` "Noto Serif SC" (candidate L191), `--ur_body-font` "Noto Sans SC" (candidate L192). The documentation, meanwhile, promises that ultimate mode enables a Japanese Mincho body font — a selection the CSS never makes. **Flagged** — per-theme record: two faces are loaded on every page render and used by nothing, and the docs promise what the stacks do not do. Assets: `--sp_header-logo` (HEADERVAR) moves from the original's `https://sigma9.scpwikicn.com/cn/img/logo.png` to the draft host's own-folder `logo.png` — the KB-58 re-hosting class; the license box records the logo's license as not stated in the original, "投稿前に著者へ確認してください" (confirm with the author before posting), which is the honest entry.
- **Why:** P7 is a two-half class (load *and* apply); this candidate performs the first half only. The mirror-image failure (a stack naming an unloaded face) is a standing flag in this campaign; a load naming no stack is the same class from the other side, and the documentation promise makes it reader-visible.
- **Verify:** `grep -n 'Noto Sans JP\|Noto Serif JP' candidate.txt` — four loci, none of them a stack; `grep -n -- '--ur_body-font\|--ur_title-font' candidate.txt` for the SC values.
- **Disposition:** **FLAGGED** (the unapplied JP faces, per-theme record); the logo re-hosting is DISPOSITIONED (KB-58, class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header variables are the Sigma+ `--sp_` set, carried with the conversion; the two CN header defaults from the original's documentation listing (`--header-title` "SCP基金会", `--header-subtitle` "控制，收容，保护") are not carried as defaults — a JP port should not set a Chinese institute name as its header default, and their absence from the delivered CSS is defensible localization. What is not defensible is only the documentation side of that decision (flag 2, section 8). Two rendered `content:` strings remain in Chinese in the delivered CSS — "顶部导航" at candidate L955 and L982 — recorded here under the ledger's class line for this theme (header language falls under the ruling-2 family in the §(c3) class outcomes) and not flagged: they are the base furniture's labels, carried with the nearly verbatim conversion, and the ledger has dispositioned this theme's wording charges as a class. The hidden-notice div trick (`[[div [[iftags -版式]]…` in the original) is carried with its tag localized to `-テーマ` (candidate L102).
- **Why:** The furniture check distinguishes a localization decision (the CN defaults) from a documentation break (the dangling sentence) and from class-dispositioned wording (the content strings); only the middle one is flagged, in section 8.
- **Verify:** `grep -n '顶部导航' candidate.txt` — the two loci; the defaults listing question is section 8's.
- **Disposition:** Standing, with flag 2 recorded in section 8.

### 6. Text translation

- **What:** The documentation is translated throughout (9 TRANSLATION-ANCHORED blocks, 11 TRANS-UNANCHORED), including the license-box prose the candidate adds. The banner is *not* translated — carried verbatim (section 1), which is what makes the credit flag provable from the candidate alone. GLYPH-FORM ×1 is a glyph localization inside a sample (CN form to JP form). COMMENT-TEXT ×1 is the code head's comment region, where the porter annotation of section 10 also rides.
- **Why:** P10 and KB-18; the banner's survival is the attribution rule of section 1.
- **Verify:** diff.md's body sections in order.
- **Disposition:** Standing (the port itself), subject to flag 2's documentation point.

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. The documentation's expected-display image stays on scp-wiki-cn.wdfiles.com — original-state delivery, part of the asset class (ii) record. No live link in the candidate targets a page that does not exist on its named host.
- **Why:** P11 under the dead-reference evidence standard; nothing here meets it.
- **Verify:** `grep -n 'http' candidate.txt` enumerates every URL.
- **Disposition:** Standing; no link item is flagged for this theme.

### 8. Structure

- **What:** The localize.md closing rule holds, with the conversion's two structural facts stated plainly. First, the gate scope widens (docs-only in the original; whole page in the candidate) with delivery externalized — the standard form, section 0. Second, **the dropped documentation exhibit (flag 2):** the original carries a small code exhibit (original L33–60) listing the `:root` defaults — `--header-title` "SCP基金会", `--header-subtitle` "控制，收容，保护", `--sp_area-max-width: 45rem`, the `--ur_title-font`/`--ur_body-font` faces, and the six `--ur_` color variables with CN comments. No counterpart exists in the candidate. The values themselves survive in the delivered CSS (candidate L163 sets `--sp_area-max-width: 45rem`; candidate L191–196 set the `--ur_` variables), so the loss is the *documentation listing* — plus the two CN header defaults, whose absence section 5 adjudicates as defensible. The indefensible part is that the candidate's documentation still says, in translation, "**追加のCSS変数：**（以下は「アルティメットモード」を有効にしない場合のデフォルト値です）" (candidate L48) — "the following are the default values" — and nothing follows. A reader of the JP page is promised a listing that is not there. The three EXHIBIT-RESTRUCTURE primaries otherwise adjudicate to the conversion blocks and the usage-example reordering (section 2), against a census that is 1:1 for every other exhibit.
- **Why:** R3 and the silent-drop rule: content the original carries that the candidate drops is a flag with line ranges on both sides, however defensible parts of the drop are; the dangling sentence is what makes this one a documentation defect rather than an editorial choice.
- **Verify:** Original L33–60 against the candidate's documentation section (candidate L40–60 region): the promise sentence is present, the listing is absent.
- **Disposition:** **FLAGGED** (the dropped listing and its dangling sentence, per-theme record); the rest of the structure is standing.

### 9. Formatting only

- **What:** None. No WS-ONLY block and no pure re-indent block (reindent_blocks 0); the converted CSS is carried at the original's own indentation, which is part of why the churn count stays small for a conversion.
- **Why:** R7's ground for "none".
- **Verify:** classification.json's label counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation group, inside the code block at its head (candidate L116–119, riding in the comment-text region): a bilingual banner comment — "终极阅读器 / Ultimate Reader — Ported for SCP-JP (theme:ultimate-reader rev 8 on scp-wiki-cn). 原語版の CSS はページ内のモジュールにあり、Sigma-Plus を併用します。ロゴは添付にしました。" — recording the conversion (the original's CSS lived in an in-page module; Sigma+ is used alongside; the logo was made an attachment), followed by the font comment `/* 日本語フォント (JP localization) */` over the added imports. The skeleton's per-section text does not list them because they ride inside other labeled blocks; they are recorded here from the bytes, per the standing warning for exactly this shape.
- **Why:** R2: porter-added text is part of the change record, and this comment is the only in-file explanation of the conversion.
- **Verify:** Candidate L116–119.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The ledger items: (1) T1's three pseudo-ref errors, class (ii) (the draft-host delivery and asset lines). (2) The render row's items: overflow 778px on the page and 790px on the sample at 320/375/768 (KB-33/KB-34 family); the credit modal in preview form (KB-32 family); the runtime-hotlink chain (KB-40); the T3 re-run recorded no new finding; coverage is chromium-only, a stated limitation of the row. (3) T4 row 240: display-affecting 1 (hard 1 + conditional 1 + wording 1 charged in the row, not named individually there). (4) The ledger §(c3) class outcomes for the LOCALIZE-S2-E rows: header language under ruling 2, asset hosts class (ii), credit fields FIXED by the credit waves; the population-check row (LEDGER-POPULATION-CHECK row 20, cn-2) confirms the theme's population membership. **Flagged by this package:** the three items of the per-theme record (credit deferral; dropped defaults listing; unapplied JP fonts). None of the three is covered by a ledger disposition: the credit FIXED is form-level, T4's row does not name the listing or the fonts, and the render rows measure what renders, not what the documentation promises. The flags do not disturb the verdict; each is a small candidate repair for the coordinator to land with a package refresh.
- **Why:** A disposition is a decision with grounds; an undispositioned defect is reported as a flag, not absorbed into a neighboring FIXED.
- **Verify:** Each item names its deciding record above; the flags' evidence is the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); **the three per-theme items are FLAGGED**.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 206): exit 1, 3 errors / 1 warn / 1 info; all three errors pseudo-ref, class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-G, CN16): FINDINGS — the items of section 11(2), with chromium-only coverage stated in the row. (c) T4/T5 (LOCALIZE-ROWS row 240): FINDINGS, display-affecting 1. (d) The K5a-i follow-up artifact (`gosign2-lanes/lane-oc-gs-localize-s2-E/diff-ultimate-reader-from8.txt`, read for this package): a six-line record whose content is "scp-wiki-cn:theme:ultimate-reader rev8 → rev8 変更： なし" with an empty intervening-revision table — that is, the artifact records **no upstream change after the reference revision**, which sits awkwardly with sources.tsv's "original superseded upstream since the reference revision" wording. The bytes of the artifact are followed here (no superseding revision's content exists in the record to reconcile), and the wording tension is reported in the batch report as a prose-versus-record discrepancy for the coordinator to settle. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp reads STALE because the candidate changed after the verdict in the sweep commit b5cb724. Counts in this README are the generator's (difflib, autojunk off): +91/−87 in 30 change blocks / 2 diff hunks; the GNU-diff count is 165 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result — including, for (d), reading the artifact instead of its description.
- **Verify:** Re-run the checker on `pages/theme:ultimate-reader-jp.txt`; read the follow-up artifact at the path in (d).
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 241; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Flag 1 — the credit field defers where the banner names

Both sides, verbatim. Candidate credit field (candidate L20): `**著作権者:** 原語版ページの作成者に同じ（scp-wiki-cn の theme:ultimate-reader）`. The banner carried in both files (original L121–125 = candidate L121–125): "ULTIMATE READER Theme / by Dr Hormress / Based on Sigma+ by EstrellaYoshte / SCP Logo by Woedenaz". The license box's author parameter (candidate L996) defers in the same words. So the candidate contains the author's name — in its CSS banner — while its two attribution instruments (the credit field and the license box) both decline to state it. Recommended repair: name Dr Hormress in the field and the license box, with EstrellaYoshte (Sigma+ base) and Woedenaz (logo) carried as the banner carries them.

### Flag 2 — the dropped `:root` defaults listing, and the sentence that promises it

Original L33–60 is a documentation code exhibit listing the theme's `:root` defaults (28 lines: the two CN header strings, `--sp_area-max-width: 45rem`, `--ur_title-font`, `--ur_body-font`, and the `--ur_marble/concrete/redstone/basalt/bedrock/stone` colors with CN comments). The candidate has no counterpart block. The delivered CSS keeps the values (candidate L163, L191–196), so nothing functional is lost; the documentation is. The candidate's docs still carry the introducing sentence — "**追加のCSS変数：**（以下は「アルティメットモード」を有効にしない場合のデフォルト値です）" — after which the promised listing should stand and does not. Recommended repair: restore the listing from the delivered values (with the JP-appropriate header defaults question settled explicitly), or delete the sentence; the current state, a promise with nothing after it, is the one form that is wrong either way.

### Flag 3 — two JP fonts loaded, applied nowhere

Candidate L110–111 import Noto Sans JP and Noto Serif JP; the porter comment (candidate L119) labels them the JP localization's fonts; the license box (candidate L1003) lists them. But no stack or variable in the file names either face: `--ur_title-font` remains "Noto Serif SC" (candidate L191) and `--ur_body-font` remains "Noto Sans SC" (candidate L192), and a full-text search finds the JP faces only at the import, the comment, and the license entry. The documentation's statement that ultimate mode gives the body a Japanese Mincho face is therefore not true of the delivered CSS. Recommended repair: point the `--ur_` variables' fallbacks (or the ultimate-mode overrides) at the JP faces, or remove the imports and correct the documentation; as with flag 2, either settled state is defensible and the current one is not.

## Appendix — residue blocks

None: classification.json records zero residue-tier blocks for this pair (24 specific / 6 heuristic / 0 residue). The one heuristic block that is not a translation, B27 (original L126–128 → candidate L126, DUPIMPORT-DEL-labeled), is adjudicated in section 3 as the import relocation's removal half.

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:ultimate-reader-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-MP12 item 2 (a)(b)(c) — credit author, defaults listing, JP faces applied (landing `f4488f2d2948824238a2d06479f104f4aab0cf5d`, "pages: skipos delivered channel, the-other-side fonts and subtitle, M-pure-12 repairs", 2026-11-17; record `FIX-MP12.md`).** Three changes, +29/−4 by git numstat. (a) The credit deferral is resolved: L20 `**著作権者:** 原語版ページの作成者に同じ（scp-wiki-cn の theme:ultimate-reader）` → `**著作権者:** Dr Hormress`, and the license-box L1022 `|author=scp-wiki-cn theme:ultimate-reader の作者]]` → `|author=Dr Hormress]]`; the banner still credits EstrellaYoshte and Woedenaz. (b) The original's 28-line `:root` defaults listing, dropped as built while its introducing sentence survived at L48, is restored in the candidate's own `[[code type="css"]]` form immediately after that sentence (new L50 onward), with values from the delivered CSS and translated comments (本文の幅 / タイトルフォント / 本文フォント / テーマカラー：…); the original's two CN header defaults are deliberately not carried because the port sets none (package §5 adjudicates that absence defensible), leaving nine entries. (c) The JP faces the port imported but never applied are now applied: L216/L217 (and the restored listing at L55/L57) read `--ur_title-font: "Noto Serif JP", "Noto Serif SC", serif;` and `--ur_body-font: "Noto Sans JP", "Noto Sans SC", sans-serif;` — JP face first, SC fallback, mirroring the original's application of its SC faces. Checker 3/1/1 before and after; no new class (i). (FIX-MP12's acceptance summary quotes +31/−4 for this file; git numstat is +29/−4.)

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-ultimate-reader-jp.txt` is the decoration sample the render checks ran against (it includes this candidate), and its findings are the sample half of section 11(2). The follow-up diff artifact `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-ultimate-reader-from8.txt` (campaign record, not repo) is part of this theme's provenance record and is reported in section 12(d). There are no companion fragments in the repo and no inbound-link repairs in other candidates for this theme; the base candidate it depends on is `component:sigma-plus-jp`, shared with the other Sigma+ themes.

## License and attribution

- **Title:** 终极阅读器 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:ultimate-reader — revision 8
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
