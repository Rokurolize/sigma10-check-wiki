# Review package — theme:alexylva-university-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:alexylva-university-jp — origin EN, population #54 [GOSIGN2-LEDGER (b) row 54]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now a8c674c1a328c3fe161d2b7c86ec53c11a9ee18e5691b32b3b2b2e6efab1fe06); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 0 infos (hotlink×5); standing classes dispositioned in register c1 [T1-ROWS row 54; GOSIGN2-LEDGER (b) row 54]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent header collision/clip at 320 (wordmark overlaps logo and 検索, tagline clipped); "+" contrast 1.16 washed-out rate token (theme design). [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 54, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 54]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 54]
- Computed against: canonical commit 5d951775998e4a1eeccf8e8695a6518b328962ee; candidate file pages/theme:alexylva-university-jp.txt sha256:a8c674c1a328c3fe161d2b7c86ec53c11a9ee18e5691b32b3b2b2e6efab1fe06; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 54) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×5 (class (ii), the EN local--files asset URLs); the render row's items (the 320px header collision family, KB-35; the "+" contrast token, KB-39 false-positive class) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:alexylva-university | theme:alexylva-university-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 79 (first translation; the candidate's credit block records 初訳時参照リビジョン: 79) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-alexylva-university.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:alexylva-university-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 281 lines / 6,340 bytes | 289 lines / 6,814 bytes |
| SHA-256 | 512c7031f11f97dd3c000e538ebf6694128c4dfbb3c4e0020b7bcfc0c937254c | c2c1ef80a5609bfd92ff753ee995dc8cf1edb1e5e872ce7d30fe0c3033949a1c |

Wave history: the candidate was created by the Stage 2 EN batch 1 port (3205f27, 2026-11-15) with the credit block, the porter intro line, and the CSS already in its inline module form, but without any interwiki-style frame (the original's EN frame was not carried over). Exactly one wave then edited it: FIX2-COLON (f931619, 2026-11-17), whose title names only its colon fix but which in this file also added the JP interwiki-style frame, normalized the translator field to AI, and made the JP font load and stack insertions (per-theme record). No FIX5 commit touches this file.

## Summary

A small, single-layer university theme (a Sigma-9 derivative) whose port is close to minimal: the CSS body moves from the original's `[[code]]` block into an inline `[[module CSS]]` (similarity 0.939 by the classifier's topology pass) with its banner comment and asset URLs intact, the bare Rate is replaced by the preview credit block, and the one wave that touched the file supplied the frame and the Japanese font support the port had left out — the two things T4 had charged (patterns 6 and 7). Measured churn (diff.md, the generator's count: +42/−34, 11 hunks, 20 change blocks). The flagged items are the credit author field naming the theme's cleaner rather than its creator (per-theme record, the same shape as alcur's) and the "GO VISIGOTHS!" header string standing in English (section 5).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 20 change blocks — 19 specific (95.0%), 1 heuristic (5.0%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 11 |
| JPFONT-STACK | 7 |
| TRANS-UNANCHORED | 4 |
| WS-ONLY | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COLON-ENC | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the 11 DELIVERY-MOVE blocks are the code→module relocation of the CSS body, narrated once in section 3 rather than block by block; the 7 JPFONT-STACK blocks are the FIX2-COLON wave's font-stack insertions (section 4); the 2 EXHIBIT-RESTRUCTURE blocks adjudicate in section 8 (the head furniture swap and the body-line replacement); the single heuristic block (B5) is the body line's replacement, resolved in section 6. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:alexylva-university-jp; original theme:alexylva-university on scp-wiki at reference revision 79; candidate `pages/theme:alexylva-university-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart exists, so R4 does not arise; the original has since been superseded upstream, and the follow-up delta is a campaign-record artifact noted in sources.tsv, not part of this package's diff). The frame: the original opens with a self-delivery module and an EN interwiki-style frame (original L1–8); the candidate opens with the JP frame alone (candidate L1–4), the gate, and the credit block.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the frame's history (dropped at the port, restored by the wave) is section 3.
- **Verify:** The sources.tsv row for alexylva-university-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L13) and the banner comment inside its code block (original L21–28: "Created by Uncle Nicolini, cleaned by ROUNDERHOUSE", with the logo and texture CC attributions). The candidate deletes the bare Rate (BARE-RATE-DEL) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying the eight ruling-3 fields （タイトル: アレクシルヴァ大学テーマ; 翻訳責任者: AI; 翻訳年: 2026; 原題: Alexylva University Theme; 著作権者: Rounderhouse; 作成年: 2019; 初訳時参照リビジョン: 79; 元記事リンク: the scp-wiki original), present from the port's creation except the translator value, which FIX2-COLON normalized from SCP-JP to AI. The banner comment is retained verbatim inside the candidate's module (candidate L29–36), original typos included ("CC BA SA 3.0" is the original's own text). One value-level point was flagged at review and has been repaired: T4 charged that the credit 著作権者 dropped Uncle Nicolini, the original's creator; as first built, the field named Rounderhouse alone (the cleaner named second in the banner), with the creator's name surviving in the retained banner comment. Canonical commit 09d48cb corrects the field to Uncle Nicolini & Rounderhouse, and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict, as jiha's does). The ledger adjudicates P3 FIXED on field completeness (the eight fields present, checker-verified). There is no license box on either side and no T7 credit-module CSS: the theme never styled the credit module and no supplement adds any.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields. The author-field point is recorded under the attribution evidence standard: the package states what the bytes carry and what the ledger's FIXED covers, so a reviewer can see both (the same shape as the alcur package's flag, recorded there too).
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L8–17 against the eight fields and L29–36 for the banner; compare against original L21–28.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified). The Uncle Nicolini value point is flagged in the per-theme record.

### 2. Includes and components

- **What:** The candidate's includes are three: the interwiki-style frame (section 3) and the credit pair (section 1). The original's one component include was its EN interwiki-style frame (`:scp-wiki:component:interwiki-style`, original L5–8), a COMPONENT-SWAP in the classifier's terms: the JP form of the same component, with its `theme=` repointed from the original's own /1 on scp-wiki to the candidate's own /1 on the draft host. The usage exhibit's include names the candidate itself (candidate L21). No foreign include is kept in a live position.
- **Why:** P1 (KB-15): a live include must name the JP counterpart that exists; interwiki-style is a shared component whose JP form is the environment's own. Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three includes, all `:scp-jp:` forms.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers by a live self-import (`local--code/theme%3Aalexylva-university/1` from scp-wiki.wdfiles.com, original L2) plus the EN frame naming the same /1, with the CSS body in a `[[code]]` block (original L20–280). The candidate delivers by the JP frame naming its own `local--code/theme%3Aalexylva-university-jp/1` on the draft host (candidate L1–4), with the CSS body inline in a single `[[module CSS]]` (candidate L25–287) — the classifier's topology pass matches the moved body at 0.939 similarity, the difference being the wave edits of section 4 and the banner's retention. The frame's arrival is a wave fix, not the port's shape: the port dropped the original's frame outright (T4's pattern-6 charge: interwiki-style missing), and FIX2-COLON restored it in JP form. The self-import module was dropped at the port and not restored; the inline module is the candidate's delivery form in this composition, as it is for the sibling alcur candidate.
- **Why:** P6/T3 (the interwiki-style frame is the environment's delivery contract; priority 1 is the theme's own layer, there being no base under this single-layer theme — the body's 基盤： 単体 line is accurate). P4/T9 for the /1 address's host (draft host at draft stage, KB-41 class (iii)).
- **Verify:** `grep -n 'local--code' candidate.txt` — the frame's theme= line only; `grep -n '\[\[module\|\[\[code' candidate.txt` — one module, no code block.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P6 FIXED, frame waves, checker-verified); the draft-host form of the frame's address is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Loads: the theme's display faces (Oswald, GFS Neohellenic) load from fonts.googleapis.com on both sides (the original's own imports, carried over). The JP load is the wave's: FIX2-COLON added the Noto Sans JP `@import` at the module's head (candidate L27) and inserted `"Noto Sans JP"` into seven `font-family` stacks (the 7 JPFONT-STACK blocks: the two Stardos Stencil stacks, four Oswald stacks, and the GFS Neohellenic stack — candidate L50–180 region, each a one-token insertion with the rest of the line unchanged). Assets: five lines name EN-host local--files URLs — the logo (candidate L50), header2.png (L80), igf22s1.webp (L88, its `theme:` colon-encoded by the same wave, the COLON-ENC block), 4.jpg (L157), and 3.jpg (L167) — the T1 hotlink ×5 and T4 pattern-5 set (four live links plus the banner comment's deviantart references counted by the lane). None was re-hosted.
- **Why:** P7/T5 with KB-16: the Latin-only stacks cannot render Japanese, so the load and every stack insertion arrive together; that they arrived by wave rather than at the port is T4's pattern-7 charge, recorded FIXED in the ledger. P5's asset rule meets its standing disposition: the original's own asset hosts kept as original state, class (ii) / KB-58 (re-upload barred by owner order; posting rewrites or re-hosts). KB-01 for the colon encoding (an unencoded colon in a URL path is a class (i) form error; the wave's fix is the encoding, not a re-host).
- **Verify:** `grep -n 'font-family' candidate.txt` — seven stacks carry Noto Sans JP; `grep -n 'local--files' candidate.txt` — the five lines above.
- **Disposition:** Font load and stacks FIXED (GOSIGN2-LEDGER §(c3): P7 FIXED, font wave); assets DISPOSITIONED (same line: P5, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** No P9 variable override: the theme sets no `--header-title`/`--header-subtitle`/`--logo-image` of its own (its header is the Sigma-9-derived furniture inside the CSS body, carried over). The one header-language item is the CSS `content:` string `"GO VISIGOTHS!"` (candidate L63; original L56, byte-identical), the university's slogan rendered as the header's tagline string. T4's row charged it as a T5 item (header subtitle left in English). No sidebar or topbar rule was structurally adapted.
- **Why:** KB-18 makes a `content:` string reader-visible text, so the string is recorded here rather than passed over; the standing disposition for header language is ruling 2 (header and title language is translation taste, out of scope for migration correctness), and a slogan — the fictional university's team cry — is the clearest case of it. The ledger's c3 line for this theme records no header charge.
- **Verify:** `grep -n 'GO VISIGOTHS' candidate.txt original.txt` — the same line on both sides.
- **Disposition:** DISPOSITIONED (ruling 2; the string is the original's own, byte-identical).

### 6. Text translation

- **What:** The body text is three lines, and one of them is a replacement, not a translation (the heuristic block B5): the original's intro ("This is a theme for the [[[alexylva-university-hub|Alexylva University]]] GoI. To use this theme, put the following on any page:", original L16) becomes a porter-written description ("Alexylva大学の学術的な雰囲気を表現したテーマです。", candidate L19) plus the campaign's standard usage and base lines (candidate L21–23), which name the candidate itself. The original's hub link is not carried over (section 7). Inside the CSS, the reader-visible strings are the section 5 slogan and the banner comment (retained in English as the original's attribution record, section 1); the CSS section comments (/* FONTS */ and its siblings) stand in English on both sides — porter-visible R1 candidates that the port left untranslated, recorded here so the census is complete. The 4 TRANS-UNANCHORED blocks are the intro replacement, the usage/base lines, and the gate-region lines.
- **Why:** P10 for the usage text; the intro replacement is R3-adjacent (a body line replaced rather than translated) and is adjudicated in section 8. R1's comment half is, per the taxonomy's feedback disposition, a known non-finding shape (porter-visible only); it is disclosed, not charged.
- **Verify:** Read candidate L19–23 against original L16–18; the banner and comments are candidate L29–40.
- **Disposition:** Standing (the port itself); the intro replacement is recorded in section 8.

### 7. Links

- **What:** The candidate's one live outbound prose link is the credit block's source link (candidate L16), naming `https://scp-wiki.wikidot.com/theme:alexylva-university` — the original's own host, exactly as recorded in review/sources.tsv (original_url); no host discrepancy to probe. The original's one body link, the Alexylva University hub link inside its intro sentence, was not carried over when the intro was replaced (section 6); there is no JP hub page named in any campaign record for it to repoint to, and the candidate's usage line names the theme itself. The banner comment's two deviantart URLs (logo and texture sources) stand as the original's attribution record on both sides.
- **Why:** P11: prose links take the JP counterpart where one exists; where the sentence carrying the link was itself replaced and no counterpart is recorded, the package states the drop rather than inventing a target. The dead-reference standard is met by disclosure: the hub link's absence is a fact of the candidate a reviewer can weigh, recorded here and in section 8.
- **Verify:** `grep -n 'wikidot.com\|deviantart' candidate.txt` — the source link, the asset hosts of section 4, and the banner's two URLs.
- **Disposition:** Standing for the source link; the hub link's non-carriage is recorded as part of the section 8 adjudication.

### 8. Structure

- **What:** The closing rule holds for the CSS: selectors, variable names, and the body's internal order are preserved through the code→module move, and the JP additions arrive as the head frame and credit block, not interleaved. The 2 EXHIBIT-RESTRUCTURE blocks adjudicate as follows: the first is the head furniture swap (the self-import module and EN frame out, the JP frame and credit block in — sections 1–3, furniture, not exhibits); the second is the body region, where the original's three body lines (intro with hub link, usage exhibit) become the candidate's three body lines (porter intro, usage, base note). No exhibit census question arises inside the CSS: the theme has no tabview/code exhibits of its own beyond the CSS body itself, which is carried entire. The one genuine replacement is the intro sentence, recorded in section 6: a one-line descriptive replacement for a one-line original whose only distinctive content was the hub link; the ground is the campaign's candidate body form (description + usage + base lines, the same three-line shape as the alcur candidate), and no ledger row charged it.
- **Why:** R3 exists to force this adjudication; here the census decides: nothing structural was dropped, and the single replaced line is named with its ground.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code\|\[\[include' original.txt candidate.txt`; read the body lines on both sides (original L16–18, candidate L19–23).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Three WS-ONLY blocks (whitespace-only pairs, in the carried-over CSS and at the module boundary) and no re-indentation (0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary in classification.json (WS-ONLY ×3; reindent_blocks: 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter text: the intro line (candidate L19), a porter-written description with no original counterpart, counted in section 6 and adjudicated in section 8. There are no `[!-- --]` translator notes, no editor line, and no porter comment in the CSS (the banner comment is the original's own, section 1).
- **Why:** R2: porter-added text is part of the change record, and this one replaces original text, which is why it is held to the section 8 standard rather than merely listed.
- **Verify:** Read candidate L19 against original L16.
- **Disposition:** Standing (recorded; its replacement character is section 8's adjudication).

### 11. Dispositions and exceptions

- **What:** Three groups, each with its ground. (1) T1's standing class: hotlink ×5, class (ii) — the five EN local--files asset lines of section 4, kept as original state under KB-58. (There is no pseudo-ref: the candidate's one delivery reference is its frame's draft-host address, class (iii).) (2) The render row's items: the candidate-inherent header collision/clip at 320 (the wordmark overlapping the logo and the search control, the tagline clipped), dispositioned as the narrow-width header clip/collision family (KB-35 family; FIX3-S2EN §6.5 observations) — a render-side difference class; and the "+" contrast 1.16 washed-out rate token, a machine contrast value the T3 walk did not confirm as a defect (KB-39: machine contrast warns include false positives on themed surfaces; the row itself records it as theme design). (3) T4's charges as adjudicated: P3 FIXED (with the value point flagged in section 1), P5 DISPOSITIONED (class (ii) / KB-58), P6 FIXED, P7 FIXED.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 class is register c1 of GOSIGN2-LEDGER, the render items are the theme's c2 block.
- **Disposition:** DISPOSITIONED (all three groups); the section 1 value point is flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 54): exit 1, 5 errors / 1 warn / 0 infos; all five errors are hotlink, the standing class of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 54, LOCALIZE-S2-A): FINDINGS jointly, display-affecting findings 1; the row's own closing note records the translation text itself as unproblematic （翻訳文そのものは問題なし); the ledger §(c3) line records P3 FIXED, P5 DISPOSITIONED, P6 FIXED, P7 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +42/−34 in 20 change blocks / 11 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:alexylva-university-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 54; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The wave history, edit by edit

The ledger names this theme's wave outcomes at class level (§(c3): P3 FIXED, P5 DISPOSITIONED, P6 FIXED, P7 FIXED). The bytes give the edits, and they are all in one commit:

1. **FIX2-COLON (f931619, 2026-11-17).** Its colon content in this file is one line: the `theme:alexylva-university` path in the igf22s1.webp URL colon-encoded to `theme%3Aalexylva-university` (KB-01). The same commit also: added the interwiki-style frame at the head (the P6 restoration — the port had dropped the original's frame, and T4 had charged the absence); normalized the translator field SCP-JP → AI (the credit waves' population form); added the Noto Sans JP `@import`; and inserted the JP face into all seven font-family stacks (the P7 fix T4 had charged as 和文フォント無し — no Japanese font). Four of the ledger's five outcomes for this theme were delivered by a commit whose title names only the fifth's smallest part. A reader who trusts the commit title will miss the frame and the fonts entirely; the package record follows the diff.

### The credit author field

T4's pattern-3 charge for this theme is that the credit 著作権者 drops Uncle Nicolini, the original's creator ("Created by Uncle Nicolini, cleaned by ROUNDERHOUSE", in the banner comment both sides carry). The verdict (P3 FIXED) is a field-completeness judgment: the eight ruling-3 fields are present and checker-verified. The bytes show the value naming Rounderhouse alone. Unlike the alcur case, the mitigation here is in the same file's most-read position: the banner comment at the head of the delivered CSS names both men in their roles, so the creator's credit survives in the delivered artifact itself, not only in a license parameter. The package records the difference so the judgment is visible either way. The repair has since landed (canonical commit 09d48cb): the field now reads Uncle Nicolini & Rounderhouse.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-alexylva-university-jp.txt` is the decoration sample stub the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file (the theme is single-layer, 基盤: 単体), and no inbound-link repairs in other candidates for this theme.
