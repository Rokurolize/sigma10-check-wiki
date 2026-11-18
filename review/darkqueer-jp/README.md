# Review package — theme:darkqueer-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:darkqueer-jp — origin EN, population #77 [GOSIGN2-LEDGER (b) row 77]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 77]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 77; GOSIGN2-LEDGER (b) row 77]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — footer nav "Powered by Wikidot.com"/links illegible on near-black at every width/engine (theme's dark palette) + 375px license line clipped; hidden-rate contradicted by eye; 382–428px sample overflow; `url-https//` 404 = migration infra. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 77, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 77]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 77]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:darkqueer-jp.txt sha256:b3edc2135fc435a020dc2b97a9e40339fc9b660eda7edf5de7282f3286be0e55; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 77) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (ii), section 11); the render row's items (KB-34 family; KB-50; KB-33/KB-34; migration infra, section 11); T4's P1 and P11 (section 11). The credit fields were **FIXED** by the credit waves. No usage-example defect: the install example already names theme:darkqueer-jp, and the header is translated (the batch's counter-example to the kept-English headers) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:darkqueer | theme:darkqueer-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 23 (first translation; the candidate's credit block records 初訳時参照リビジョン: 23) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:darkqueer-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 526 lines / 12,052 bytes | 544 lines / 14,146 bytes |
| SHA-256 | 7e66790da7c3a70fd85c77782a29f4a466b0aa1f4706d042043881cd8c358f32 | b3edc2135fc435a020dc2b97a9e40339fc9b660eda7edf5de7282f3286be0e55 |

Wave history: the candidate was created by the Stage 2 EN7 integration (commit 331ab7e) and last touched by FIX2-CREDIT (commit 666f543, the credit-missing-fields completions over 36 themes). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. Layering note: darkqueer is a layer over the blankstyle theme; this package's diff covers the darkqueer layer and its base include, not the base theme's own port.

## Summary

A dark pride layer over Blankstyle. The port repoints the base include itself — the original's live `:scp-wiki:theme:blankstyle` include becomes `:scp-jp:theme:blankstyle` (candidate L2), naming the production JP page for the base (probed for this package, 2026-11-17: 200) — adds the interwiki frame at the head, installs the preview credit block with the eight ruling-3 fields, deletes the original's live Rate, and translates the prose and exhibits (46 translation blocks, mostly one-line specimens). Two choices distinguish it inside this batch: the header variables are translated (SCP Foundation → SCP財団, candidate L250–251), where derby-jp and cleaning-services-jp keep theirs in English under ruling 2 — both are legitimate under the ruling, and the difference is recorded so it reads as taste exercised, not inconsistency discovered; and the tail self-delivery import the original already carried is kept in place and moved to the draft host (candidate L543). Measured churn (diff.md: +108/−95, 203 changed lines in 52 change blocks / 7 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 52 change blocks — 17 specific (32.7%), 35 heuristic (67.3%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 37 |
| TRANSLATION-ANCHORED | 9 |
| INCLUDE-REPOINT | 4 |
| DRAFT-HOST | 4 |
| SELF-DELIVERY | 2 |
| LINK-REPOINT | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 1 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| COMPONENT-SWAP | 1 |
| HEADERVAR | 1 |
| DELIVERY-HOST | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic two-thirds is the one-line exhibit translation mass, the expected class M shape for this page. The two EXHIBIT-RESTRUCTURE labels are the standing false-fire shape (repoints inside exhibit regions); the census of section 8 decides. There is no residue. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:darkqueer-jp; original theme:darkqueer on scp-wiki at reference revision 23; candidate `pages/theme:darkqueer-jp.txt`. Provenance route: derived from the original at the reference revision, as a layer over blankstyle (no production JP counterpart for the darkqueer layer itself, so the R4 adoption question does not arise for this layer; the base's production page is a different matter, section 3).
- **Why:** Section 0 declares the provenance route and the layering so every later count is read against the right baseline.
- **Verify:** The sources.tsv row for darkqueer-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L50–59 with bare includes, carrying the eight ruling-3 fields: title Darkqueer Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Darkqueer Theme; 著作権者 Queerious; 作成年 2024; 初訳時参照リビジョン 23; the source link (candidate L58) naming scp-wiki.wikidot.com, the original's recorded host. The original's live `[[module Rate]]` (original L46) is deleted (BARE-RATE-DEL): the preview block is rate-bearing, and a kept Rate is the KB-09 duplicate. The localize lane's P1/P3 items (LOCALIZE-ROWS row 77) describe the pre-completion state; FIX2-CREDIT completed the fields, and the ledger records P3 as FIXED and P1 as DISPOSITIONED (posting-procedure convention class). No T7 credit-module CSS supplement exists in this layer.
- **Why:** P3/T1 and ruling 3; KB-09 for the duplicate the deletion prevents.
- **Verify:** `grep -n 'module Rate\|module rate' candidate.txt` returns nothing; read candidate L50–59 against the eight fields.
- **Disposition:** FIXED (P3, FIX2-CREDIT); P1 DISPOSITIONED (section 11).

### 2. Includes and components

- **What:** The base include (section 3), the frame pair, the credit pair (section 1), and the theme-squares include repointed to `:scp-jp:` (candidate L76, B9). The usage examples are both correct: candidate L70 names the base in bare form (`@@[[include theme:blankstyle]]@@`, the production page's name) and candidate L71 names `@@[[include theme:darkqueer-jp]]@@`, this candidate's own posting name — the batch's usage-example defect does not apply.
- **Why:** P1 (KB-15) for the live includes; the usage examples under the campaign's settled rule (AGENTS.md §6), satisfied here.
- **Verify:** `grep -n '\[\[include' candidate.txt` — no `:scp-wiki:` include remains.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The original's own delivery mechanism is a live page include of its base: original L2 includes `:scp-wiki:theme:blankstyle`. The candidate repoints that include to `:scp-jp:theme:blankstyle` (candidate L2, B1) — the production JP page for the base, which exists (probe above) — keeping the original's include mechanism with its target on the JP side. (This is a page include, the theme's own composition form, not a compiled-CSS delivery; the delivery rulings for CSS imports do not change its treatment.) The candidate adds the interwiki-style frame at the head (candidate L5–7) naming its own /1, and keeps the original's tail self-delivery import, moved from the EN wdfiles host to the draft host (candidate L543, B52; SELF-DELIVERY ×2, DELIVERY-HOST ×1).
- **Why:** P1/P4: a layer theme composes over its base's JP page, never over the raw upstream delivery (the cross-theme dependency rule); P6/T3 for the frame. The draft-host form is KB-41, class (iii).
- **Verify:** `sed -n '1,8p' candidate.txt`; `grep -n 'wdfiles' candidate.txt` — draft host only.
- **Disposition:** DISPOSITIONED (class (iii) for the draft-host line).

### 4. Fonts and assets

- **What:** Fonts: none in this layer — no font load and no stack blocks on either side; the composed page's typography comes from the blankstyle base (the T5-absent shape for a layer). Assets: the pride logo gp_logo.svg moves to the draft host in both its uses — the image-block exhibit's name (candidate L109, B10) and the CSS background (candidate L274) — with the remaining DRAFT-HOST blocks moving the layer's other asset URLs the same way, file names unchanged.
- **Why:** P5/KB-17 (asset hosts), in the class (iii) draft-host form.
- **Verify:** `grep -n 'gp_logo' candidate.txt` — candidate L109 and L274, both draft-host.
- **Disposition:** DISPOSITIONED (class (ii)/(iii) family).

### 5. Header, sidebar, and site furniture

- **What:** The header variables are translated (B50, HEADERVAR): `--header-title: "SCP Foundation"` → `"SCP財団"` (candidate L250) and `--header-subtitle` → `"確保、収容、保護"` (candidate L251). This is ruling 2 exercised in the other direction from derby-jp and cleaning-services-jp: header language is translation taste, and this porter translated. Neither choice is a migration defect, and the ledger's PASS covers this theme with the translation in place. No P8 layout adaptation was needed.
- **Why:** P9, with ruling 2's settlement stated so the batch's two header treatments read as the same rule, not a contradiction.
- **Verify:** `grep -n -- '--header-' original.txt candidate.txt` — the two lines, translated.
- **Disposition:** Standing (applied translation; ruling 2 covers either choice).

### 6. Text translation

- **What:** The prose and exhibits are translated throughout (TRANSLATION-ANCHORED ×9, TRANS-UNANCHORED ×37, CREDIT-PROSE ×1). The localize lane's T5 note (English tab labels standing in the exhibits, LOCALIZE-ROWS row 77) records the specimen layer: the tab specimens demonstrate the theme's tab styling with their labels as specimens, and the item stands as the lane recorded it within its joint T4/T5 findings, all dispositioned at the ledger.
- **Why:** P10 (body and usage translation); the specimen ground for exhibit labels.
- **Verify:** A CJK scan of candidate.txt outside the credit block's 原題 field returns translated text and the recorded specimens.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L58) names scp-wiki.wikidot.com, the original's recorded host — the host check passes. The prose's base link becomes an internal link to the production base page (`[[[theme:blankstyle|BLANKSTYLE]]]`, candidate L61, B4), and the pride-highlighter component link is kept in bare form (`[[[component:pride-highlighter|...]]]`, candidate L62–63, B5) — the campaign's own component page name. The localize lane's P11 item (the Queerstyle EN link notation) is dispositioned at the ledger (sibling/batch-posting class family for link notations pointing at pages outside this theme's record).
- **Why:** P11: prose links take the JP counterpart or the serving original.
- **Verify:** `grep -n 'wikidot.com\|\[\[\[' candidate.txt` — the source link and the two prose links above.
- **Disposition:** Standing; P11 DISPOSITIONED (section 11).

### 8. Structure

- **What:** The closing rule holds inside the layer's CSS: selectors, rule order, and variable names are preserved; the internal changes are the section-4 asset lines and the section-5 header values. Exhibit census (R3): the original's exhibits (usage, image specimen, tab specimens, license tail) all survive in the candidate in the same order; the two EXHIBIT-RESTRUCTURE labels sit on repoint blocks inside exhibit regions and are discharged on that ground. The only deletion is the live Rate of section 1.
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape.
- **Verify:** Compare the exhibit sequence in original.txt against candidate.txt.
- **Disposition:** Standing; no structural deletion beyond the recorded furniture fix, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added by the porter — the candidate carries no `[!-- ... --]` translator notes and no editor line (checked explicitly). The CSS comment at candidate L232 (the pride logo's attribution line, naming its source page) is the original's own comment, present at original L214 and carried over in place — an inherited attribution, not a porter annotation.
- **Why:** R2: porter-added text is part of the change record; an inherited comment is distinguished from an annotation by exactly this check.
- **Verify:** `grep -n 'White Outline' original.txt candidate.txt` — the comment on both sides.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three pseudo-ref errors: class (ii), posting-procedure — the draft-host lines of sections 3–4. (2) The render row's items: the footer nav's illegibility on the theme's near-black palette and the clipped 375px license line (KB-34 family — the theme's own dark styling at small widths, recorded as the cross-cutting family records it); the hidden-rate item (KB-50: the sample's rate display contradicted the hidden-rate expectation on the lane's visual check); the sample overflow at 382–428px (KB-33/KB-34); and the url-https// 404, which is migration infrastructure, not a page property. (3) T4's P1 and P11: DISPOSITIONED (posting-procedure convention class; the link-notation item), sections 1 and 7.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; infrastructure failures are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–3); P3 FIXED (section 1).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 77): exit 1, 3 errors / 2 warns / 1 info; all three errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-B (EN7)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 77): FINDINGS jointly, display-affecting findings 3 — the credit item FIXED afterwards (section 1), the rest dispositioned in section 11(3). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +108/−95 in 52 change blocks / 7 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:darkqueer-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 77; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-darkqueer-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The base theme (theme:blankstyle on production, theme:blankstyle-jp as a candidate) has its own package; nothing in this theme's record edits it. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Darkqueer Theme
- **Author:** Queerious
- **Source:** https://scp-wiki.wikidot.com/theme:darkqueer — revision 23
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
