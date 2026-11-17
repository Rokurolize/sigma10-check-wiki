# Review package — theme:ashes-to-ashes-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ashes-to-ashes-jp — origin EN, population #59 [GOSIGN2-LEDGER (b) row 59]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7ddb45d1401652f446d60077ef3222c8f4eb436c684cbf3edb4461d8e3f01870); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 0 infos (hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 59; GOSIGN2-LEDGER (b) row 59]
- T2/T3 (render, combined verdict): PASS-WITH-NOTES — [combined T2/T3] report `NO candidate-specific defect beyond cross-cutting X2/X3/X5/X7` — only borderline license legibility (observation); no BLOCKED-ENV. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 59, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 59]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 59]
- Computed against: canonical commit 2aee8616594f39690b137601f242125d8376cc07; candidate file pages/theme:ashes-to-ashes-jp.txt sha256:7ddb45d1401652f446d60077ef3222c8f4eb436c684cbf3edb4461d8e3f01870; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 59) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 (original-state asset URLs, section 11); P4/P5 delivery and asset classes (section 11). **FLAGGED by this package** — the header font named in `--header-font` is loaded nowhere in the candidate, and the candidate contains no BHL base delivery (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ashes-to-ashes | theme:ashes-to-ashes-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 8 (first translation; the candidate's credit block records 初訳時参照リビジョン: 8) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-ashes-to-ashes.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ashes-to-ashes-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 211 lines / 5,694 bytes | 154 lines / 3,922 bytes |
| SHA-256 | 10ff775e828cfe51a3d46f3f114532cda64d2bf834d1a53ccf92080e69a62349 | 4d2e6ca0d9f34e6dcf0f54d44d940aa6a1e2107b16a82d5050cc3b57183cca66 |

Wave history: the candidate was created by the Stage 2 EN batch 1 integration (commit 3205f27) and has exactly one later commit, f931619 (FIX2-COLON, unencoded-colon URL fixes over 18 themes), which is the stamp's computed-against commit and the source of the three colon encodings in section 4. The original has been superseded upstream since revision 8; the follow-up diff artifact `diff-ashes-to-ashes-from8.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A Black Highlighter override theme built for Yoshihide's Proposal (Public Domain Contest 2025): the original pairs a BHL base delivered by GitHub Pages @imports with a single override CSS module, and closes with a long English demonstration body (story quote, usage prose, syntax exhibits) behind a second tag gate. The candidate keeps the override module nearly intact — its only CSS edits are the font load, one font stack, and three colon encodings — and rebuilds everything around it: the BHL import head is deleted, the frame and credit block are added at the head with three compressed JP prose lines, the two EN BHL furniture includes are removed, and the demonstration body and its bare Rate module are dropped. Measured churn (diff.md, the generator's count: +27/−82 in 9 change blocks / 6 hunks) understates the structural change, because the override CSS (the bulk of the file) is carried over almost line for line. Two items are flagged in the per-theme record: the header font the candidate names is not loaded anywhere in it, and the candidate contains no delivery of the BHL base its prose declares.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 9 change blocks — 7 specific (77.8%), 1 heuristic (11.1%), 1 residue (11.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| IFTAGS | 3 |
| COLON-ENC | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| BARE-RATE-DEL | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic CSS-BODY block is a P7 font-stack rewrite (section 4); the residue block is a single blank line (section 9); the two EXHIBIT-RESTRUCTURE primaries split — B2 is the head furniture swap (sections 1–2), and B9 is a genuine exhibit-body deletion, adjudicated in section 8 with its ground. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ashes-to-ashes-jp; original theme:ashes-to-ashes on scp-wiki at reference revision 8; candidate `pages/theme:ashes-to-ashes-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch 1 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved to the head: the original opens with a tag-gated head module carrying the BHL @imports (original L1–6) and closes with a second tag gate around its demonstration body (original L143); the candidate opens with the frame include (candidate L1–4) and a single gate around the whole page (candidate L6).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3), and the head module's deletion is P4 (section 3).
- **Verify:** The sources.tsv row for ashes-to-ashes-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original carries no credit block at all: no credit include, no license entries; its only credit-shaped furniture is the bare `[[module Rate]]` centred in the tail gate (original L145–147), which the candidate deletes with the tail body (block B9). The candidate installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–18) carrying all eight ruling-3 fields (title 灰から灰へテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Ashes To Ashes Theme; 著作権者 Yossipossi; 作成年 2025; 初訳時参照リビジョン 8; the source link, section 7). The fields were present from the file's creation commit; no credit wave needed to complete them. There is no license box on either side (the original had none, so the T4/KB-63 dropped-box shape does not arise).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module Rate\|license-box' candidate.txt` returns nothing; read candidate L8–18 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified — for this file the form arrived at creation).

### 2. Includes and components

- **What:** The original's two EN furniture includes, `:scp-wiki:component:toggle-sidebar-bhl` and `:scp-wiki:component:centered-header-bhl` (original L8–9), are deleted (block B2, COMPONENT-SWAP label); nothing replaces them one-for-one, because the JP environment supplies its own header and sidebar furniture and the BHL component pair has no place in the JP candidate. The candidate's includes are the frame (section 3) and the credit pair (section 1); its one usage line is exhibit text naming the candidate itself in bare local form (`@@[[include theme:ashes-to-ashes-jp]]@@`, candidate L21). Every include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15) governs repoints; a deletion is the right outcome where the included furniture belongs to the foreign base's page furniture rather than to the theme — keeping either include would be a foreign-include error, class (i). Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its base by a tag-gated head module (original L2–5): `@import`s of BHL normalize and black-highlighter from `nu-scptheme.github.io`. The candidate deletes that module outright (block B1) and adds the frame the original lacked: an interwiki-style include at the head (candidate L1–4) with `priority=1` and `theme=` naming the candidate's own `local--code/theme%3Aashes-to-ashes-jp/1` on the draft host. **Frame paragraph (the M-frame addition):** the frame is the single-layer own-code form — priority 1 is the theme's own layer — and there are no base layers in it: no priority 2/3 entries, no JP BHL theme include, and no BHL @import anywhere in the candidate, although the candidate's own prose declares **基盤:** BHL（インライン） (candidate L23). The ledger records the frame outcome as P6 FIXED (frame waves; checker-verified). The base-delivery question this raises is flagged in the per-theme record.
- **Why:** P6/T3 for the frame; P4/T9 for delivery sources generally — the campaign's BHL form, visible in this batch's theme:doap-bhl-jp, delivers the base through the JP BHL theme include with the own layer at priority 3, which is the comparison the flag rests on. The draft-host form of the theme= URL is KB-41, class (iii).
- **Verify:** `grep -n 'github.io\|Black-Highlighter\|interwiki-style' candidate.txt` — the frame line only; compare theme:doap-bhl-jp's head in `pages/`.
- **Disposition:** FIXED (P6, frame waves) for the frame itself; the base-delivery gap is FLAGGED (per-theme record), not silently passed.

### 4. Fonts and assets

- **What:** Font load (block B3, JPFONT-LOAD): the original's two bunny.net @imports (`Protest Revolution`, `Fredericka the Great`, original L13–14) are deleted, and the candidate loads one family from Google Fonts at the head of its CSS module (candidate L26): Noto Sans JP (400;700). Stack (block B4, the heuristic CSS-BODY block, adjudicated here as the standing lesson directs): the `--header-font` value gains the JP face in second position — `'Fredericka the Great', 'Noto Sans JP', Times New Roman` (candidate L69) — a P7 font-stack rewrite, not a body-CSS change. `Protest Revolution` was loaded by the original but referenced by no stack in it, and is simply gone. `Fredericka the Great` is still named first in the header stack but is loaded nowhere in the candidate — flagged in the per-theme record. Assets (blocks B5–B7, COLON-ENC): the three background images (fire.webp candidate L85, bamboo.webp L102, parchment.webp L116) keep the original's host and folder (`scp-wiki.wikidot.com/local--files/theme:ashes-to-ashes/`) with only the colon encoded (`theme:` → `theme%3A`), the KB-01 form, executed by FIX2-COLON (f931619).
- **Why:** P7/T5 with KB-16 for the JP load and stack (Japanese header text needs a JP-capable face in the stack); KB-01 for the colon encoding (an unencoded colon in a local--files URL is the checker's unencoded-colon class); P5/KB-58 for the assets' hosting state, which the ledger dispositions rather than fixes (section 11).
- **Verify:** `grep -n '@import\|Fredericka' candidate.txt` — two lines (L26, L69), matching the flag; `grep -n 'local--files' candidate.txt` — the three encoded URLs.
- **Disposition:** JP load and stack applied; the three asset URLs are DISPOSITIONED (class (ii) / KB-58, original-state hosting); the Fredericka load gap is FLAGGED (per-theme record).

### 5. Header, sidebar, and site furniture

- **What:** One variable group is carried, none is overridden for JP: the candidate keeps the original's act-specific `:root` strings (`--head-prelude`, `--head-1`..`--head-3`, `--sub-*`, candidate L28–38) in English — they are the theme's own act titles for Yoshihide's Proposal, reader-visible through the BHL header machinery — and the `--header-font` stack of section 4 is the only header variable whose value changes. There is no `--header-title` or `--logo-image` override. The EN BHL furniture includes are section 2.
- **Why:** P9/T6 is a per-theme judgment; KB-57 (header language) is the standing disposition family for kept original-language header text — the act titles are the work's own proper titles, not UI prose awaiting translation.
- **Verify:** `grep -n -- '--head-\|--sub-\|--header-' candidate.txt original.txt` — the values correspond one to one apart from section 4's stack.
- **Disposition:** Standing; the kept English act titles are recorded here so they are not mistaken for untranslated prose (section 6).

### 6. Text translation

- **What:** The candidate's prose is three compressed lines at the head (candidate L19–23, inside block B2): the theme description (Black Highlighterを基盤にしたAshes to Ashesテーマです), the usage line, and the base line. They replace, in compressed form, the original's usage prose that sat in its tail body (section 8). The original's story quote and contest note were not translated; they were dropped with that body. The CSS carries no translated strings: the act titles of section 5 are kept in English, there are no `content:` strings, and the one CSS comment (`/* ACT-SPECIFIC CSS */`, `/* REGULAR STUFF */`) is carried untranslated as porter-visible text (R1 comment form, a known non-finding shape). R5 glyph-form conversion: none (the source is English).
- **Why:** P10 for the usage prose; the distinction between reader-visible strings (KB-18) and porter-visible comments is the R1 line — comments are documented here, not charged.
- **Verify:** Read candidate L19–23 against the original's tail prose (original L152–160); a CJK scan of the candidate's CSS returns only the font names of section 4.
- **Disposition:** Standing; the dropped English prose is adjudicated in section 8, not hidden here.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L18): `https://scp-wiki.wikidot.com/theme:ashes-to-ashes`. That is the original's recorded host — review/sources.tsv records the original at scp-wiki.wikidot.com, the same host the mirror was taken from — so the link names the serving original and no host defect arises. The original's contest link (to the Public Domain Contest 2025 page) sat in the dropped tail body (section 8). No other prose links exist in the candidate.
- **Why:** P11, under the dead-reference evidence standard; here the recorded host and the link agree, which is the check the jiha package's finding taught this batch to run on every theme.
- **Verify:** Compare candidate L18's host against the sources.tsv row's original_url host (scp-wiki.wikidot.com) — identical.
- **Disposition:** Standing; no defect flag.

### 8. Structure

- **What:** Two structural facts. First, the preserved core: the override CSS module keeps the original's variable names, selectors, and order (original L11–141 → candidate L25–151), with the JP edits arriving as the head frame and credit block, not interleaved into the inherited CSS — the localize.md closing rule holds for the CSS. Second, the deletion (block B9, EXHIBIT-RESTRUCTURE with BARE-RATE-DEL): the original's entire tail body (original L143–209) — the centred bare Rate, the Yoshihide story quote, the contest note and usage prose, the image-block exhibit, the header/format specimens, the collapsible and footnoteblock exhibits — is dropped, and the candidate ends at its CSS module. Adjudication, replaced vs dropped: the usage prose is *replaced* in compressed form at the head (section 6); the Rate is *replaced* by the rate-bearing credit block (section 1); the demonstration exhibits and the story quote are *dropped* without a translated counterpart. The ground for the drop, stated plainly: the JP theme-page form carries the credit, the compressed usage head, and the CSS; demonstrations live on the decoration sample (`pages/theme-decoration-sample-ashes-to-ashes-jp.txt`), which is where the render checks exercised this theme's formatting. No ledger record charges the drop as a class I item, and the theme's T4 findings (section 12) do not name it; it is recorded here because R3 requires the ground to be stated, not because a record charged it.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** An exhibit census — `grep -n '\[\[tab\|\[\[code\|\[\[collapsible\|\[\[include\|image-block' original.txt candidate.txt` — shows the original's exhibits with no candidate counterparts outside the head lines.
- **Disposition:** Standing as documented; no class I item was charged by any record.

### 9. Formatting only

- **What:** One block: B8, the classifier's residue — a single blank line added ahead of the candidate's `[[/module]]` (candidate L152). No whitespace-only block pair and no re-indentation anywhere else (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The last hunk of diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added. The candidate carries no `[!-- --]` translator notes and no editor line; its only CSS comments are the original's own section comments, carried untranslated (section 6).
- **Why:** R2: porter-added text is part of the change record; here the check was run explicitly and the answer is none.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; the `/*` lines in candidate.txt all have original counterparts.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three hotlink errors: the three original-state asset URLs of section 4 — DISPOSITIONED in register c1 (hotlink, class (ii): original-state asset hosts are rewritten at posting or kept as original state; re-upload is barred by owner order), and per-theme in §(c3) as P5 DISPOSITIONED (class (ii) / KB-58). (2) P4 delivery: §(c3) records P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery) — the original-state delivery lines that remain are the section 4 assets; the BHL @import delivery itself was removed, not kept (section 3). (3) The T2/T3 row's only note is borderline license legibility (an observation, cross-cutting X2/X3/X5/X7 family), recorded as not-charged. The two FLAGGED items (the unloaded header font; the absent BHL base delivery) are argued in the per-theme record; the ledger's determination for this theme is PASS and this package does not re-open it — the flags are the documentation doing its job.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 not-charged; two items flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 59): exit 1, 3 errors / 1 warn / 0 infos; all three errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN3)): PASS-WITH-NOTES on both pages — no candidate-specific defect beyond the cross-cutting families; only borderline license legibility (observation); no BLOCKED-ENV. (c) T4/T5 (LOCALIZE-ROWS row 59): FINDINGS jointly, display-affecting findings 5 — the destroyed font @import with the header falling back (finding 1; its current state is the per-theme record's first flag), the three EN local--files direct links (finding 2; dispositioned, section 11), the absent interwiki-style (finding 3; since FIXED, section 3), and the balance of the row's five. The ledger §(c3) line records the outcomes: P4 DISPOSITIONED, P5 DISPOSITIONED, P6 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +27/−82 in 9 change blocks / 6 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ashes-to-ashes-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 59; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The header font that is named but never loaded

LOCALIZE-ROWS row 59 records the T4 lane's first finding: the font `@import` was destroyed wholesale, `'Fredericka the Great'` did not load, and the header fell back to Times New Roman; the lane's stated remedy was a repoint to Google Fonts. The bytes at the FIX5 head show a half-repair. The candidate's only font load (candidate L26) is a Google Fonts import of Noto Sans JP; the two bunny.net loads (Fredericka the Great, Protest Revolution) are deleted; and the header stack (candidate L69) reads `'Fredericka the Great', 'Noto Sans JP', Times New Roman`. So the named first-choice face is still loaded nowhere in the candidate — `grep -n 'Fredericka' candidate.txt` returns exactly the stack line — and the header now falls back to Noto Sans JP instead of Times New Roman. No ledger outcome line for this theme names the font load (the §(c3) line covers P4, P5, P6), so the package carries the item as a flag: a one-line load (adding the Fredericka family to the existing Google Fonts import) is the repair a future editor should make, and making it is outside this package's remit, which is to document the candidate as it stands. Protest Revolution needs no such repair: the original loaded it but referenced it in no stack, and the candidate references it nowhere either.

### The BHL base that the prose declares and the file does not deliver

The original delivered the Black Highlighter base by two @imports from nu-scptheme.github.io (original L3–4); the candidate deletes them and contains no BHL load of any form — no @import, no JP BHL theme include — while its own prose declares **基盤:** BHL（インライン） (candidate L23) and its frame names only its own code at priority 1 (section 3). The campaign's BHL form elsewhere (this batch's theme:doap-bhl-jp) delivers the base through `[[include :scp-jp:theme:black-highlighter-theme]]` with the theme's own layer framed at priority 3. Against that form, this candidate's base delivery is absent from the two files in this package. The counter-evidence is the render record: T2/T3 ran the composition and returned PASS-WITH-NOTES with no candidate-specific defect, so in the check environment the override layer rendered as a theme. The package records both sides and flags the gap for the coordinator: either the environment supplies the base (in which case the prose line is right and the delivery is environmental), or the candidate is missing its base layer (in which case the fix is the doap form). The two files in this package cannot decide between those, and the package does not pretend they can.

## Appendix — residue blocks

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B4 | 58-58 → 69-69 (module-css → module-css) | heuristic CSS-BODY | P7 font-stack rewrite: `'Noto Sans JP'` inserted into the `--header-font` stack; section 4 |
| B8 | at 141 → at 152 (module-css → body) | residue, no signature | Single blank line added ahead of `[[/module]]`; section 9 |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-ashes-to-ashes-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row, and it is where this theme's demonstration formatting lives after the section 8 drop); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
