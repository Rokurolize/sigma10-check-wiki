# Review package — theme:ared-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ared-jp — origin CN, population #165 [GOSIGN2-LEDGER (b) row 165]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 3668556339075889d15440ddfe52c1b6c9dc11440281f4e44d11ba1a883188c5); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 142; GOSIGN2-LEDGER (b) row 165]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page page-overflow 328px@320 only (8px), runtime-hotlink site-theme chain + candidate-own ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com (judgment-required); sample credit-modal (preview-form), page-overflow 328px@320 + 884px@768 (cross-cutting static-credit), runtime-hotlink incl. the ah-sandbox hosts + sample font host; T3 clean on both pages (sidebar at left JP position, opens in both engines; subtitle doubling + preview-notice clipping cross-cutting). [RENDER-ROWS-RERUN16 (CN1) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN1)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 164, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 164]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 165]
- Computed against: canonical commit 13b5725f80aba2d622b96662fe2257ccbed5749d; candidate file pages/theme:ared-jp.txt sha256:3668556339075889d15440ddfe52c1b6c9dc11440281f4e44d11ba1a883188c5; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 165) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×2 and pseudo-ref ×1 (section 11); the render row's items (cross-cutting and delivery classes, section 11); P5 sandbox-host images (KB-58). **FLAGGED by this package** — the CSS header `content:` string still renders the department name in its Chinese glyph form (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ared | theme:ared-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 8 (first translation; the candidate's credit block records 初訳時参照リビジョン: 8) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-ared.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ared-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 562 lines / 10,327 bytes | 566 lines / 10,792 bytes |
| SHA-256 | ae4e6b6aa7c54d6dec46cf3ad96c9e88e6e1e209f3cae75bc3a7239b6839b8c1 | 1b89d34b078b5fff0d429ae89eb1bcf6f9237cc4c03bedd5fe401627a15b4cba |

Wave history: the candidate was created by the Stage 2 CN1 integration (commit 4a2f4a5); FIX-CREDIT-D (1869877) normalized its credit attribution; FIX4-IWA (8c62b7b, missing interwiki frames added to 31 themes, KB-07a) added its frame and is the last commit and the stamp's computed-against commit. The original has been superseded upstream since revision 8; the follow-up diff artifact `diff-ared-from8.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A department aesthetic theme from CN (the Abnormal Religion Expression Department, by Dr Hormress) whose port is the in-place kind: the exhibit body — image-block, blockquote specimens, an eight-tab tabview, and the full CSS in a code exhibit — is translated where it stands, and the change concentrates at the two ends of the file. At the head, the CN rating/credit furniture is replaced by the JP credit block and the frame the frame wave added; in the code exhibit, the font load and stack convert from Noto Serif SC to Noto Serif JP; at the tail, the delivery import is repointed from the original's live code URL to the candidate's own local--code on the draft host. Measured churn (diff.md, the generator's count: +53/−49 in 22 change blocks / 3 hunks). One item is flagged in the per-theme record: the header's CSS `content:` string still renders the department name in Chinese glyph forms, exactly as the T4 lane recorded, and no ledger outcome line dispositions it.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 22 change blocks — 16 specific (72.7%), 5 heuristic (22.7%), 1 residue (4.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 8 |
| TRANS-UNANCHORED | 7 |
| DELIVERY-MOVE | 3 |
| INCLUDE-REPOINT | 3 |
| DRAFT-HOST | 2 |
| ESCAPED-INCLUDE | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| ANNOTATION | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 5 heuristic blocks are one-line exhibit translations (B4, B5, B7, B9, B10, section 6) and the commented tab's title (B18, sections 6 and 10); the 1 residue block is a blank line (section 9); the single EXHIBIT-RESTRUCTURE primary (B3) is the image-block exhibit carried with its caption translated, not a restructure (section 8); the DELIVERY-MOVE primaries are alignment moves inside the carried code exhibit (the font lines, sections 3–4), not relocations of the delivery itself. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ared-jp; original theme:ared on scp-wiki-cn at reference revision 8; candidate `pages/theme:ared-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN1 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The original opens directly with its tag gate (`[[iftags +版式]]`, original L1); the candidate opens with the added frame (candidate L1–4) and then the localized gate (candidate L6).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for ared-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a rating block and a CN credit block side by side (original L2–14): a bare `[[module rate]]` under its 评分模块 label, and the `:scp-wiki-cn:credit:start`/`more`/`end` triple under its 著作信息评分模块 label. The candidate deletes both (blocks B1–B2) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying all eight ruling-3 fields (title 异常宗教表现部 版式; 翻訳責任者 AI; 翻訳年 2026; 原題 异常宗教表现部 版式; 著作権者 Dr Hormress; 作成年 2021; 初訳時参照リビジョン 8; the source link, section 7). The title fields carry the original's Chinese title as the work's name; the department's name in the candidate's own prose is written in Japanese glyph form (異常宗教表現部, candidate L23) — the contrast with the CSS string of the per-theme record. There is no license box on either side.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare rate module is deleted rather than duplicated (KB-09), and the CN credit triple is the foreign form of the same furniture, replaced by the JP module rather than kept alongside it. Ruling 3 fixes the eight fields; FIX-CREDIT-D normalized the translator field to its ruling-3 form.
- **Verify:** `grep -n 'module rate\|credit:start\|credit:more' candidate.txt` returns nothing (the JP preview pair is `credit:start-preview`); read candidate L8–17 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Two escaped-include repoints in the usage exhibits (blocks B6, B8): `@@[[include :scp-wiki-cn:theme:ared]]@@` → `@@[[include :scp-jp:theme:ared]]@@` as built (candidate L32) and its dark-mode form `@@[[include :scp-jp:theme:ared dark=*]]@@` (candidate L38). As built, both repoints changed the branch prefix but kept the original's slug, naming a page that does not exist on scp-jp; the population sweep has since completed both to this candidate's posting name (`:scp-jp:theme:ared-jp`, the second as `:scp-jp:theme:ared-jp dark=*`) — see the per-theme record. The image-block exhibit (candidate L21) is a bare `component:image-block` include, unchanged in form on both sides; only its caption was translated (section 6). The candidate's remaining includes are the frame (section 3) and the credit pair (section 1); every named include in the candidate is `:scp-jp:` or the site-local component form.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp, and the escaped usage examples are repointed on the same rule, because the snippet a user pastes must name the JP theme page — including its `dark=*` parameter form. As built, the repoint satisfied the branch half of that rule only; the sweep's completion of the two names is what brings the snippets under it. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the image-block exhibit, and the two escaped usage lines.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The theme's CSS sits in a `[[code]]` exhibit on both sides (original L77–543 → candidate L80–546) and is delivered by a tail module import: the original's `[[module CSS]]` imports `https://scp-wiki-cn.wikidot.com/theme:ared/code/1` (original L545–546, the live URL form naming the original page); the candidate's imports `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aared-jp/1` (candidate L549–550, block B22). **Frame paragraph (the M-frame addition):** the candidate adds the interwiki-style frame at the head (candidate L1–4) with `priority=1` and `theme=` naming the same own-code delivery on the draft host — the single-layer own-code form, since the theme has no base distribution; the frame was absent at the T4 measurement and was added by FIX4-IWA (commit 8c62b7b, the KB-07a missing-frame wave), which the ledger records as P6 FIXED (frame waves; checker-verified). The tag-case changes that ride along (`[[code type="CSS"]]` → `type="css"`, `[[module CSS]]` → `[[module css]]`) are form normalizations inside blocks B19/B22, with no delivery effect.
- **Why:** P6/T3 (the interwiki-style supplement frame, KB-07) and P4/T9 (own-code delivery served from JP hosts — the original's import named the CN page's live code URL, which is the foreign-delivery form the port exists to replace). The draft-host form is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code\|interwiki-style\|code/1' candidate.txt` — L3 and L550, both draft-host forms of the candidate's own delivery.
- **Disposition:** FIXED (P6, FIX4-IWA frame wave); the draft-host lines are DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Font (blocks B19–B20, JPFONT-LOAD): the code exhibit's load converts from `family=Noto+Serif+SC:wght@900` to `family=Noto+Serif+JP:wght@900` (candidate L81, Google Fonts on both sides), and the one stack that names the face converts with it — `'Noto Serif SC', serif` → `'Noto Serif JP', serif` (candidate L127). Assets: the theme's logo, ARED_2_w.svg, is referenced twice, both times from the author's personal sandbox host, unchanged: the image-block exhibit (candidate L21) and the header background in the CSS (candidate L104), both `ah-sandbox.wikidot.com/local--files/hormress-s-logos/`. These are the T1 baseline's two hotlink errors and the T4 lane's P5 finding (live images ×2 from a personal wikidot delivery, display-affecting).
- **Why:** P7/T5 with KB-16: the SC face cannot render Japanese text, so the load and every stack that names it convert together — the complete form of the repair, load and stack in one move. P5/KB-58 for the logo: the campaign does not re-upload assets, and the ledger dispositions the sandbox-host delivery rather than fixing it (section 11).
- **Verify:** `grep -n 'Noto Serif' candidate.txt` — two lines (L81, L127), both JP; `grep -n 'ah-sandbox' candidate.txt` — L21 and L104.
- **Disposition:** Font conversion applied; the two sandbox-host asset lines are DISPOSITIONED (class (ii) / KB-58; GOSIGN2-LEDGER §(c3) P5).

### 5. Header, sidebar, and site furniture

- **What:** The header's rendered department label is a CSS `content:` string in the code exhibit (candidate L124): `content: "异常宗教表现部"` — carried byte-identical from the original (original L121), in Chinese glyph forms, while the candidate's prose writes the same name in Japanese glyph form (異常宗教表現部). That string is the per-theme record's flag. The repair has since landed (canonical commit 2437825): the string now reads 異常宗教表現部 in Japanese glyph forms, and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict). No header variable is overridden (no `--header-title` / `--header-subtitle` / `--logo-image`); the header background is the section 4 logo.
- **Why:** P9/T6 is a per-theme judgment and none was needed; the `content:` string is reader-visible text, so KB-18 governs it — which is why its untranslated state is a flag and not a formatting note.
- **Verify:** `sed -n '124p' candidate.txt` against the credit title (candidate L9) and the prose (candidate L23) — the three writings of the department name, two glyph forms.
- **Disposition:** Standing, with the `content:` string FLAGGED (per-theme record).

### 6. Text translation

- **What:** The exhibit body is translated in place, in counted groups. Eight TRANSLATION-ANCHORED blocks (B11–B17 and B3): the tabview's tab titles （要命的tab → 面倒なタブ; 另一个tab → 別のタブ, repeated across the tabview's eight tabs, candidate L50–73), the blockquote specimens （引用块 → 引用ブロック; 一条分割线 → 水平線; 嵌套引用块 → 入れ子の引用ブロック）, and the image-block caption (ARED Logo → AREDロゴ, inside B3). Five heuristic TRANS-UNANCHORED blocks (B4, B5, B7, B9, B10), each a one-line prose or instruction translation verified against the mirror (the theme description, the two usage instructions, the tabview's lead lines). One R1 item: the commented-out tab inside the tabview (`[!-- [[tab 另一个tab]] … --]`, original L70 → candidate L73, block B18) had its title translated inside the comment — porter-visible text, translated with the exhibit it sits in. The department name in prose is written in Japanese glyph form (異常宗教表現部, R5 glyph-form conversion applied to the prose), which is what makes the unconverted CSS string of section 5 visible by contrast. Simplified Chinese survives in the credit title fields (the work's original name) and in that one CSS string.
- **Why:** P10 (body, usage, and sample translation is the port's purpose), KB-18 (reader-visible strings), R5 (glyph-form conversion is a named sub-shape of translation: a retained string can be neither translated nor untouched, and the prose here took the conversion while the CSS string did not).
- **Verify:** The pairs are diff.md's three hunks in order; `grep -n 'content:' candidate.txt` isolates the one unconverted string.
- **Disposition:** Standing (the port itself); the one unconverted reader-visible string is flagged in section 5 and the per-theme record.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L16): `https://scp-wiki-cn.wikidot.com/theme:ared`, labelled with the original title. That is the original's recorded host — review/sources.tsv records the original at scp-wiki-cn.wikidot.com, the same host the mirror was taken from — so the link names the serving original and no host defect arises. The author link in the prose ([[*user dr-hormress]], candidate L23) is a Wikidot user link, host-independent. No other prose links exist in the candidate.
- **Why:** P11, under the dead-reference evidence standard; here the recorded host and the link agree, which is the check the jiha package's finding taught this batch to run on every theme.
- **Verify:** Compare candidate L16's host against the sources.tsv row's original_url host (scp-wiki-cn.wikidot.com) — identical.
- **Disposition:** Standing; no defect flag.

### 8. Structure

- **What:** The localize.md closing rule holds in full: variable names, selectors, and channel order are preserved; the code exhibit sits where the original's sits; the tabview keeps all eight tabs in order (one of them commented out on both sides); the JP additions are the head frame and the credit swap, not interleaved into the inherited body. The classifier's one EXHIBIT-RESTRUCTURE primary (B3) adjudicates to the image-block exhibit carried with its caption translated — an exhibit census (image-block, blockquote specimens, tabview with eight tabs, code exhibit) finds every original exhibit present on the candidate side in the same order, so the R3 question (sanctioned replacement vs silent deletion) does not arise for this theme.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include\|image-block' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** One block: B21, the classifier's residue — a single blank line added ahead of the candidate's closing `[[/iftags]]` (candidate L546). The classifier finds no whitespace-only block pair and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The tag-case normalizations of section 3 ride inside their delivery blocks and are recorded there.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The last hunk of diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** No porter-added annotations. The candidate's one `[!-- --]` block (candidate L73) is the original's own commented-out tab, carried with its title translated (section 6) — original content in comment form, not an addition. There are no translator notes and no editor line; the CSS comments in the code exhibit are the original's own.
- **Why:** R2: porter-added text is part of the change record; the one comment-form block present was checked explicitly and is inherited, not added.
- **Verify:** `grep -n '\[!--' candidate.txt original.txt` — one hit each, corresponding lines.
- **Disposition:** Standing (checked; the single comment block is original content).

### 11. Dispositions and exceptions

- **What:** Three groups, each with its ground. (1) T1's two hotlink errors and one pseudo-ref error: the hotlinks are the sandbox-host logo lines of section 4 — DISPOSITIONED in register c1 (hotlink, class (ii)) and per-theme as P5 (class (ii) / KB-58); the pseudo-ref is the draft-host delivery import (candidate L550) — class (iii) draft form, DISPOSITIONED in c1. (2) The render row's items (RENDER-ROWS-RERUN16 (CN1), which supersedes the earlier row for this theme): the page's 328px@320 overflow (8px over) and the sample's 884px@768 overflow are the cross-cutting static-credit shape (KB-33/KB-34 family); the runtime-hotlink lines are the site-theme chain (KB-40) plus the candidate-own ah-sandbox hosts, adjudicated to the same delivery class as item 1; the sample credit-modal errors are the preview form's property (KB-32, ruling 5); subtitle doubling and preview-notice clipping are the shared site-theme shape (KB-35); and T3 was clean on both pages, with the sidebar confirmed at the JP position in both engines. All DISPOSITIONED, none charged to the candidate. (3) The header `content:` string: recorded by the T4 lane as display-affecting, with no outcome line in §(c3) — FLAGGED in the per-theme record. The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 142): exit 1, 3 errors / 1 warn / 1 info (hotlink×2, pseudo-ref×1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-RERUN16 (CN1), superseding the RENDER-ROWS-2 row by rule S1): FINDINGS, every item dispositioned (section 11 item 2); engine coverage full (chromium and webkit, both pages); T3 clean on both pages. (c) T4/T5 (LOCALIZE-ROWS row 164): FINDINGS jointly, display-affecting findings 4 — the CSS `content:` Chinese header string with its glyph variance against the JP text (item a; its current state is the per-theme record's flag), the pattern-5 live images ×2 (item b; dispositioned, section 11), the absent interwiki-style (item c; since FIXED by FIX4-IWA, section 3), and the row's §3 item. The ledger §(c3) line records the outcomes: P5 DISPOSITIONED, P6 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +53/−49 in 22 change blocks / 3 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ared-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 165; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The header string that still renders in Chinese glyph forms

LOCALIZE-ROWS row 164 records the T4 lane's lead finding for this theme: the CSS `content:` string at the header keeps the Chinese department name (display-affecting), with glyph variance against the candidate's Japanese text. The bytes at the FIX5 head bear it out exactly. Candidate L124 reads `content: "异常宗教表现部";`, byte-identical to original L121 — the string was carried, not converted. The candidate's own prose writes the same name in Japanese glyph form (異常宗教表現部, candidate L23), and its credit title fields keep the Chinese title as the work's original name (candidate L9, L12), so the file contains both forms, each in a defensible place except this one: the `content:` string is reader-visible rendered text (it is the header's department label), and KB-18 governs reader-visible strings. No ledger outcome line for this theme dispositions it (the §(c3) line covers P5 and P6 only). The repair a future editor should make is a one-line glyph conversion of that string to 異常宗教表現部, matching the prose. Making it here is outside this package's remit, which is to document the candidate as it stands; the flag is recorded so a reviewer following the header today sees the variance the T4 lane saw.

### The usage examples' posting name

The two escaped usage examples (candidate L32 and L38, the second in its `dark=*` parameter form) as built named this theme by its original's slug on the JP branch, `:scp-jp:theme:ared` — a page that does not exist on scp-jp, under the campaign's settled rule for usage examples (AGENTS.md §6). The usage-example population sweep has since completed both names to this candidate's posting name, `:scp-jp:theme:ared-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commits b5cb724 and 13b5725 — this file's two sweep lines were re-applied in 13b5725 after a restore briefly reverted them). This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B4 | 20-20 → 23-23 (body → body) | heuristic TRANS-UNANCHORED | One-line prose translation (theme description); section 6 |
| B5 | 26-26 → 29-29 (body → body) | heuristic TRANS-UNANCHORED | One-line instruction translation (first usage lead); section 6 |
| B7 | 32-32 → 35-35 (body → body) | heuristic TRANS-UNANCHORED | One-line instruction translation (dark-mode lead); section 6 |
| B9 | 40-40 → 43-43 (body → body) | heuristic TRANS-UNANCHORED | One-line specimen translation (blockquote lead); section 6 |
| B10 | 43-44 → 46-47 (body → body) | heuristic TRANS-UNANCHORED | Two-line specimen translation (blockquote body); section 6 |
| B18 | 70-70 → 73-73 (body → body) | tier-B TRANS-UNANCHORED + ANNOTATION | The original's commented-out tab, title translated inside the comment (R1); sections 6 and 10 |
| B21 | at 543 → 546-546 (body → body) | residue, no signature | Single blank line added ahead of `[[/iftags]]`; section 9 |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-ared-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 异常宗教表现部 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:ared — revision 8
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
