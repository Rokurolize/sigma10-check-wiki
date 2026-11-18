# Review package — theme:mole-cricket-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:mole-cricket-jp — origin KO, population #274 [GOSIGN2-LEDGER (b) row 274]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 274]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 278; GOSIGN2-LEDGER (b) row 274]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 273, source LOCALIZE-S2-F]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 273]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 274]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:mole-cricket-jp.txt sha256:17925b1624af76465675af1f4d7c30eaece02fd978f231d917bde8275270327b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 278) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (sections 3 and 4); the render row's items (section 11). T4/T5 passed outright with zero findings, the cleanest localize row in this batch |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:mole-cricket | theme:mole-cricket-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 11 (first translation; the candidate's credit block records 初訳時参照リビジョン: 11) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-mole-cricket.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:mole-cricket-jp.txt`, byte-identical at canonical HEAD c635d01 |
| Lines / bytes | 616 lines / 11,591 bytes | 629 lines / 13,260 bytes |
| SHA-256 | 57abda46c875d0dae48c9b835baf05cc3bd47b315e21858b3ee36bc61c15a734 | 17925b1624af76465675af1f4d7c30eaece02fd978f231d917bde8275270327b |

Wave history: the candidate was created by the Stage 2 KO6 integration (commit 8dd8c2f) and has exactly one later commit, 1869877, the FIX-CREDIT-D wave's translator-attribution normalization. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A standard mechanical port, and the lightest diff in this batch. The original is a self-contained KO theme page: it self-delivers through a head module and an interwiki-style frame, carries a bare Rate module and an empty info pair for credit, and presents its CSS in one code exhibit. The candidate swaps the credit furniture for the JP preview credit block (with two attribution fields beyond the standard eight, section 1), repoints the delivery frame to the draft host, re-hosts the theme's two images to the JP side, replaces the Korean display font Dongle with the rounded JP face Kosugi Maru in load and stacks, retunes the header geometry and the mobile media queries for the translated header strings (section 5), translates the exhibit body, and appends a license box that attributes the two images and states honestly that the original carries no license statement for them (section 1). Measured churn (diff.md, the generator's difflib count with autojunk off: +56/−48, 104 changed lines in 24 change blocks / 5 hunks; a GNU-diff count of the same pair gives 105 changed lines — the difference is alignment choice, not content). No defect flag arises for this theme: its usage example already names the candidate's posting name in the -jp form, and its credit source link names the recorded scpko host.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 24 change blocks — 15 specific (62.5%), 8 heuristic (33.3%), 1 residue (4.2%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 7 |
| TRANSLATION-ANCHORED | 6 |
| DRAFT-HOST | 5 |
| CSS-BODY | 4 |
| DELIVERY-HOST | 2 |
| CONTENT-STRING | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 4 CSS-BODY blocks are header geometry and media-query adaptations riding the font and content-string changes (section 5), not churn; the 2 EXHIBIT-RESTRUCTURE primaries are an include repoint and the image-block exhibit's asset re-host (sections 2 and 4); the single residue block (B22) is a deleted blank line between the two media queries, absorbed by the media-query rewrite around it (section 5); the COMPONENT-SWAP label on B6 is the credit furniture swap itself (section 1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:mole-cricket-jp; original theme:mole-cricket on scpko at reference revision 11; candidate `pages/theme:mole-cricket-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO6 wave (sources.tsv kind: standard; no production JP counterpart is recorded for this theme, so the R4 adoption question does not arise). The frame order is the original's own: delivery module and interwiki-style include first (original L1–7), then the tag gate `[[iftags +테마]]` (original L10); the candidate keeps that order (candidate L1–10) with the gate's tag localized and the credit block directly under it.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate is P2, the frame is P4/P6 (section 3).
- **Verify:** The sources.tsv row for mole-cricket-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a right-aligned div under a "평가 모듈:" label (original L16–19), a second div headed "정보 모듈이 있는 평가 모듈:" (original L21–24), and an empty `:scp-wiki:info:start`/`end` pair (original L25–28, no body). The candidate deletes all three (blocks B4, B6) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L11–22) carrying the eight ruling-3 fields (title ケラCSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 땅강아지 CSS 테마; 著作権者 [[*user c_bonefish]]; 作成年 2022; 初訳時参照リビジョン 11; the source link, section 7) plus two attribution fields beyond the eight: a フォント field (Kosugi Maru, Google Fonts, SIL Open Font License) and an 画像の出典 field (the two images re-hosted from SCP-KO; back.png made from a Pixabay CC0 wheat silhouette, as the original's comment records). The field's author matches the original's prose attribution (made by c_bonefish) — no name is dropped. The translator field took its ruling-3 form in 1869877. The candidate also appends a license box after the code exhibit (candidate L614–628, block B24): a `:scp-jp:component:license-box-backend`/`license-box-end` pair with one entry per image (back.png, author c_bonefish; logo.png, author thd-glasses), each entry stating that the original carries no license statement for the file and advising confirmation with the author before posting, and each linking its source on scpko. The original has no license box and no image entries; the box is an added attribution record, and its "no license stated" wording is the honest form of it — it does not invent a license the original never granted. The two attribution statements address different objects and do not conflict: the credit block's 画像の出典 field concerns the Pixabay base image back.png was made from (CC0), while the license-box entries concern the derived files themselves, for which the original states no license.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the empty info pair is ledger class C residue. Ruling 3 fixes the eight fields and the translator credit form; the two extra fields and the license box are T12 attribution supplements, the campaign's TASL record-keeping applied to a theme whose assets arrived without one.
- **Verify:** `grep -n 'info:start\|info:end\|module Rate' candidate.txt` returns nothing; read candidate L11–22 against the eight fields plus the two supplements, and candidate L614–628 for the license box.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the license box is a standing supplement.

### 2. Includes and components

- **What:** One repoint block, and one deliberate non-change. B2: the interwiki-style include, `:scp-wiki:component:interwiki-style` → `:scp-jp:component:interwiki-style` (original L5 → candidate L5; its theme= parameter is section 3). The non-change: the image-block exhibit's include keeps the original's bare form, `[[include component:image-block ...]]` (original L33 → candidate L32), with no wiki prefix on either side; its change is the asset re-host and caption translation (sections 4 and 6). A bare include resolves on the wiki that hosts the page, so the form names scpko's component on the original and names scp-jp's component in the candidate — the counterpart follows from the hosting, and component:image-block exists on scp-jp. The credit and license-box includes (section 1) complete the candidate's include list.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. The interwiki include named the EN component explicitly and is repointed; the image-block include named no wiki and needs none. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the interwiki, credit, and license-box includes name `:scp-jp:` targets; the image-block include is the bare form on both sides.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original self-delivers: a head `[[module CSS]]` importing its own `local--code/theme%3Amole-cricket/1` from scpko.wdfiles.com (original L2), and the interwiki-style include at priority 1 whose `theme=` names the same delivery in its wikidot.com URL form (original L5–7). The candidate keeps the same two-part frame and repoints it to the candidate's own delivery on the draft host: the module imports `local--code/theme%3Amole-cricket-jp/1` from sigma10-jp-test.wdfiles.com (candidate L2), and the include's `theme=` names the same draft-host URL (candidate L7), so the two halves of the frame agree on one address in the candidate. The original already carried the interwiki-style frame, so this theme is M-pure, not M-frame. Two of T1's four pseudo-ref errors are these head lines.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame form, priority 1 for the theme's own layer). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L2 and L7, both draft-host; compare the sibling heads in `pages/`.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii); the production-host rewrite at posting is class (ii) mechanics).

### 4. Fonts and assets

- **What:** Load (block B14): the original loads the Korean display face Dongle from Google Fonts (original L76); the candidate loads Kosugi Maru from the same service (candidate L75). Stacks: the two header stacks that named `'Dongle'` now name `'Kosugi Maru', 'Hiragino Maru Gothic ProN', 'Yu Gothic', 'Noto Sans JP', sans-serif` (inside blocks B17 and B20, with the content strings of section 5); Kosugi Maru is loaded, so no stack names an unloaded first family. Assets: the theme's two images are re-hosted from scpko to the draft host's own folder — `back.png` (candidate L80's zone) and `logo.png` (candidate L86's zone) under `sigma10-jp-test.wdfiles.com/local--files/theme%3Amole-cricket-jp/` — and the image-block exhibit's `name=` takes the same draft-host form (candidate L32). These draft-host asset lines are the other two of T1's four pseudo-ref errors. The re-hosting is recorded in the credit block's 画像の出典 field and in the license box (section 1).
- **Why:** P7/T5 with KB-16 (the font load gap): Dongle is a Hangul display face with no kana; Kosugi Maru is the rounded JP face that keeps the header's character, and the load and both stacks change together. P5 with KB-17 (asset hosts): the theme's own images are re-hosted to the JP side; the draft-host form is class (iii) at this stage.
- **Verify:** `grep -n '@import\|font-family' candidate.txt` — the load at L75 and the two header stacks; `grep -n 'wdfiles' candidate.txt` returns the delivery lines of section 3 and the three asset lines, all draft-host.
- **Disposition:** Font load and stacks applied; the draft-host asset URLs are DISPOSITIONED (class (iii) draft form; posting rewrites them to the production host).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header carries two rendered strings, and both are translated with their geometry retuned. The h1 string: `content: "두레원"` → `content: "ドゥレウォン"`, with its stack swapped to the Kosugi Maru stack (block B17, candidate L114–115). The h2 subtitle string: `content: "바람이 머물다 간 들판에"` → `content: "風がとどまっていった野原に"` (block B20, candidate L128–129), and its placement is retuned for the new face and string: `left: 350px` → `330px` and `font-size: 55px` → `38px` (blocks B18, B19, candidate L121–124). The mobile media queries gain the matching adaptation (blocks B21, B23): the 336–755px query adds `#header h1 a { font-size: 58px; }` and a `::before` position rule, and the ≤335px query changes the h1 size from 70px to 48px and adds the same positioning — the original's queries only hid the subtitle. The theme overrides no `--header-*` variables on either side. Residue block B22 (a blank line deleted between the two queries) is absorbed by this rewrite.
- **Why:** P9/T6 for the strings; the values are reader-visible header text, so their translation is P10/KB-18 carried in strings. The size and position changes are P8 layout adaptation: Kosugi Maru's metrics and the longer Japanese subtitle do not fit the geometry Dongle and the Korean string used, and the media queries are where the original itself puts its small-width header behavior. Ruling 2 is not engaged: both strings were translated, not kept.
- **Verify:** Read candidate L111–130 against original L112–130, and candidate L598–611 against original L597–613.
- **Disposition:** Standing (adaptation argued from the font metrics and string lengths).

### 6. Text translation

- **What:** The exhibit body is translated throughout, in counted groups. Six TRANSLATION-ANCHORED blocks (B7: the "페이지 요소" heading; B9: the heading samples 見出し1–6; B13: the "CSS 테마 코드" heading; and the tab samples) and the prose TRANS-UNANCHORED blocks (B5, B10, B12: the intro prose and exhibit strings, including the dummy-text sample ㅁㄴㅇㄹ → あいうえお and the footnote sample 똑똑 → コンコン). The link sample's labels are translated inside B11 (section 7). The CSS comments are carried untranslated where they are the original's section names in English ("Header", "Login & Search & Top Bar", "etc." — the original's own English, kept as-is), and the banner comment's attribution lines are the credit record of section 1. Korean survives in the candidate in exactly one place: the credit block's original-title field (candidate L15), a quotation. R5 glyph-form conversion: none — the source is Korean.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`). The unanchored group is where a silent deletion would hide, which is why each was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's hunks in order; a Hangul scan of candidate.txt returns only candidate L15.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the one quotation.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L19): `https://scpko.wikidot.com/theme:mole-cricket`, whose host is the original's recorded host in sources.tsv and which serves the original — no probe discrepancy, no defect. The exhibit links are the correct-form control for this batch: the usage example reads `> @@[[include :scp-jp:theme:mole-cricket-jp]]@@` (candidate L27) and the link sample links `[[[theme:mole-cricket-jp|訪問済みリンク]]]` (candidate L48), both naming the candidate's posting name with the -jp suffix, where the sibling candidates flagged in this campaign kept the plain slug. The license box's two source links (section 1) name the images' KO originals and are attribution records, not navigation.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; the source link satisfies it as written, and the exhibits name the page a user would actually paste.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the two license-box source links are the only hits.
- **Disposition:** Standing; no flag for this theme.

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the candidate's single code exhibit sits where the original's sits, and an exhibit census confirms the shape: the tabview and its two tabs, the link and footnote samples, the heading samples, the image-block div, and the code exhibit are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise. The classifier's two EXHIBIT-RESTRUCTURE primaries adjudicate elsewhere: B2 is the interwiki include repoint (section 2), and B8 is the image-block exhibit's asset re-host with its caption translation (sections 4 and 6). The JP additions arrive at the head (sections 1–3), inside the header rules (section 5), and as the appended license box (section 1), not interleaved into the inherited CSS.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond one to one, with the license-box pair as the only addition.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None beyond the absorbed blank line of section 5. The classifier finds no WS-ONLY block and no re-indentation in this pair (0 and 0): the original's code exhibit carries no trailing-space blank lines of the kind the EN-wave themes shed by the dozen, so there is no formatting mass to disclose.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the class is empty and the section says so with its ground.
- **Verify:** classification.json's summary for this package: WS-ONLY absent, reindent_blocks 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None as comments. The candidate carries no porter-added comment: the code exhibit's comments are the original's own, and there is no provenance comment at the head of the code block. The porter's added text is functional and is recorded where it acts: the credit block's two attribution fields and the license box (section 1). This section was checked explicitly against the candidate's comment lines rather than taken from the skeleton's "none".
- **Why:** R2: porter-added text is part of the change record; here the record is that the additions are the attribution furniture, not annotations.
- **Verify:** `grep -n '/\*' candidate.txt` — all hits are the original's own comments.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) T1's four pseudo-ref errors: the candidate's own draft-host lines (the delivery pair of section 3 and the asset lines of section 4); class (iii), sanctioned at draft stage, with the posting rewrite class (ii) mechanics. There is no hotlink error and no class (i) error for this theme: every asset was re-hosted rather than kept on the KO host. (2) The render row's items, all environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the sample's 884px@768 overflow reading (capture-layer width reading of the KB-44 family). T3 reports nothing beyond the cross-cutting items.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 278): exit 1, 4 errors / 1 warn / 1 info; all four errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO6)): FINDINGS, the items of section 11(2), all dispositioned; T3 nothing beyond cross-cutting items; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 273): PASS and PASS, display-affecting findings 0 — the only outright localize pass in this batch, and consistent with the bytes this package documents (correct-form exhibits, recorded host, no dropped name). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +56/−48 in 24 change blocks / 5 hunks; the GNU-diff count of the same pair is 105 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:mole-cricket-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 278; go-sign, COMPLETION-REPORT §10).

## Per-theme record

No per-theme record is required for this theme: no finding is flagged, no prose record disagrees with the bytes, and the two judgment calls a reviewer is most likely to question — the bare image-block include form (section 2) and the license box's "no license stated" entries (section 1) — are argued in their standing sections with both sides' text. The theme is also this batch's correct-form control for the usage-example name family: its exhibits name theme:mole-cricket-jp, the posting name, where the flagged sibling candidates kept the plain slug.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-mole-cricket-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 땅강아지 CSS 테마
- **Author:** c_bonefish
- **Source:** https://scpko.wikidot.com/theme:mole-cricket — revision 11
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
