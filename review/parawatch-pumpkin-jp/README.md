# Review package — theme:parawatch-pumpkin-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:parawatch-pumpkin-jp — origin EN, population #121 [GOSIGN2-LEDGER (b) row 121]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4f5b0c4daa46aac4e6fee59f16aa6f9770fb484937eb1ca7496db242f1ff6b43); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 0 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 156; GOSIGN2-LEDGER (b) row 121]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only (T3: credit modal opens); sample credit-modal (preview-form) + page-overflow 325px@320 + 884px@768. [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 121, source LOCALIZE-S2-B]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 121]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 121]
- Computed against: canonical commit a2bd1fb983b56a82b69d82c9350a628c2e32197d; candidate file pages/theme:parawatch-pumpkin-jp.txt sha256:4f5b0c4daa46aac4e6fee59f16aa6f9770fb484937eb1ca7496db242f1ff6b43; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 121) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (iii), section 11); the render row's items (KB-40 / KB-32 and the sample overflow readings, section 11). **FLAGGED by this package** — the usage exhibits and two prose links name base-theme pages under plain slugs that do not resolve on scp-jp (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:parawatch-pumpkin | theme:parawatch-pumpkin-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 11 (first translation; the candidate's credit block records 初訳時参照リビジョン: 11) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-parawatch-pumpkin.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:parawatch-pumpkin-jp.txt`, copied at worktree HEAD 9068bb7 |
| Lines / bytes | 124 lines / 3,182 bytes | 128 lines / 3,994 bytes |
| SHA-256 | 6ea878e7861854c2929605c6c2ddd7c0554e1801ecc87f225aab3017b69caa09 | 2920681af49a424036e58ebc5eefd53b61bca441316b69533926cb70c4efe031 |

Wave history: the candidate was created by the Stage 2 EN16 integration (commit 6d5fc81, the LOCALIZE-S2-B wave's port, lane-oc-en16) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose parawatch hunk is the translator-field normalization (翻訳責任者 taking its ruling-3 form). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A derivative theme at the mechanical end of the campaign: Parawatch Pumpkin is a recolor of the Parawatch Anon theme, which is itself a variant of Creepypasta, and the port's real work is re-expressing that base chain in JP form. The original pulls both bases in as live foreign includes; the candidate includes the JP anon candidate (theme:anon-jp), through which the JP creepypasta candidate's delivery arrives, and states that chain in an added credit line. Around that, the changes are the standing classes applied once each: the bare Rate and blockquote credit prose are swapped for the preview credit block, the tail delivery (module CSS plus an interwiki-style include at priority 3) is rebuilt at the head as the wave-standard frame at priority 1 on the draft host, the one image is re-hosted to the candidate's draft-host folder, the license box takes the JP backend form with its entry translated, and the prose and two CSS comment banners are translated. Measured churn (diff.md, the generator's difflib count with autojunk off: +40/−36 in 13 change blocks / 4 hunks). One item deserves a reviewer's eye rather than a skim: the usage exhibits and the prose links to the anon base name plain slugs that do not resolve on scp-jp, recorded with probe evidence in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 13 change blocks — 8 specific (61.5%), 5 heuristic (38.5%), 0 residue (0.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 7 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 3 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| COMMENT-TEXT | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| IFTAGS | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 5 heuristic blocks resolve as 2 prose translations (B4, B5, section 6), 2 CSS comment translations (B7, B9, R1, section 6), and 1 relocation of the `#interwiki` filter rule into the frame's `css=` parameter (B10, section 3). The 2 EXHIBIT-RESTRUCTURE primaries are not exhibit changes: B11 is the license-box swap (section 1) and B13 is the tail delivery's relocation to the head (section 3); the exhibit census (the usage code div, the CSS code block, the license entry) is complete on both sides. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:parawatch-pumpkin-jp; original theme:parawatch-pumpkin on scp-wiki at reference revision 11; candidate `pages/theme:parawatch-pumpkin-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original opens with its tag gate `[[iftags +theme]]` (original L1) and carries its delivery at the tail (original L117–124); the candidate opens with the delivery frame and its own-code module (candidate L1–9) and places the localized gate `[[iftags +テーマ]]` after them (candidate L11).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization), the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for parawatch-pumpkin-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a right-aligned block (original L7–10) plus credit prose in a blockquote (original L12–13) naming the author and the two base themes; there is no info module. The candidate deletes the Rate block outright (block B3) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L13–23) carrying the eight ruling-3 fields (title パラウォッチ・パンプキンテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Parawatch Pumpkin Theme; 著作権者 [[*user stormbreath]]; 作成年 2022; 初訳時参照リビジョン 11; the source link https://scp-wiki.wikidot.com/theme:parawatch-pumpkin, whose host matches the sources.tsv record for the original). The block carries one further line with no counterpart among the eight: a 基盤 (base) statement (candidate L22) recording that the base is the Parawatch Anon theme via theme:anon-jp and that Creepypasta is bundled inline through it; that statement is porter-added credit prose and is counted in section 10. The original's blockquote prose survives directly below, translated (candidate L28–29). License box: the original's `:scp-wiki:component:license-box-theme`/`end` pair (original L106–113) becomes the JP backend form, `:scp-jp:component:license-box-backend |author=stormbreath]]` with `:scp-jp:component:license-box-end` (candidate L119–124), and its single image entry (parawatch-orange.png) is translated in place (ファイル名 / 著者 / ライセンス / 派生元), the derivative-of link kept to the serving scp-wiki creepypasta page. T7 credit-module CSS: none — neither side styles the credit module (no `.creditButton` or `.rate-box-with-credit-button` rule exists in either file), so there is no supplement to add and none was.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields and the translator credit form; the file's last commit (1869877) is exactly that form arriving. T4 (the JP license box) is a swap here, not an addition: the original already carried the box.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L13–23 against the eight fields; `grep -n 'license-box' candidate.txt` — the backend/end pair at L119 and L124.
- **Disposition:** FIXED by construction at creation (P3 credit fields; the ledger's (c3) register carries no item for this theme, and T4 judged the theme PASS with 0 display-affecting findings, LOCALIZE-ROWS row 121).

### 2. Includes and components

- **What:** The live base chain is one block (B2, COMPONENT-SWAP): the original's hidden div includes both bases live from the foreign wiki, `:scp-wiki:theme:creepypasta` and `:scp-wiki:theme:anon` (original L3–4); the candidate's hidden div includes exactly one page, `theme:anon-jp` in bare local form (candidate L25). The second base is not dropped: theme:anon-jp's own delivery `@import`s theme:creepypasta-jp's code (its credit block states the same chain), so the full chain of the original (pumpkin → anon → creepypasta) is preserved with every link in JP-candidate form. The three usage exhibits (B6) are repointed `:scp-wiki:` → `:scp-jp:` (original L20–22 → candidate L36–38); their slugs are the plain forms, which is the flagged item of the per-theme record. The frame include (candidate L1) is the bare local `component:interwiki-style`, the JP environment's own form; the credit and license includes are section 1. Every live include in the candidate resolves on the JP side.
- **Why:** P1 (KB-15) for the exhibits: an include must name the JP counterpart. For the live chain, ruling 1 (cross-theme imports repoint to the JP fixed base candidate) and KB-14: a dependent theme takes its base from the base's JP port candidate, never from the foreign original; taking anon through theme:anon-jp also inherits anon-jp's own creepypasta delivery instead of naming the EN creepypasta page. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — nine includes; the live chain is candidate L25; theme:anon-jp's creepypasta import is at `pages/theme:anon-jp.txt` L27.
- **Disposition:** Applied for the live chain; the exhibits' slug form is flagged in the per-theme record (not edited by this package).

### 3. Delivery and code loading

- **What:** The original delivers at the tail: a `[[module CSS]]` importing its own `local--code/theme%3Aparawatch-pumpkin/1` from scp-wiki.wdfiles.com (original L117–119) and an interwiki-style include at priority 3 with `theme=` naming the same /1 (original L121–124). The candidate rebuilds both at the head (blocks B1, B12, B13): the interwiki-style frame at priority 1 with `theme=` naming its own `local--code/theme%3Aparawatch-pumpkin-jp/1` on the draft host (candidate L1–5), and the module CSS importing the same /1 (candidate L7–9). The priority drops from 3 to 1 because the layering changed, not the theme: in the original the frame's stack sat above the two live-included bases, while in the candidate the base chain arrives through the section 2 include and the frame carries the theme's own layer only. The frame also gains a `css=` parameter with no original counterpart at the frame: the `#interwiki .menu-item img` filter rule (hue-rotate(8deg) brightness(4.5) saturate(200%)) that the original's code block carries as its last rule (original L101–103) is percent-encoded into the frame's css parameter (candidate L4), and the code block no longer carries it (block B10, the classifier's CSS-BODY primary). The rule styles the interwiki module's own DOM, so it rides the include that renders that module.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame; priority names the theme's own layer). The draft-host form of both live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L3 (frame) and L8 (module), both draft-host; decode candidate L4's css parameter against original L101–103.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: none. Neither side names a `font-family` anywhere (0 hits in each file); the theme inherits its bases' fonts, no JP font supplement was needed, and none was added — the skeleton's "none" for the font half survives contact with the bytes. Assets: one image, parawatch-orange.png, referenced by the header rule (original L66, on scp-wiki.wdfiles.com under `theme%3Aparawatch-pumpkin/`) and re-hosted to the candidate's own draft-host folder `theme%3Aparawatch-pumpkin-jp/` with the filename unchanged (candidate L82, block B8). Its license entry is section 1.
- **Why:** P5 with KB-17 (asset hosts): the theme's own image is re-hosted to the JP side. The draft-host form is the same class (iii) as section 3.
- **Verify:** `grep -n 'font-family' candidate.txt` returns nothing; `grep -n 'parawatch-orange' candidate.txt` — L82 (CSS) and L120 (license entry).
- **Disposition:** DISPOSITIONED (the draft-host asset URL, class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** None. The candidate overrides no header variable (no `--header-title`, no `--header-subtitle`, no `--logo-image` on either side), and the theme's header, top-bar, and sidebar rules are carried over unmodified apart from their comment banners (section 6). The one furniture-adjacent rule, the `#interwiki` image filter, moved into the frame's css parameter and is recorded in section 3, not here. No P8 layout adaptation was needed: the candidate inherits the JP site furniture through the frame and the base chain.
- **Why:** P8/P9 are checked and absent, which is itself the finding a reviewer needs: nothing in this theme's furniture required a JP-specific override.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose is translated throughout, in two counted groups. Blocks B4–B5 (TRANS-UNANCHORED primaries, verified line by line against the mirror): the blockquote credit paragraph (candidate L28–29), the introduction (candidate L31), and the usage lead-in (candidate L33). R1 in-CSS text: the code block's two section banners are translated in place, `/* -------------- HEADER -------------- */` → `/* -------------- ヘッダー -------------- */` (B7, candidate L75) and `/* -------------- SIDE-BAR -------------- */` → `/* -------------- サイドバー -------------- */` (B9, candidate L102); both are porter-visible only, not reader-visible. No reader-visible CSS string exists in this theme (no `content:` property on either side), and no string-valued variable carries text. No source-language prose survives outside the credit block's original-title field (candidate L17, a quotation by design).
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings). R1 is stated separately from reader-visible text because comments are porter-visible only; the distinction is what lets a reviewer judge the translation claim precisely.
- **Verify:** The pairs are diff.md's body sections in order; an English-prose scan of candidate.txt outside the credit fields returns only the license-entry link target and user names.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme PASS with 0 display-affecting findings (LOCALIZE-ROWS row 121).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L21), naming the original on scp-wiki.wikidot.com, the host the campaign's provenance records name for it; it serves the original page. Two prose links inside the translated text name base-theme pages in bare local form, `[[[theme:anon|…]]]` and `[[[theme:creepypasta|…]]]` (candidate L29; the anon link also appears in the credit block's base line, candidate L22). Probed for this package (2026-11-17): theme:creepypasta exists on scp-jp as a production page (200), so that link resolves; theme:anon does not exist on scp-jp (404), so the anon links name a page that is not there — the base's JP presence is the candidate theme:anon-jp. The license entry's derivative-of link (candidate L123) names the scp-wiki creepypasta page by full URL and serves. The anon-link finding is argued in the per-theme record.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard (probe first, then judge).
- **Verify:** `grep -n 'theme:anon\]\|theme:creepypasta\]' candidate.txt` — L22, L29 (anon) and L29 (creepypasta); the probe pair is recorded in the per-theme record.
- **Disposition:** The creepypasta link stands (serving production page); the anon links are flagged in the per-theme record.

### 8. Structure

- **What:** The localize.md closing rule holds for everything the candidate carries: the CSS code block sits where the original's sits relative to the prose (after the usage exhibits), its rules, selectors, and order are unchanged, and the JP corrections arrive as the head frame and credit block, not interleaved into the inherited CSS. An exhibit census confirms the shape: the usage code div, the CSS code exhibit, and the license entry are present on both sides in the same order. The classifier's two EXHIBIT-RESTRUCTURE primaries adjudicate away from this section: B11 is the license-box swap (section 1) and B13 is the delivery relocation (section 3). The one rule that left the code block, the `#interwiki` filter, moved into the frame's css parameter (section 3) and is accounted there, so the R3 question (sanctioned replacement vs silent deletion) does not arise for this theme.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|\[\[div class="code"\|license-box' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation anywhere in the pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, riding inside another labeled block: the credit block's 基盤 line (candidate L22), which has no original counterpart and records the base chain the port established (anon via theme:anon-jp, Creepypasta bundled inline through it). It rides inside the CREDIT-PREVIEW block (B1), which is why no separate annotation signature fired; the skeleton's "none" for this section does not survive contact with the bytes and is corrected here. There are no comment-form annotations (`[!-- … --]`) and no editor lines in the candidate.
- **Why:** R2: porter-added text is part of the change record; this line is load-bearing, because it is the only in-file statement of how the two-base chain is delivered in JP form.
- **Verify:** Read candidate L22 against original L12–13 (the prose it supplements).
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two pseudo-ref errors: class (iii), draft-form — they are the candidate's own draft-host local--code lines (sections 3–4); the posting procedure rewrites them to the production host, and fix lanes never "fix" them in the candidate. (2) The render row's items, all environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the sample's page-overflow readings (325px@320, 884px@768), recorded verbatim from RENDER-ROWS-2 without a candidate-side cause in the row. T3's note that the credit modal opens on the page is the real-module behaviour on the decoration sample, the counterpart of the preview-form disposition. (3) The usage exhibits and anon prose links flagged in the per-theme record: the package records them with probe evidence and does not edit the candidate; the ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 156): exit 1, 2 errors / 2 warns / 0 infos; both errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN16)): FINDINGS, the three items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 121): PASS jointly, display-affecting findings 0; the ledger (c3) register carries no disposition line for this theme because nothing needed one. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +40/−36 in 13 change blocks / 4 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:parawatch-pumpkin-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 121; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibits and the anon prose links (flagged by this package)

The usage exhibits (candidate L36–38) were repointed from `:scp-wiki:` to `:scp-jp:` at creation, but their slugs are the plain forms: `:scp-jp:theme:creepypasta`, `:scp-jp:theme:anon`, `:scp-jp:theme:parawatch-pumpkin`. The candidate's own posting name is theme:parawatch-pumpkin-jp, and its live base include uses the correct JP form (bare `theme:anon-jp`, candidate L25), so the file contradicts itself: a reader copying the documented syntax would include a page that does not exist under that name for two of the three lines (anon and parawatch-pumpkin), and for the third (creepypasta) would include the older production page on scp-jp rather than the creepypasta-jp delivery this candidate's chain actually uses. The same plain-slug shape appears in the prose links to the anon base (candidate L22 and L29): probed for this package (2026-11-17), `https://scp-jp.wikidot.com/theme:anon` returns 404 while `https://scp-jp.wikidot.com/theme:creepypasta` serves the production page (200). This is the shape the campaign's own supplement charged elsewhere (GOSIGN2-LEDGER-SUPPLEMENT item 82, theme:shivering-night-jp: dead prose links naming plain slugs whose candidates carry the -jp form). T4 judged this theme PASS with 0 display-affecting findings, so the record and the bytes disagree for these lines; this package follows the bytes and the probe, flags the five lines (candidate L22, L29, L36, L37, L38), and leaves the candidate unedited, as the population sweep repairing this family is a coordinator matter.

The dead prose links have since been repaired — FIX-MISC9, canonical commit `a2bd1fb983b56a82b69d82c9350a628c2e32197d` ("pages: pastel-skies font load and parawatch-pumpkin links", 2026-11-17; report `R/review-scout/FIX-MISC9.md`). Two single-token changes closed the 404s: the credit block's 基盤 line (candidate L22) and the body prose line (candidate L29) now name `[[[theme:anon-jp|…]]]` instead of the plain `theme:anon` that returned 404 while this candidate's live chain runs through `theme:anon-jp` (candidate L25); the checker's counts were unchanged and no class (i) error appeared. The earlier population sweep b5cb724 also repaired two of the three usage exhibits: the anon and parawatch-pumpkin lines now name `:scp-jp:theme:anon-jp` and `:scp-jp:theme:parawatch-pumpkin-jp` (candidate L37–38). The remaining `creepypasta` exhibit (candidate L36) still names the plain production slug, which is unchanged by the repair recorded here and left as it stands (theme:creepypasta is the dependency base whose live production page serves today). This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:parawatch-pumpkin-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-parawatch-pumpkin-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The base chain runs through `pages/theme:anon-jp.txt` (section 2), which is that theme's own package's subject, not this one's. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Parawatch Pumpkin Theme
- **Author:** stormbreath
- **Source:** https://scp-wiki.wikidot.com/theme:parawatch-pumpkin — revision 11
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
