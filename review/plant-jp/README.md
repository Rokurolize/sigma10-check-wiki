# Review package — theme:plant-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:plant-jp — origin EN, population #123 [GOSIGN2-LEDGER (b) row 123]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 50535b11b1a03d9e460a6458c1ecbd0af40a49808ed5119292a0ceb69c4f05c6); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 2 warns / 0 infos (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 158; GOSIGN2-LEDGER (b) row 123]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 851px@webkit-768 (page only) + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2). [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 123, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 123]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 123]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:plant-jp.txt sha256:50535b11b1a03d9e460a6458c1ecbd0af40a49808ed5119292a0ceb69c4f05c6; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 123) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (class (iii), section 11); the render row's page-overflow reading and site-theme chain (KB-40, section 11); T4's two items, P7 and P9, both dispositioned in the ledger's (c3) register (sections 4, 6, 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:plant | theme:plant-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 28 (first translation; the candidate's credit block records 初訳時参照リビジョン: 28) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-plant.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:plant-jp.txt`, copied at worktree HEAD 9068bb7 |
| Lines / bytes | 266 lines / 6,274 bytes | 271 lines / 7,123 bytes |
| SHA-256 | 95e334cdc70b2d10b365e8a289f690d93bfe01832e0bbac856b053e9b21d2407 | 36c3aee5495953c3f5d5f2a24945337d8969756dc7ef3524340bc1114ca0bedd |

Wave history: the candidate was created by the Stage 2 EN16 integration (commit 6d5fc81, the LOCALIZE-S2-B wave's port, lane-oc-en16) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose plant hunk is the translator-field normalization. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A small Sigma-9 variant theme (the 2020 April Fool's "Super Cool Plants!" theme) whose port is the standing classes applied once each, with no defect repair and no structural surprise. The original already delivers in the modern form (a head module CSS plus an interwiki-style frame at priority 1), so the delivery work is a host repoint, not a rebuild. The bare Rate is swapped for the preview credit block, which gains a font credit line; the license box takes the JP backend form with all three image entries translated; the Short Stack load moves from fonts.bunny.net to Google Fonts and 'Noto Sans JP' is appended to the two heading stacks; the code exhibit's banner comment and section comments are translated; and the asset URLs take the draft-host form. Measured churn (diff.md, the generator's difflib count with autojunk off: +98/−93 in 40 change blocks / 8 hunks). Two T4 items ride along as dispositions, both stated openly below: the heading stacks name a JP face this file never loads (section 4), and the masthead string stays in English under ruling 2 (section 6). The usage exhibit names the plain slug on the JP side, the population-sweep family, flagged in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 40 change blocks — 24 specific (60.0%), 13 heuristic (32.5%), 3 residue (7.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 19 |
| COMMENT-TEXT | 9 |
| WS-ONLY | 8 |
| DRAFT-HOST | 7 |
| SELF-DELIVERY | 3 |
| EXHIBIT-RESTRUCTURE | 3 |
| IFTAGS | 2 |
| JPFONT-STACK | 2 |
| LICENSE-BOX | 2 |
| LINK-REPOINT | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 3 residue blocks are B8 (an alignment artefact where the usage lead-in's translation and the exhibit repoint cross, sections 2 and 6) and B13/B16 (trailing-space blank lines inside the code exhibit, section 9). Of the heuristic mass, the COMMENT-TEXT blocks are the banner and section-comment translations (R1, section 6), the license-entry translations are B38–B40 (section 1), and the remaining TRANS-UNANCHORED blocks are one-line prose and entry translations verified line by line (section 6). The 3 EXHIBIT-RESTRUCTURE primaries are not exhibit changes: B3 is the frame include's form change (section 3), B37/B40 are the license-box swap and its entries (section 1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:plant-jp; original theme:plant on scp-wiki at reference revision 28; candidate `pages/theme:plant-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). Both sides open with the delivery pair (module CSS, then the interwiki-style frame) ahead of the tag gate; the candidate keeps that order, with the localized gate `[[iftags +テーマ]]` at candidate L11 (original `[[iftags +theme]]` at original L11).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for plant-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` in a right-aligned block (original L13–16); there is no info module and no credit prose on the original. The candidate deletes the Rate block (BARE-RATE-DEL block) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L13–23) carrying the eight ruling-3 fields (title Plantテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Plant Theme; 著作権者 [[*user stormbreath]]; 作成年 2020; 初訳時参照リビジョン 28; the source link https://scp-wiki.wikidot.com/theme:plant, whose host matches the sources.tsv record). The block carries one further line, a フォント credit (candidate L22) naming Short Stack and Noto Sans JP as Google Fonts faces under the SIL Open Font License; that line is the P7 font credit and is assessed in section 4. License box: the original's `:scp-wiki:component:license-box-theme`/`end` pair (original L234–265) becomes `:scp-jp:component:license-box-backend |author=stormbreath]]` with `:scp-jp:component:license-box-end` (candidate L241–270), and all three image entries are translated in place, field labels included (ファイル名 / 名称 / 著者 / ライセンス / 派生元 / ソースリンク): plantbg.png (stormbreath, CC BY-SA 3.0, derivative of Dimhou's CC0 Pixabay photograph), body_bg.png (Aelanna, CC-BY-SA 3.0), and plantlogo.png (stormbreath, derivative of a CC0 kissclipart leaf). No attribution present in the original is dropped: the banner comment's two image credits (original L35–36) also survive, translated, in the code exhibit (candidate L42–43). T7 credit-module CSS: none — neither side styles the credit module, so there is no supplement to add and none was.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields and the translator credit form; the file's last commit (1869877) is that form arriving. T4 (the JP license box) is a swap here, not an addition (KB-63 is the dropped set; this theme is not in it).
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L13–23 against the eight fields; compare the license entries at original L234–265 and candidate L241–270 entry by entry.
- **Disposition:** FIXED by construction at creation (P3 credit fields; T4 judged the credit furniture complete — its two findings are the font and masthead items of sections 4 and 6).

### 2. Includes and components

- **What:** One repoint block: the usage exhibit, `:scp-wiki:theme:plant` → `:scp-jp:theme:plant` (original L22 → candidate L29). Its slug is the plain form, which is the flagged item of the per-theme record. The frame include loses its site prefix, `:scp-wiki:component:interwiki-style` → bare `component:interwiki-style` (original L5 → candidate L1), the JP environment's local form for its own component. The credit and license includes are section 1. No other include exists on either side; no component swap (T8) was needed and none was made.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — six includes, all JP-side or bare-local.
- **Disposition:** Applied; the exhibit's slug form is flagged in the per-theme record (not edited by this package).

### 3. Delivery and code loading

- **What:** The original already delivers in the form the campaign standardizes: a head `[[module CSS]]` importing its own `local--code/theme%3Aplant/1` from scp-wiki.wdfiles.com (original L1–3) and an interwiki-style frame at priority 1 with `theme=` naming the same /1 (original L5–8). The candidate keeps both, in the same order and at the same priority, repointed to its own delivery on the draft host (candidate L1–8): the frame's `theme=` names `local--code/theme%3Aplant-jp/1` on sigma10-jp-test.wdfiles.com and the module imports the same /1 from sigma10-jp-test.wdfiles.com. The classifier's EXHIBIT-RESTRUCTURE primary B3 is this zone (the frame include's prefix change), not an exhibit change. The code exhibit itself (original L28–94 → candidate L35–101) is the documentation copy of the same CSS and is carried as an exhibit, not a live channel.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame, priority 1 for the theme's own layer over the Sigma base). The draft-host form of both live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L3 (frame) and L7 (module), both draft-host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Loads: the original loads one face, Short Stack, from fonts.bunny.net (original L29, inside the code exhibit); the candidate loads the same face from Google Fonts (candidate L36, block B11) — a host re-host of the identical family load, not a grammar repair. Stacks: 'Noto Sans JP' is appended to the theme's two heading stacks (blocks B14, B21): the `h1, #page-title` stack (original L41 → candidate L48) and the `#header h1 a, #header h2 span` stack (original L95 → candidate L102), both becoming `'Comic Sans MS', 'Comic Sans', 'Short Stack', 'Noto Sans JP', cursive`. The credit block's font line (candidate L22) credits both faces as Google Fonts loads. The file-level fact, stated plainly: no line in the candidate loads Noto Sans JP — its only font load is Short Stack — so the appended family renders only where the surrounding JP environment supplies it, which this repo cannot verify (the environment base, theme:sigma-10-jp, loads a compiled sigma stylesheet from scp-jp.github.io whose contents are outside this repo). T4 charged exactly this (LOCALIZE-ROWS row 123, item (a): "P7 font credited/named but never loaded (mild, display-affecting class)"), and the ledger dispositioned it (section 11). Assets: the theme's own images (tabs.png and the background/logo files named in the license entries) move from `scp-wiki.wdfiles.com/local--files/theme%3Aplant/` to the draft host's `theme%3Aplant-jp/` folder with filenames unchanged (the DRAFT-HOST blocks inside the code exhibit, e.g. candidate L74, L79, L229–238).
- **Why:** P7/T5 with KB-16 (the font load gap) is the class the charge and the supplement both belong to: a JP face is appended to Latin-only stacks so Japanese heading text renders in a JP face rather than a fallback. P5 with KB-17 for the Short Stack re-host (fonts.bunny.net is not among the hosts the JP environment keeps; Google Fonts is) and for the asset re-hosting.
- **Verify:** `grep -n '@import' candidate.txt` — two lines (L7 self-delivery, L36 Short Stack); `grep -n 'font-family' candidate.txt` — the two stacks at L48 and L102.
- **Disposition:** The Short Stack re-host and the stack appends are applied. The Noto Sans JP load gap is DISPOSITIONED (GOSIGN2-LEDGER §(c3): P7 DISPOSITIONED, recorded without a display-affecting mark under the T4 bar), with the file-level fact stated above rather than passed over.

### 5. Header, sidebar, and site furniture

- **What:** None. The candidate overrides no header variable (no `--header-title`, no `--header-subtitle`, no `--logo-image` on either side), and the theme's header, sidebar, and tab rules are carried over unmodified apart from the font stacks (section 4), their comment banners (section 6), and the asset hosts (section 4). The skeleton's "none" for this section survives contact with the bytes. No P8 layout adaptation was needed.
- **Why:** P8/P9 are checked and absent, which is itself the finding a reviewer needs.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose and the code exhibit's text are translated throughout. Prose: the introduction (original L18 → candidate L25), the usage lead-in (candidate L27), the heading sample (`+ Heading 1` → `+ 第1見出し`), and the link exhibit's labels (`[# Unvisited Link] ([/theme:plant Visited Link])` → `[# 未訪問リンク] ([/theme:plant 訪問済みリンク])`, its target path kept as the original's form). R1 in-CSS text: the code exhibit's banner comment is translated (candidate L38–44: `[2020年 Wikidotテーマ]`, `SCP財団のために stormbreath が作成`, and the logo/header image credit lines with their CC0 source URLs kept), and its section comments are translated (`/* COMMON */` → `/* 共通 */`, `/* FOOTER */` → `/* フッター */`, `/* YUI-TABS */` → `/* YUIタブ */`); all are porter-visible only. The license entries' field labels and names are translated in section 1. One string stays in English by disposition: the masthead/event name "Super Cool Plants!" (candidate L25 prose and the banner at candidate L39), which is T4's item (b), a P9 header/title-language item dispositioned under ruling 2 (header and title language is out of scope for migration correctness). No other source-language prose survives outside the credit block's original-title field (candidate L17, a quotation by design).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). R1 is stated separately because comments are porter-visible only. Ruling 2 covers the kept masthead string.
- **Verify:** The pairs are diff.md's body sections in order; an English-prose scan of candidate.txt outside the credit fields returns the masthead name and the license entries' proper nouns only.
- **Disposition:** Standing (the port itself); the masthead string is DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3) P9 line for this theme).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L21), naming the original on scp-wiki.wikidot.com, the host the campaign's provenance records name for it; it serves the original page. The license entries' source links are kept to their serving originals (the Pixabay photograph and the kissclipart leaf, candidate L250 and L264), with their labels translated. One entry's source link is a bare local form on both sides, `[[[component:theme|Site Theme]]]` → `[[[component:theme|サイトテーマ]]]` (candidate L255, L269): a same-wiki component reference carried in the original's form, its label translated (the classifier's LINK-REPOINT primary B38 sits in this zone and adjudicates to the entries' label translations, not a target change). The link exhibit in the usage sample keeps its `/theme:plant` path target with translated labels (section 6); it is sample text, not navigation.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; exhibit labels follow P10 instead.
- **Verify:** `grep -n 'wikidot.com\|pixabay\|kissclipart' candidate.txt` — the source link and the two license source links.
- **Disposition:** Standing; no dead link was found in this theme and none was left byte-unchanged under an ORIGINAL-DEFECT claim.

### 8. Structure

- **What:** The localize.md closing rule holds: variable names, selectors, and channel order are preserved; the candidate's code exhibit sits where the original's sits, and the JP corrections arrive as the head frame/credit swap and the license-box swap, not interleaved into the inherited CSS. An exhibit census confirms the shape: the usage exhibit, the heading and link samples, the CSS code exhibit, and the license entries are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise. The classifier's three EXHIBIT-RESTRUCTURE primaries adjudicate to the frame form change (B3, section 3) and the license-box swap and entries (B37, B40, section 1).
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|license-box' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Eight whitespace-only blocks (WS-ONLY), all of one shape: blank lines inside the code exhibit that carry a trailing space in the original (e.g. original L30, L38, L64–65) are clean blank lines in the candidate. The classifier finds no re-indentation anywhere else (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is confined to these eight lines and is on record here.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The WS-ONLY count in the classification summary is 8; the loci are the code exhibit's blank lines in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, riding inside another labeled block: the credit block's フォント line (candidate L22), which has no original counterpart and records the port's font provenance (the two faces, their host, and their license). It rides inside the CREDIT-PREVIEW block, which is why no separate annotation signature fired; the skeleton's "none" for this section does not survive contact with the bytes and is corrected here. There are no comment-form annotations (`[!-- … --]`) and no editor lines in the candidate.
- **Why:** R2: porter-added text is part of the change record; this line is also the credit the P7 rule requires for an added JP font (its accuracy is assessed in section 4).
- **Verify:** Read candidate L22; the original has no corresponding line.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's six pseudo-ref errors: class (iii), draft-form — they are the candidate's own draft-host local--code and local--files lines (sections 3–4); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (2) The render row's items, environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40) and a page-overflow reading of 851px at webkit-768 recorded for the page only; the sample's T2 run returned no machine verdict (exit 2), which the row records verbatim and this package carries as inconclusive rather than as a pass. (3) T4's two items, both dispositioned in the ledger's (c3) register: the P7 font item (section 4: credited/named but never loaded in-file, recorded without a display-affecting mark under the T4 bar) and the P9 masthead string (section 6: ruling 2, header/title language out of scope).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); ruling 2; the named KB entries), not an omission; an inconclusive render run is recorded as inconclusive, not upgraded.
- **Verify:** Each item names its deciding record above; the T4 items are LOCALIZE-ROWS row 123 and the (c3) line for theme:plant-jp.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 158): exit 1, 6 errors / 2 warns / 0 infos; all six errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN16)): FINDINGS — the page items of section 11(2); the sample run was inconclusive (exit 2), recorded as such. (c) T4/T5 (LOCALIZE-ROWS row 123): FINDINGS jointly, display-affecting findings 1 (the P7 font item); the ledger §(c3) line dispositions P7 and P9 for this theme. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +98/−93 in 40 change blocks / 8 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:plant-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 123; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibit's slug (flagged by this package)

The usage exhibit (candidate L29) was repointed from `:scp-wiki:theme:plant` to `:scp-jp:theme:plant` at creation, keeping the plain slug. The candidate's own posting name is theme:plant-jp, so the documented syntax names a page that will not exist under that name on scp-jp; the file's own delivery lines use the -jp form throughout (candidate L3, L7). This is the population-sweep family (the same shape is flagged in the parawatch-pumpkin package in this batch and was probed there against the check-wiki convention: the plain form 404s, the -jp candidate is the posting name). The ledger's determination for this theme is PASS and this package does not re-open it; the line is flagged here with its locus, and the candidate is left unedited, as the sweep repairing this family is a coordinator matter.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-plant-jp.txt` is the decoration sample the render checks ran against (its inconclusive run is recorded in section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Plant Theme
- **Author:** stormbreath
- **Source:** https://scp-wiki.wikidot.com/theme:plant — revision 28
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
