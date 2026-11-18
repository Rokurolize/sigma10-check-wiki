# Review package — theme:mr-reprisal-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:mr-reprisal-jp — origin KO, population #275 [GOSIGN2-LEDGER (b) row 275]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 337f7e8616539f556d41f9688c669ddff0d605020e3da5d2d8377df4ff9640c2); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 279; GOSIGN2-LEDGER (b) row 275]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO6))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 274, source LOCALIZE-S2-F]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 274]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 275]
- Computed against: canonical commit 1db8300464d032875c6f8cc6ab61a5cafc6b7433; candidate file pages/theme:mr-reprisal-jp.txt sha256:337f7e8616539f556d41f9688c669ddff0d605020e3da5d2d8377df4ff9640c2; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 275) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (class (ii), section 11); the render row's items (site-theme chain, credit-modal preview form, 884px@768 overflow, section 11). **FLAGGED by this package** — the credit block's holder field names the theme's author but not the base-code author its banner credits (per-theme record, item 1), and one inherited credit-module rule keeps the pre-correction selector form (per-theme record, item 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:mr-reprisal | theme:mr-reprisal-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 13 (first translation; the candidate's credit block records 初訳時参照リビジョン: 13) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-mr-reprisal.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:mr-reprisal-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 626 lines / 12,414 bytes | 639 lines / 13,881 bytes |
| SHA-256 | 60e8aa5fa3a73adb7863e8272d3ff154f7993184d4141d049ea5caaf5c80ab57 | 4b62b0eac3f0b74580393368a6e47658ed9353f74aa7781f6eb1bf98a7ced355 |

Wave history: the candidate arrived through the Stage 2 KO integrations (commits 18280b3, lane-dsh-ko1, and 8dd8c2f, lane-oc-ko6; the LOCALIZE-S2-F wave's port) and has one later commit, 1869877 (FIX-CREDIT-D, the translator-attribution normalization run over 163 candidate files). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The lightest-touch shape in this batch: a self-contained KO theme whose topology, delivery form, and CSS body survive the port nearly line for line, with the change concentrated at the head (delivery re-hosting, the credit furniture swap) and in the exhibit text. The original self-delivers from the live KO host with an interwiki-style frame it already had; the candidate keeps the same two-part form on the draft host. The Korean font faces are replaced by JP faces in load and stack together, the two background images are re-hosted, the body and exhibits are translated, and a JP license box is appended at the tail, its entries honestly recording that the original states no license for the two images. Measured churn (diff.md, the generator's difflib count with autojunk off: +53/−45, 98 changed lines in 20 change blocks / 5 hunks). Two items are flagged in the per-theme record: the credit holder field's silence on the base-code author, and one inherited credit rule in the pre-correction selector form.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 20 change blocks — 16 specific (80.0%), 4 heuristic (20.0%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 8 |
| TRANSLATION-ANCHORED | 6 |
| FONT-IMPORT | 2 |
| CONTENT-STRING | 2 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 4 |
| SELF-DELIVERY | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| INCLUDE-REPOINT | 2 |
| CREDIT-PREVIEW | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| ESCAPED-INCLUDE | 1 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| LICENSE-BOX | 1 |

Adjudication for this README (every block was read against the bytes): the two EXHIBIT-RESTRUCTURE primaries are not exhibit changes — B2 is the interwiki-style include's repoint (section 2) and B9 is the image-block exhibit line, whose only change is its asset's host (section 4); the exhibit census in section 8 confirms every exhibit carried. B7's COMPONENT-SWAP label adjudicates to the info-pair deletion and the usage example's repoint, not a component exchange. The four heuristic blocks are the translation pairs the matcher could not anchor (B5, B11, B13 and one of B7's lines), each verified line by line for section 6. The skeleton's section arrangement understates sections 1 and 4: the license box (B20) belongs to section 1's T4 half, and the font credit lives in the credit block's supplementary lines, not in a CSS block. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:mr-reprisal-jp; original theme:mr-reprisal on scpko at reference revision 13; candidate `pages/theme:mr-reprisal-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame did not move: the original opens with its delivery module and interwiki-style frame ahead of its gate (original L1–10), and the candidate keeps that order exactly, with the gate's tag localized (candidate L10).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for mr-reprisal-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame's host changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labeled exhibit pair at the head of the body: a centered bare `[[module Rate]]` under its caption (original L13–16), and an unprefixed `[[include info:start]]`/`[[include info:end]]` pair under a second caption (original L18–22). The candidate deletes both exhibits and their captions (blocks B6–B7) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block directly under the gate (candidate L11–22) carrying the eight ruling-3 fields (title ミスター・リプライザルCSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 복수 씨 CSS 테마, the original's Korean title kept as the original-title field; 著作権者 [[*user c_bonefish]]; 作成年 2022; 初訳時参照リビジョン 13; the source link, candidate L19, on scpko.wikidot.com, the host sources.tsv records for the original). Two supplementary lines ride inside the block beyond the eight fields: a **フォント:** line crediting the four loaded faces (Kaisei Decol・Kiwi Maru・Berkshire Swash・Sansita, Google Fonts, SIL Open Font License 等) and an **画像の出典:** line recording that the two images are re-hosted from SCP-KO (section 4). Author check against the original: c_bonefish is the theme's author (the original's prose, original L26, and its CSS banner, original L66–67); the banner's second credit, "Base Code by Denevola", is not reflected in the holder field — flagged in the per-theme record, item 1. The translator field took its ruling-3 form in 1869877 (FIX-CREDIT-D). The section's T4 half: a JP license box is appended inside the gate at the tail (candidate L625–638, block B20), where the original has none. Its two entries cover the re-hosted images (back.png, logo.png; author c_bonefish; source the KO file URLs) and state the license honestly as not stated in the original, with a note to confirm with the author before posting (per-theme record, item 3). T7 credit-module CSS: the theme carries its own credit-rule group inherited from the original (`.creditRate`, `.rate-box-with-credit-button`, `.creditButton p a`, the `.fa-info` pair; original L499–524 → candidate L498–523), byte-identical on both sides; one selector in it is flagged in the per-theme record, item 2. No supplement was added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate and the info pair are deleted rather than duplicated (a kept Rate would be the KB-09 duplicate; a kept info pair is ledger class C residue). Ruling 3 fixes the eight fields; P7 requires the added fonts' credit to be written into the credit block, which the supplementary フォント line does. T4: the license box is a supplement where the original had none, in the settled JP form.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L11–22 against the eight fields plus the two supplementary lines; `grep -n 'license-box' candidate.txt` returns the pair at L625 and L638.
- **Disposition:** Applied (LOCALIZE-ROWS row 274 records this theme's T4 outcome as PASS with no credit item).

### 2. Includes and components

- **What:** Three include changes. (a) The interwiki-style include the original borrowed from the EN wiki (`:scp-wiki:component:interwiki-style`, original L5) is repointed to `:scp-jp:` (candidate L5, block B2; its `theme=` value is section 3). (b) The usage example's escaped include is repointed with the candidate's own posting name (original L30 `:scpko:theme:mr-reprisal` → candidate L29 `:scp-jp:theme:mr-reprisal-jp`, block B7) — the correct form, in contrast to the plain-slug shape flagged in sibling packages. (c) The image-block exhibit include keeps its unprefixed same-wiki form on both sides (`[[include component:image-block ...]]`, original L33 → candidate L34); only its asset parameter changes (section 4). The credit pair (section 1) and the license-box pair (section 1) complete the live include list; every prefixed include names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that exists. The unprefixed image-block form resolves on the posting wiki on both sides (scpko for the original, scp-jp for the candidate), so its form is carried, not repointed. Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the image-block exhibit, and the license-box pair.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original already self-delivers in the campaign's form, from the live KO host: a head `[[module CSS]]` importing `local--code/theme%3Amr-reprisal/1` from scpko.wikidot.com (original L2), and the interwiki-style frame at priority 1 naming the same /1 (original L5–8). The candidate keeps both halves and changes only the host and the name: the draft host sigma10-jp-test.wdfiles.com and `theme%3Amr-reprisal-jp/1` (candidate L2 and L5–8, blocks B1 and B3). Priority 1 is the theme's own layer; the theme has no base, so there are no priority 2/3 entries and no base-delivery question. The code exhibit itself (`[[code type="css"]]`, original L62 → candidate L61) is the /1 body on both sides, carried at the same position.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame). No frame had to be added: this is the T3 form arriving with the original, re-hosted. The draft-host form is KB-41, class (iii).
- **Verify:** `grep -n 'local--code' candidate.txt` — L2 and L7; compare original L2 and L5–8.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Loads: the original's exhibit loads four faces (original L74–77): NapjakBlock from the KO wiki's own font folder (scpko.wdfiles.com/local--files/korean-font/), and Berkshire Swash, Sansita, and Stylish from Google Fonts. The candidate loads four (candidate L72–75): Kaisei Decol and Kiwi Maru from Google Fonts (the JP faces), with Berkshire Swash and Sansita kept. NapjakBlock and Stylish are dropped from the loads and from the stacks together: NapjakBlock is a Korean display face served from a foreign wiki's file folder, and Stylish held the second stack position the JP face takes. Stacks (the FONT-IMPORT blocks B15–B16 and their stack lines): the header rule's stack `'Berkshire Swash', 'NapjakBlock', cursive` → `'Kaisei Decol', 'Berkshire Swash', serif` (candidate L120), and the second stack `'Sansita', 'Stylish', sans-serif` → `'Kiwi Maru', 'Sansita', sans-serif` (candidate L133). Load-gap check: the first-named face of each stack (Kaisei Decol, Kiwi Maru) is loaded, and both kept faces are loaded, so there is no KB-16 gap. The credit block's フォント line (section 1) is the P7 credit half of this change. Assets (B17 and B9): the two background images move from `scpko.wikidot.com/local--files/theme:mr-reprisal/` to the candidate's own folder with file names unchanged — `--image-1` back.png on the draft host (candidate L78) and `--image-2` logo.png on the production host scp-jp.wdfiles.com (candidate L79) — and the image-block exhibit's logo.png takes the draft-host form (candidate L34). The one production-form line among draft-form siblings is recorded here because a reviewer will trip on it; both forms are posting-procedure mechanics.
- **Why:** P7 with KB-16 (the load and every stack that names a face change together; a Korean-only face cannot render Japanese text, and its host is a foreign file folder in any case). P5 with KB-17 (the theme's own images are re-hosted to the JP side; Google Fonts is an allowed hotlink host).
- **Verify:** `grep -n '@import' candidate.txt` — five imports (L2 own code; L72–75 the exhibit's four); `grep -n 'local--files' candidate.txt` against the three asset lines above.
- **Disposition:** Loads and stacks applied; the asset URL host forms are DISPOSITIONED (classes (ii)/(iii)).

### 5. Header, sidebar, and site furniture

- **What:** None beyond sections 3 and 4: the candidate overrides no header variable (there is no `--header-title`, `--header-subtitle`, or `--logo-image` on either side; the header image travels as the `--image-1`/`--image-2` asset variables of section 4), and no P8 layout adaptation fired or was needed. The theme's header styling is its own CSS, carried unchanged apart from the font lines of section 4 and the two translated `content:` strings of section 6.
- **Why:** The section is present so "checked, absent" is on record: P9/T6 do not apply to a theme that sets no header variables, and P8 does not apply where the JP furniture needed no adaptation.
- **Verify:** `grep -n -- '--header-\|--logo-image' candidate.txt` returns nothing.
- **Disposition:** None — checked, absent.

### 6. Text translation

- **What:** The body is translated throughout, in three counted groups. Six TRANSLATION-ANCHORED blocks (B8, B10, B14, and the CSS-side B18–B19 with one more body pair): the homage line's label, the heading samples, and the closing prose. Eight TRANS-UNANCHORED blocks by primary label (B4–B7, B11–B13 and one exhibit pair), each a one-line prose or exhibit-string translation verified line by line against the mirror: the author prose (with its hub link, section 7), the usage instructions, the tab exhibit's sample text (the Korean filler ㅁㄴㅇㄹ becomes サンプルテキスト), the link labels (未訪問リンク / 訪問済みリンク), and the footnote's onomatopoeia (똑똑, a knock, becomes コンコン, its Japanese counterpart). The original's standalone title heading (`+ 복수 씨 CSS 테마`, original L11) has no counterpart heading: the title moved into the credit block's title field (section 1), and the body's first heading is now `+ ページ要素`. The two reader-visible CSS strings are the `content:` values (B18, B19): "원더테인먼트 박사!" → "ワンダーテインメント博士！" (candidate L121) and the longer slogan line → "忘れないで、あなたの頭の中はワンダフルな場所だってことを" (candidate L134). In-CSS text (R1), stated separately: the exhibit's banner comment (Created by c_bonefish / Base Code by Denevola / CC BY-SA 3.0) is carried verbatim in English, porter-visible only, as the attribution record. Korean survives in the candidate on exactly one line, the credit block's original-title field (candidate L15), where it is a quotation.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`).
- **Verify:** The pairs are diff.md's five hunks in order; a Hangul scan of candidate.txt returns only candidate L15.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the one quotation.

### 7. Links

- **What:** Two prose-link changes. (a) The hub link in the author prose is repointed to the JP counterpart hub (original L26 `scpko.wikidot.com/dr-wondertainment-hub` → candidate L26 `scp-jp.wikidot.com/dr-wondertainment-hub`, block B7's link half). (b) The homage link to the EN Wondertainment theme (`[*https://scp-wiki.wikidot.com/theme:wondertainment|...]`, original L24 → candidate L24) keeps its target on both sides; only its label is translated. The tab exhibit's visited-link sample is repointed to the candidate's own page (original L50 `[[[theme:mr-reprisal|...]]]` → candidate L50 `[[[theme:mr-reprisal-jp|...]]]`, block B12). The credit source link (candidate L19) names scpko.wikidot.com, the recorded host, and serves the original. The license box's 出典 links (candidate L631, L636) point back at the KO file URLs: they are provenance records for the re-hosted images, not loads.
- **Why:** P11: prose links take the JP counterpart where one exists (the hub), and the serving original where the link is itself the homage record (the theme link). The dead-reference standard is not engaged; nothing here is dead.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the hub, the homage link, the source link, and the two 出典 records.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds in full. Topology is identical on both sides (head module, frame, gate, body, one code exhibit, gate close), variable names and selectors are preserved, and the JP corrections arrive at the edges: the credit block at the head of the body, the license box at its tail. Exhibit census: the image-block exhibit, the heading samples, the tabview exhibit with its footnote, and the code exhibit are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise. The two furniture exhibits that disappear (the labeled Rate and info exhibits) are the P3 furniture swap of section 1, not sample content. The two EXHIBIT-RESTRUCTURE primaries adjudicate to an include repoint (B2, section 2) and an asset host change inside an exhibit line (B9, section 4).
- **Why:** R3's distinction is decided by the census, not the label; the closing rule is what keeps a follow-up diff applicable, and this port keeps it.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond, with the credit and license pairs added at the edges.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds 0 WS-ONLY blocks and 0 re-indentation pairs, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The skeleton's section 9 counts in classification.json (`reindent_blocks`: 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, not assumed: the candidate adds no comment-form annotation (no `[!-- --]` note and no added CSS comment; the exhibit's banner comment is the original's own, carried verbatim, section 6). The port's additions that look like annotations are credit prose: the credit block's フォント and 画像の出典 lines (section 1) and the license box's license-absence note (per-theme record, item 3).
- **Why:** R2 requires the check to be explicit, because annotations ride inside other labeled blocks in sibling packages; here the grep is the evidence.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; compare the CSS comments on both sides of diff.md's code hunks.
- **Disposition:** None — checked, absent.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host `local--code` and `local--files` lines (sections 3 and 4); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. One asset line (`--image-2`, candidate L79) already carries the production host form; recorded in section 4. (2) The render row's three items (RENDER-ROWS-2, lane RENDER-S2-H (KO6)), none charged to the candidate at the ledger determination: the page's runtime-hotlink site-theme chain (KB-40, environment layer); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the sample's 884px@768 overflow, recorded verbatim in the render row. (3) The two per-theme flags (the holder field's silence on Denevola; the inherited `.creditButton p a` selector) are flagged, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 279): exit 1, 4 errors / 1 warn / 1 info; all four errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-H (KO6)): FINDINGS, the three items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 274, LOCALIZE-S2-F): PASS / PASS, display-affecting findings 0. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +53/−45 in 20 change blocks / 5 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:mr-reprisal-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 275; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the holder field and Denevola (flagged) Adjudicated after this package was built (FIX-CREDITBTN item 2, commit 1db8300): Denevola stands in the banner; attribution stands, no edit. See the post-package repairs item below.

The original credits two people in two places: its prose names c_bonefish as the theme's maker (original L26), and its CSS banner reads "Created by c_bonefish / Base Code by Denevola" (original L66–67). The candidate's credit block names c_bonefish alone in the 著作権者 field (candidate L16), and the license box's `author=` parameter likewise names c_bonefish alone (candidate L626). Denevola's credit survives in the candidate only inside the carried banner comment (candidate L66–67), in the delivered CSS itself. The distinction from the sibling flags in this campaign is real — Denevola is credited with the base code, not with the theme's authorship, and the field does name the author of record — but the shape is the family the U-1 and U-2 batches repaired (a contributor the original names in its credit furniture, absent from the TASL field, surviving in a comment). This package flags the gap with both sides' text and does not edit the candidate; the ledger's determination for this theme is PASS and its T4 row charges nothing.

### Item 2 — the inherited `.creditButton p a` selector (flagged) Repaired after this package was built (FIX-CREDITBTN item 1, commit 1db8300): the selector now reads `.creditButton > a`; see the post-package repairs item below.

The theme's own credit-rule group is carried byte-identical (original L499–524 → candidate L498–523), including `.creditButton p a` (original L513 → candidate L512), which sets the credit anchor's `border-left` and `color` declarations. The campaign's T7 record (SUPPLEMENT-TYPES T7; KB-11) states the JP credit module emits the anchor as a direct child of `.creditButton`, without the `<p>` wrapper this selector requires, and sibling ports corrected exactly this shape: theme:sodium-jp in place (`.creditButton p a` → `.creditButton > a`, the R6 form) and theme:jiha-jp by an appended restatement module. In this candidate the rule stands uncorrected, so on the JP DOM it cannot match, and the credit anchor loses those two declarations. The theme's T4 row is PASS and no ledger line charges it; the render row's credit-modal item is the preview-form disposition, a different matter. This package flags the selector with its evidence and does not edit the candidate.

### Item 3 — the license box's license-absence entries (judgment call, recorded)

The original states no license for its two images anywhere (its only license text is the banner's "CC BY-SA 3.0" for the theme code itself). The appended license box (candidate L625–638) therefore records, for each image, ライセンス: 原語版に記載なし — "not stated in the original version" — with the parenthetical that the original page carries no license statement and the author should be confirmed with before posting. The alternative (copying the theme code's CC BY-SA 3.0 onto the images) would have invented a license the author never stated; the box documents the absence instead, which is the KB-60 form-uncertainty discipline applied to content. A reviewer can re-derive the absence from this package's original.txt: no license statement for back.png or logo.png exists in it.

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-CREDITBTN item 1 — KB-11 selector correction (landing 1db8300, 2026-11-17).** `FIX-CREDITBTN.md` records that the JP credit component emits the anchor as a direct child of `.creditButton`, so the inherited `.creditButton p a` selector cannot match. Commit 1db8300 changed candidate L512 from `.creditButton p a {` to `.creditButton > a {` (the in-place, declaration-block-untouched form of theme:sodium-jp); no declaration moved. T1 before/after identical (4/1/1).

**FIX-CREDITBTN item 2 — base-work contributor adjudication (no edits).** `FIX-CREDITBTN.md` item 2 adjudicates Denevola as STANDING. The adjudication loci are the candidate's authorship banner (L66–67, `Created by c_bonefish` / `Base Code by Denevola`, verbatim from the original L66–67) and, in the credit apparatus, the 著作権者 field (L16) and license-box `author=` (L626) naming c_bonefish. Denevola is a base-code contributor, not a theme co-author, so naming the theme author alone in the field is correct; the existing record item that calls this a gap described the package as built and is closed by this adjudication, with no candidate edit.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-mr-reprisal-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 복수 씨 CSS 테마
- **Author:** c_bonefish
- **Source:** https://scpko.wikidot.com/theme:mr-reprisal — revision 13
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
