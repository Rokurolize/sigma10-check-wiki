# Review package — theme:asagao-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:asagao-jp — origin CN, population #166 [GOSIGN2-LEDGER (b) row 166]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 236e6e2143b6d886b7931fffc520728b8514134ab266a3776b299b6daf26a47e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 13 errors / 0 warns / 1 info (hotlink×12, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 143; GOSIGN2-LEDGER (b) row 166]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-* cluster at chromium ≤768 (the chromium-768/375 captures carry an http.cat-only hotlink line = transient 503; the chromium-320 cluster is recorded as-is) + sidebar-unreachable at chromium ≤375; sample credit-modal (preview-form) + page-overflow 842px@768. [RENDER-ROWS-2 (RENDER-S2-E (CN1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 165, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 165]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 166]
- Computed against: canonical commit 780e0485dc89a41ccdf8671591c08bc887984edb; candidate file pages/theme:asagao-jp.txt sha256:236e6e2143b6d886b7931fffc520728b8514134ab266a3776b299b6daf26a47e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 166) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×12 (class (ii)) and pseudo-ref ×1 (class (iii)); the render row's hidden-cluster, sidebar, credit-modal, and overflow items (ledger (c2), section 11); T4's findings dispositioned per the ledger (c3) line (P3 FIXED; P5, class (ii) / KB-58) |
| Recorded tension | The ledger (c3) line dispositions P3 as FIXED (credit fields, checker-verified), and the eight fields are present; the candidate's bytes nonetheless drop the original credit block's third attribution — the base-work credit to maki hisane — entirely (per-theme record; the fields are complete, the attribution set is not) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:asagao | theme:asagao-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-asagao.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:asagao-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 1,496 lines / 45,524 bytes | 1,509 lines / 47,268 bytes |
| SHA-256 | 6ea403c4a2b0505ab0e5472d78c15d8d6281444f4083431319e1652e01096547 | 981e939a2116e8addf223993531bf9db77082b7b1d4cbb4038f69712533007f0 |

Wave history: the candidate was created by the Stage 2 CN1 integration (commit 4a2f4a5), then passed through the rework2-p5 wave (b89741d, the Sigma-9 base family), FIX-CREDIT-D (1869877, translator attribution normalization), and FIX4-MECH (a497307, duplicate @import removal under KB-65; the stamp's computed-against commit).

## Summary

The largest package in this batch: a roughly 1,500-line theme whose original is a self-contained magazine-layout system (the 朝颜文学报 / "Asagao Literary Journal" design) with an extensive usage documentation, delivered by an unusual mechanism — a ThemePreviewer module plus a shown CSS module importing the CN Sigma-9 base from jsdelivr. The candidate converts the delivery to the standard JP form (the CSS in a code block, self-imported by a tail module from the draft host, frame appended), translates the documentation line by line where it stands, rewrites the font supply from SC faces to JP faces, and keeps the theme's own CSS essentially intact under a porter banner. Measured churn is small against the file's size (diff.md, the generator's difflib count with autojunk off: +168/−160, 328 changed lines in 100 change blocks; a GNU-diff count of the same pair gives 255 changed lines — the difference is alignment choice across the line-by-line translation, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 100 change blocks — 37 specific (37.0%), 60 heuristic (60.0%), 3 residue (3.0%), 0 skipped. The heuristic share is the batch's highest and has a stated cause: the documentation translation proceeds one line at a time, and the anchored-translation heuristic needs multi-line context, so most prose lines land in the heuristic TRANS-UNANCHORED bucket; they were verified by their position in the documentation body and by spot pairs read against the mirror, and they are the translation of section 6, not sixty separate mechanisms. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 61 |
| TRANSLATION-ANCHORED | 18 |
| COLON-ENC | 6 |
| FONTLOAD-CJK-STACK | 4 |
| ESCAPED-INCLUDE | 2 |
| GLYPH-FORM | 2 |
| JPFONT-LOAD | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the three residue blocks resolve as the title-image scheme upgrade (B2, and its escaped twin inside the documentation, B68; section 7) and a blank/rule boundary at the code block's head (B83; section 9). The CSS-BODY heuristic blocks inside the code (B87, B95, B96 and their kin) are the font-stack rewrites and the `content:` strings of sections 4 and 6. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:asagao-jp; original theme:asagao on scp-wiki-cn at reference revision 10; candidate `pages/theme:asagao-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN1 wave (sources.tsv kind: standard; no production JP counterpart exists, so the R4 adoption question does not arise). The frame order follows the original: the localized gate first (candidate L1), then the theme's own title furniture; there is no head frame include — the interwiki frame sits at the file's tail, after the delivery module (candidate L1506–1509), where the delivery conversion put it.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for asagao-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's furniture is a `[[module rate]]` (original L10) and a `:scp-wiki-cn:credit:start`/`end` block (original L12–17) carrying THREE attributions: the layout author (Dr Hormress), the header-logo author (breaddddd), and a base-work credit — "based on the library codex 朝颜文学报 created by maki hisane" (original L16). The candidate deletes the Rate (BARE-RATE-DEL) and carries a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L11–21) with the eight ruling-3 fields (タイトル 《朝颜文学报特刊》：实验性文章布局及其使用方法 — the work's title kept in Chinese as its name; 翻訳責任者 AI; 翻訳年 2026; 原題 the same; 著作権者 "Dr Hormress（ヘッダーロゴ: breaddddd）" — the logo author folded into the author field; 作成年 2022; 初訳時参照リビジョン 10; the source link, candidate L20, naming `scp-wiki-cn.wikidot.com/theme:asagao` — the original's recorded host). The maki hisane base-work credit appears nowhere in the candidate: `grep -ci 'maki' candidate.txt` returns 0. The loss is the per-theme record below. License box (T4): neither side carries one.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form (KB-09) and ruling 3 fixes the eight fields — both satisfied. But a base-work attribution is license substance of the same kind the fields exist to protect; folding two of the original's three credits into one field and dropping the third is not what the field form sanctions, and this README records the drop rather than letting the field check imply completeness.
- **Verify:** Read original L12–17 against candidate L11–21; the grep above.
- **Disposition:** FIXED as to the eight fields (credit waves, checker-verified; the ledger (c3) outcomes); the dropped base-work attribution is recorded in the per-theme record as a surviving gap under that disposition, not as a re-opened verdict.

### 2. Includes and components

- **What:** The candidate's live includes are few: the credit pair (section 1), the documentation's `component:image-block` exhibits (kept, parameters translated; e.g. candidate L24–28), the collapsible/code furniture of the source exhibit, and the tail frame (section 3). Two ESCAPED-INCLUDE blocks are the documentation's escaped module exhibits (`@@[[module CSS]]@@`, candidate L241 and its twin), kept escaped — they are teaching text, not live includes. No include names a foreign-wiki target; the original's `:scp-wiki-cn:credit:*` pair is the only foreign include either side carries, and it is the replaced furniture of section 1.
- **Why:** P1 (KB-15): includes name JP counterparts or bare component names that resolve on JP. Escaped exhibits are R1 text, not delivery.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every target is `:scp-jp:` or a bare `component:` name.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original's delivery is the batch's most unusual: its CSS sits in a `[[module CSS show="true"]]` (original L290) headed by a `[[module ThemePreviewer]]` (original L289), the pair wrapped in a div gated by an inline `[[iftags -版式]]` (original L287), and its first import is the CN Sigma-9 base from jsdelivr (`cdn.jsdelivr.net/gh/scp-cn-tech/sigma9@cn/cn/sigma9_ch.min.css`, original L291). The candidate converts the whole mechanism: the ThemePreviewer and the shown module are gone; the theme's CSS (some 1,200 lines) sits in a `[[code type="css"]]` block (candidate L292–1497) under a porter banner (section 10); a tail `[[module css]]` (candidate L1503–1505) imports that block as `local--code/theme%3Aasagao-jp/1` from the draft host; the interwiki frame follows (candidate L1506–1509, priority 1). The jsdelivr Sigma-9 base import was removed and not replaced by an in-file base import: the candidate's CSS is the theme's own layer, and the composition's environment supplies the base — the same ground, and the same caveat, as theme:a-problematic-theme-jp's missing base (this batch): the bytes contain no base, and the ledger's determination for this Sigma-9-base-family theme (rework2-p5) is PASS. The one pseudo-ref error in T1 is the tail import's draft-host form.
- **Why:** P4 (own-code delivery served from JP hosts) and P6/T3 (the frame); the draft-host form is KB-41, class (iii), rewritten at posting. The foreign jsdelivr base could not stay (P1/P4: a base import must name the JP environment's own supply), and the conversion to code-block self-delivery is the campaign's standard JP form for a theme whose CSS was trapped inside a preview module.
- **Verify:** `grep -n 'jsdelivr\|ThemePreviewer\|local--code' candidate.txt` — the first two return nothing, the third returns the tail import and the frame line; compare original L287–291.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)); the base-supply ground is recorded above.

### 4. Fonts and assets

- **What:** Font supply is rewritten from CN faces to JP faces. Loads: the original imports Noto Serif JP (300–900), Noto Serif SC, and Noto Sans SC from Google Fonts (original L297–299); the candidate imports Noto Serif JP in two weight sets (candidate L294, added by the port at 400;700; candidate L301, the original's 300–900) and Noto Sans JP (candidate L302), and the SC loads are gone. Stacks: four FONTLOAD-CJK-STACK blocks and the CSS-BODY heuristics inside the code rewrite the stacks to the JP families (e.g. candidate L317, L395, L414, L660, L825: literal "Noto Sans JP" / "Noto Serif JP"). Two JPFONT-LOAD blocks name the added JP imports. FIX4-MECH (a497307) later removed duplicate @imports across the campaign under KB-65; the two Serif JP imports survive side by side because their weight sets differ. Assets: the theme's images serve from a personal sandbox host in both files — the title SVG (candidate L4, `ah-sandbox.wikidot.com/local--files/theme%3Ayasuharasuzu/asagao-title.svg`), the logo exhibit (candidate L25, the wdfiles twin), and the documentation's delivered images, eleven in the localize row's count (two live, nine in source), including one EN-host image (sh_expand.png). With the scheme upgrades of section 7 these are T1's twelve hotlink errors. Colons (KB-01): six COLON-ENC blocks encode page-name colons in the sandbox and delivery addresses.
- **Why:** P7/T5 (the CJK stack rewrite: SC faces out, JP faces in, loads and stacks consistent) with KB-16. P5 with KB-17/KB-58 for the sandbox-hosted images: the original's own delivery state, class (ii), re-hosted at posting; the ledger (c3) line dispositions this theme's P5 exactly so.
- **Verify:** `grep -n '@import\|font-family' candidate.txt` against the lines above; `grep -c 'ah-sandbox' candidate.txt`.
- **Disposition:** Font rewrite applied; the sandbox asset URLs DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The theme IS header furniture: its title block (candidate L3–8) is a custom div pair (the title SVG image and a meta-title line, 実験的記事レイアウトとその使用方法 — translated from 实验性文章布局及其使用方法）. The CSS carries the header/sidebar geometry variables (`--header-height`, `--sidebar-width` and kin, candidate L304 ff.), carried unchanged. No `--header-title` override exists on either side. The render row's sidebar item is section 11's.
- **Why:** P9/T6 names no override change here; the meta-title's translation is section 6's R1 work.
- **Verify:** Read candidate L3–8 and the `:root` head (candidate L304–316) against the original's in diff.md.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The documentation is translated in place, line by line: eighteen TRANSLATION-ANCHORED blocks and the sixty-one heuristic TRANS-UNANCHORED blocks are this one job, the usage prose, the examples, and the exhibit captions (e.g. the introduction at candidate L23, the divider example at candidate L32). Two GLYPH-FORM blocks are R5 conversions of retained strings. The `content:` strings split: `content: "朝顔文学報"` (candidate L394) takes the Japanese glyph form, while `content: "做风的君王"` (candidate L417) keeps its Chinese slogan — LOCALIZE-ROWS row 165's item (a), a reader-visible string in the original's language, recorded as found; its disposition ground is ruling 2's family (a slogan is design text), and the ledger determination is PASS. The CSS banner comment inside the code block (candidate L297–299) keeps the original's Chinese credit text (朝颜文学报版式 / [2022 Wikidot Theme] / 由Dr Hormress制作） — an R1 retention inside a comment, where the port's own banner (section 10) sits directly above it. The credit block's title fields likewise keep the work's Chinese title as its name (section 1).
- **Why:** P10 and KB-18 (reader-visible strings) for the translated mass; R5 for the glyph conversions. The retained slogan and banner are stated separately because "was this string translated?" has a per-string answer.
- **Verify:** A Han-character scan of candidate.txt returns the credit title fields, the L417 slogan, the code banner, and the R5-converted strings; the translated pairs are diff.md's body sections in order.
- **Disposition:** Standing (the port itself); the retained Chinese strings recorded with their grounds.

### 7. Links

- **What:** The two scheme upgrades: the title image address is `http:` in the original (original L3) and `https:` in the candidate (candidate L4), and the same upgrade fires inside the documentation's escaped copy of the title block (B68). No `http://` address remains in the candidate. The credit source link (candidate L20) names the original's recorded host (section 1). The documentation's prose links are carried as the original carries them; none targets a CN-wiki page.
- **Why:** P11 for the carried links. The upgrades are the T12 shape in reverse: an address the port touched takes its secure form.
- **Verify:** `grep -n 'http://' candidate.txt` returns nothing.
- **Disposition:** Standing; no dead link carried, no http residue.

### 8. Structure

- **What:** The closing rule holds, with one mechanism-level change that is delivery, not structure: the CSS's container changed from a shown module to a code block (section 3), at the same position in the file (after the documentation, before the closing gate). Everything else preserves order: gate, title furniture, credit, documentation with its exhibits, source exhibit, closing `[[/iftags]]` (candidate L1501), tail delivery. The exhibit census is one-to-one — the documentation's examples and the source exhibit are present on both sides in the same order; nothing was dropped, so the R3 question does not arise.
- **Why:** R3 exists to force this adjudication; the census decides for preservation, and the one container change is charged to section 3 where it belongs.
- **Verify:** Compare the section sequences of the two files (documentation headings and the code/source exhibits appear in the same order in diff.md).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** One boundary block (B83): a blank line and rule realign at the source exhibit's head where the delivery conversion landed (original L284–285 → candidate L285–286). No whitespace-only block pair and no re-indentation signature fires anywhere in the file (0 and 0) — remarkable in a 1,500-line port, and it means the translation preserved the code's indentation exactly.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The exhibit-head section of diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One, in comment form rather than the `[!-- --]` form: at the code block's head the port adds a banner comment, `/* ===== asagao 本体（原語版のインライン CSS） ===== */` (candidate L293), marking the CSS as the original-language inline body carried into the code block — the marker that tells a future editor the code below is the ported original, not JP-authored CSS. `grep -n '\[!--' candidate.txt` returns nothing; the annotation's form is a CSS comment because its position is inside the CSS.
- **Why:** R2: porter-added text is part of the change record; its form follows its position, and the check for the bracket form was run and is negative, stated with its ground.
- **Verify:** Read candidate L292–294.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's twelve hotlink errors: class (ii), posting-procedure — the sandbox-hosted title, logo, and documentation images (section 4); posting re-hosts them. Its one pseudo-ref error: the tail draft-host import (section 3), class (iii) (KB-41). (2) The render row's items, all DISPOSITIONED in the ledger (c2) register: the page hidden-* cluster at chromium ≤768 (its 768/375 captures carry an http.cat-only hotlink line, a transient Wikidot 503 capture, not a result — KB-44; the 320 cluster recorded as-is) and sidebar-unreachable at chromium ≤375 (single-combo machine line, not confirmed by the T3 walk — KB-47 family; where T3 checked the drawer it is recorded opening); the sample's credit-modal (preview form) and page-overflow 842px@768 (the recorded cross-cutting families: static credit replica fixed width, KB-33; preview chrome, KB-34; the per-theme figures match the campaign-wide shapes). (3) T4's findings (LOCALIZE-ROWS row 165): the credit item FIXED as to fields with the attribution gap recorded in section 1 and the per-theme record; the asset item (b) DISPOSITIONED (class (ii) / KB-58); the slogan item (a) is section 6's, grounded on ruling 2's family.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 1, 3, and 4.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 143): exit 1, 13 errors / 0 warns / 1 info; the errors are hotlink ×12 and pseudo-ref ×1, the standing classes of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E): FAIL/FAIL with FINDINGS, the items of section 11(2), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 165): FINDINGS jointly, display-affecting findings 4, dispositioned as in section 11(3) and the ledger §(c3) line (P3 FIXED; P5 DISPOSITIONED, class (ii) / KB-58). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +168/−160 in 100 change blocks; the GNU-diff count of the same pair is 255 changed lines, and the difference is alignment choice across the line-by-line translation, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:asagao-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 166; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The third attribution (what the field check cannot see)

The original's credit block names three parties: the layout's author, its logo's author, and the author of the work it is based on — maki hisane, whose "library codex" version of the 朝颜文学报 this theme reworks (original L16). The candidate's credit block carries the first two (the second folded into the author field) and the third nowhere: the name does not occur in the file. The credit waves' fix, and the checker that verified it, operate on the eight ruling-3 fields — presence, form, and the translator attribution — and by that measure the block is FIXED, as the ledger (c3) line records. A dropped base-work credit is outside that measure: no field exists for "based on," and the JP credit module's field set has no slot the porter was told to fill with it. This record exists so the loss is visible to a human reader rather than certified away: the repair, if the coordinator chooses it, is one line of attribution prose restored under the credit block, of the kind the candidate already carries for its images in other themes of this batch. The verdict is not re-opened here; the ledger's PASS stands on its own grounds, and this is the one place in the package where the bytes are poorer than the disposition implies.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-asagao-jp.txt` is the decoration sample the render checks ran against (its credit-modal and overflow states are section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There is no base-theme include for this theme (its CSS is self-contained, section 3), no companion fragments, and no inbound-link repairs in other candidates.
