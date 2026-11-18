# Review package — theme:shark-punching-centre-bhl-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:shark-punching-centre-bhl-jp — origin EN, population #135 [GOSIGN2-LEDGER (b) row 135]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 6eaed19dc43acd17588896a621988e22fd8354686d420df9edce7c153b7c34fe); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 2 warns / 2 infos (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 120; GOSIGN2-LEDGER (b) row 135]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only (sidebar-position machine warn at 1366 is a Sigma-9 baseline mismatch; T3 confirms sidebar visibly at left JP position, mobile button opens); sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host; T3 clean on both pages (specimens 1–31 render; decorative logo 404s owner-deferred; WebKit stray glyph cross-cutting). [RENDER-ROWS-RERUN16 (EN19) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (EN19)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 135, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 135]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 135]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:shark-punching-centre-bhl-jp.txt sha256:6eaed19dc43acd17588896a621988e22fd8354686d420df9edce7c153b7c34fe; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 135) |
| Standing items | **One FIXED, rest DISPOSITIONED** — the credit fields were completed by a fix wave (P3 FIXED, section 1); the T1 pseudo-refs are draft form (class (iii), section 11); the render record that governs is the RERUN16 re-measurement, whose items are the environment families of section 11. One item is flagged in the per-theme record: the usage exhibit's plain-slug self-reference |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:shark-punching-centre-bhl | theme:shark-punching-centre-bhl-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 22 (first translation; the candidate's credit block records 初訳時参照リビジョン: 22) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-s2-2/mirrors/shark-punching-centre-bhl.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:shark-punching-centre-bhl-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 406 lines / 9,227 bytes | 417 lines / 11,045 bytes |
| SHA-256 | edcf4b961b3e5dba2e6f482beb7d32ea2e22ee3194c900af7c2ef7eb36ed12e8 | 0f26f7b0b7645751d6e23bdb0ee86ec3f414556badf62a6af5b962452f0f332b |

Wave history: the candidate was created by the Stage 2 EN19 integration (commit 765e2f8, the RENDER-S2-2 wave's port) and has exactly one later commit, 666f543 (FIX2-CREDIT), which completed the credit block of section 1. Provenance caveat recorded in review/sources.tsv: the original has been superseded upstream since the reference revision, and a follow-up diff artifact (diff-shark-punching-centre-bhl-from21.txt) sits in the campaign record (the K5a-i treatment); this package documents the port against the frozen revision-22 mirror, which is the revision the port was made from.

## Summary

A Black Highlighter derivative: the theme imports the BHL base stylesheets and layers an SPC (Shark Punching Centre) skin over them — header art, logo variables, and a long documentation body of component exhibits. The port repoints the base delivery to the JP BHL mirror host (scp-jp.github.io), repoints every frame and exhibit include to its `:scp-jp:` form, re-hosts the theme's four own images to the candidate's draft-host file area, translates the header strings and the whole documentation body, and — after the localize check found six of the eight credit fields missing — had its credit block completed by the FIX2-CREDIT wave, which the ledger records as P3 FIXED. The render record for this theme is one of the RERUN16 re-measurements, which supersedes its first render row wholesale; section 12 reads verification through that record. One flag is recorded: the usage exhibit for the theme itself names the plain slug.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 79 change blocks — 33 specific (41.8%), 45 heuristic (57.0%), 1 residue (1.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 47 |
| COMMENT-TEXT | 23 |
| TRANSLATION-ANCHORED | 20 |
| INCLUDE-REPOINT | 6 |
| DRAFT-HOST | 6 |
| DELIVERY-HOST | 5 |
| EXHIBIT-RESTRUCTURE | 4 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the four EXHIBIT-RESTRUCTURE blocks are all mere include repoints inside exhibit regions (B3, B5, B12, B78 — the exhibit census in section 8 shows no restructuring), the classifier's known false-fire for this label. The INFO-DEL primary (B10) is likewise a repoint plus translation of the info exhibit, not a deletion (section 2). The one residue block (B8) is a single translated line (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:shark-punching-centre-bhl-jp; original theme:shark-punching-centre-bhl on scp-wiki at reference revision 22; candidate `pages/theme:shark-punching-centre-bhl-jp.txt`. Provenance route: derived from the original at the reference revision by the RENDER-S2-2 wave (sources.tsv kind: standard). The upstream page has moved on since (the K5a-i note in the Provenance caveat); the port and this package are anchored to revision 22. The tag gate localizes as usual (block B1: `[[iftags +theme]]` → `[[iftags +テーマ]]`).
- **Why:** Section 0 declares the provenance route and the frozen baseline; the gate's tag is P2 (iftags tag localization).
- **Verify:** The sources.tsv row for shark-punching-centre-bhl-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original carries no credit block at all — its head is the delivery module and frames, and its body opens with the rating exhibit (original L41–46). The candidate inserts the preview credit block after the frames (candidate L40–49, block B7): the eight ruling-3 fields （タイトル SPC Black Highlighter Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 SPC Black Highlighter Theme; 著作権者 [[*user GreenGolem]]; 作成年 2021; 初訳時参照リビジョン 22; the source link, host-verified in section 7). At localize time the block stood at two of eight fields (the LOCALIZE row's pattern-3 charge: six of eight missing, the panel incomplete though rendering); the FIX2-CREDIT wave (commit 666f543) completed it, and the ledger records the outcome as P3 FIXED. The author field names GreenGolem, the theme's author; the second hand the original names, JackalRelated, is an image credit (the high-resolution SPC logo, original L105), and that credit survives translated in the exhibit prose (candidate L123). The rating exhibit itself is carried translated (original L41–46 → candidate L52–57: 評価：, the live `[[module Rate]]`, クレジットモジュール付き評価：), and no T7 credit CSS supplement exists on either side (neither file carries credit-module rules; the theme's credit styling comes from its BHL base).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form and ruling 3 fixes its eight fields; a two-field block renders an incomplete panel, which is the failure the fix wave removed. The title fields keep the theme's English proper name, as ruling 3's fields record names rather than translate them.
- **Verify:** Read candidate L40–49 against the eight fields; `git log --oneline -- pages/theme:shark-punching-centre-bhl-jp.txt` shows the FIX2-CREDIT commit.
- **Disposition:** FIXED (P3, credit waves; GOSIGN2-LEDGER §(c3)).

### 2. Includes and components

- **What:** Every include is repointed to its `:scp-jp:` form, and the classifier's EXHIBIT-RESTRUCTURE labels on four of them are adjudicated in the class summary. The head frames (original L30, L35 → candidate L30, L35, blocks B3, B5) name `:scp-jp:component:interwiki-style` with their theme targets repointed in step (section 3). The info exhibit trio (block B10: original L47–51 → candidate L58–62) is repointed `:scp-wiki:info:` → `:scp-jp:info:` with its placeholder texts translated （ページ情報。 / ページの追加情報。) — the block's INFO-DEL primary is a mislabel in substance: nothing is deleted. The theme-squares exhibit (block B12) is repointed with its colour-name parameters translated. The tail frame is repointed (block B78, section 3). The usage exhibits (block B20, section 8 of the per-theme record) repoint the base include correctly and the theme's own include with a flagged name. No component swap (T8) occurs.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; every component named here has one. Ruling 4 is not engaged: the BHL base is a stylesheet delivery, not a component port (section 3).
- **Verify:** `grep -n '\[\[include' candidate.txt` — frames at L30/L35, credit pair at L40/L49, info trio at L58–62, theme-squares at L66, exhibits at L96–97, tail frame at L414; no `:scp-wiki:` include remains.
- **Disposition:** Applied; the theme exhibit's name form is the flagged item of the per-theme record.

### 3. Delivery and code loading

- **What:** The topology is preserved exactly (the classifier's pass: three components on each side, no moves). The head module (original L2–29 → candidate L2–29) imports the BHL base's two minified stylesheets; their host is repointed from the EN BHL delivery `nu-scptheme.github.io` to the JP BHL mirror `scp-jp.github.io` (blocks B2, B4, B6 — the two @imports and the frames' theme targets), and the two head frames follow at priorities 1 and 2. The theme's own CSS is the code exhibit (original L286–396 → candidate L297–407, 110 lines each). The tail module imports the theme's own /1 delivery with its host repointed from scp-wiki.wdfiles to the candidate's draft host (block B77, candidate L410–413), and the tail frame names the same delivery at priority 3 (blocks B78, B79, candidate L414–417).
- **Why:** P4/T9: the base must be the delivery that exists in the JP environment — for BHL that is the JP mirror host the ported base theme itself uses — and P6/T3 for the frame priorities, which keep base (1, 2) below own (3) as the original orders them. The own-delivery host form is KB-41, class (iii).
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` — two mirror imports, two frame targets, one own-delivery pair; priorities read at candidate L30–38 and L414–417.
- **Disposition:** DISPOSITIONED (draft-host own delivery, class (iii)); the base-host repoint is applied.

### 4. Fonts and assets

- **What:** The theme declares no fonts of its own (its faces arrive with the BHL base delivery of section 3). Its own images are re-hosted to the candidate page's draft-host file area, four in all: the BHL logo in the body exhibit (block B16: original L74, an scp-wiki.wdfiles URL → candidate L85, the draft-host `local--files/theme%3Ashark-punching-centre-bhl-jp/black-highlighter-logo.svg`), the high-resolution SPC logo (block B24: the original's bare relative `[[=image spc-logo.png]]` at original L106 becomes the full draft-host URL at candidate L117), the header art in the `--logo-image` variable (block B70, candidate L302), and the band image (block B76: original L332 → candidate L343). Each move also upgrades the scheme to https where the original was http.
- **Why:** P5: images a theme loads must not depend on the original wiki's file area in the JP environment; the candidate's own file area is the re-hosting target, and its draft-host form is the class (iii) posting state. The relative-filename original (spc-logo.png) is the case that makes the rule concrete: on scp-jp it would resolve against the including page, not the theme.
- **Verify:** `grep -n 'wdfiles' candidate.txt` — every remaining wdfiles reference is the candidate's own draft-host area; the four loci are named above.
- **Disposition:** DISPOSITIONED (draft form, class (iii)); the re-hosting itself is applied.

### 5. Header, sidebar, and site furniture

- **What:** The header variables sit inside the code exhibit (block B70: original L291–293 → candidate L302–304): `--logo-image` re-hosted (section 4), `--header-title: "SPC DATABASE"` → `"SPCデータベース"`, and `--header-subtitle: "SHARK PUNCHING CENTER"` → `"サメ殴りセンター"`. The SPC acronym is retained as the organization's proper mark in both strings. Sidebar behaviour is a render-record item: the RERUN16 re-measurement's machine warn on sidebar position at 1366px is a Sigma-9 baseline mismatch, and its T3 read confirms the sidebar visibly at the left JP position with the mobile button opening it (section 11).
- **Why:** P8 (KB-19): header strings are reader-visible furniture and are localized; the acronym is a proper noun, not untranslated prose.
- **Verify:** `grep -n -- '--header-' candidate.txt` — the two translated strings at L303–304.
- **Disposition:** Applied (header strings); the sidebar warn is DISPOSITIONED as a baseline artefact (RERUN16 record).

### 6. Text translation

- **What:** The documentation body is translated throughout: the rating and info exhibits (section 1/2), the theme-colour exhibit's parameters, the usage and component documentation (the long run of single-line blocks B13–B68 — 47 TRANS-UNANCHORED and 20 TRANSLATION-ANCHORED blocks in total across body and code), the collapsible labels and image credits (block B24), the link-exhibit texts (block B25, section 7), and the CSS comments inside the code exhibit (blocks B69, B71–B75, COMMENT-TEXT). The anchored blocks were verified line by line; the unanchored mass is single-line prose and comment translation of the same shapes, with no content class dropped (the census in section 8).
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings, including the exhibit labels a user reads while copying components).
- **Verify:** The pairs are diff.md's body sections in order; the code comments read at candidate L299–320 against original L288–309.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit block's source link (candidate L48) names `https://scp-wiki.wikidot.com/theme:shark-punching-centre-bhl` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is ソース. The one prose link repoint is in the link exhibit (block B25: original L111–112 → candidate L122–123): the "this link does exist" example target moves from `scp-wiki.wikidot.com/adoption-poster-phoebe` to its scp-jp counterpart, with both example texts translated (the non-existent-link example stays a non-resolving wikilink by design, as the original designs it).
- **Why:** P11: prose links take the JP counterpart where one exists; an exhibit demonstrating link behaviour must demonstrate it against the environment the reader is in.
- **Verify:** `grep -n 'adoption-poster' candidate.txt` — one hit, the scp-jp host.
- **Disposition:** Applied.

### 8. Structure

- **What:** No restructuring in substance. The exhibit census corresponds one to one: rating exhibit, info exhibit, theme-squares exhibit, logo collapsible, link exhibit, usage exhibits, and the code exhibit are present on both sides in the same order; the only insertion is the credit block (section 1), and the only reordering is none. The four EXHIBIT-RESTRUCTURE labels are the repoints adjudicated in the class summary. Selector and variable names inside the CSS are preserved; the CSS changes are the re-hosts of section 4, the header strings of section 5, and comment translation.
- **Why:** R3: the census is what separates a repoint (this theme) from a silent restructure or drop (the failure class I charges); here the census closes clean.
- **Verify:** Compare the heading and include sequences of the two files (`grep -n '^+\|\[\[include\|\[\[collapsible'`) — they correspond at the loci named in sections 1–3.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0) in this pair.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (no WS-ONLY label).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. An explicit check of the candidate finds no `[!-- ... --]` porter comment and no editor line with no original counterpart; the classifier's ANNOTATION signature does not fire.
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground, all read through the RERUN16 record (section 12 explains why that record governs). (1) T1's five pseudo-ref errors: class (iii) — the draft-host references of sections 3 and 4. There are no hotlink errors: the base delivery host is the JP mirror, and the theme's own images are re-hosted. (2) The page-side render items: the runtime-hotlink site-theme chain only (KB-40, the environment layer: the check site's own theme chain, not this candidate), and the sidebar-position machine warn, a Sigma-9 baseline mismatch whose T3 read confirms the JP position (section 5). (3) The sample-side items: the credit-modal errors (KB-32, ruling 5 — the sample's preview-form credit include has no modal mechanism), the page-overflow pair 337px@320 and 389px@375 (KB-33/KB-34 cross-cutting families), the hotlink chain, and a sample font host line (the sample environment's own font delivery).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 120): exit 1, 5 errors / 2 warns / 2 infos; all five errors are pseudo-ref, the class (iii) item of section 11(1); there is no class (i) error. (b) T2/T3 render: this theme is one of the 17 RERUN16 themes, so the operative record is RENDER-ROWS-RERUN16 (lane RENDER-S2-2, EN19), which supersedes its RENDER-ROWS-2 row wholesale under the six supersession rules (the newest same-lane record governs; RENDER-ROWS-RERUN16-PARTIAL.md is excluded by name everywhere); its content is the items of section 11(2)/(3), all dispositioned, with T3's sidebar confirmation as recorded in section 5. (c) T4/T5 (LOCALIZE-ROWS row 135): FINDINGS jointly, display-affecting findings 1 — the pattern-3 credit charge, which the ledger §(c3) line records as P3 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +150/−145 in 79 classifier change blocks / 12 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; where two records cover one theme, the supersession rule decides which one a reader should trust, and it is stated rather than left implicit.
- **Verify:** Re-run the checker on `pages/theme:shark-punching-centre-bhl-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 135; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibit's self-reference (flagged)

The usage exhibits (block B20: original L85–86 → candidate L96–97) repoint both includes to `:scp-jp:`. The base include names `theme:black-highlighter-theme`, the JP port's real posting name, and is correct. The theme's own include names `:scp-jp:theme:shark-punching-centre-bhl` — the plain slug, where the candidate's posting name is theme:shark-punching-centre-bhl-jp. The original's exhibit names `:scp-wiki:theme:shark-punching-centre-bhl` (original L86), that page's real name on its own wiki, so the port's repoint changed the site prefix and kept a name that, on the target wiki, will not be the posted page's name. Probes made for this package (2026-11-17): both `https://scp-jp.wikidot.com/theme:shark-punching-centre-bhl` and `https://scp-jp.wikidot.com/theme:shark-punching-centre-bhl-jp` return 404 today, because the theme is not yet posted in either name; the probe therefore cannot decide the point, and the flag rests on the posting-name convention, the same ground on which the M-pure-3 batch flagged five instances of this shape and a population sweep is repairing the family. This package does not edit the candidate; the flag is recorded so the sweep's list is complete.

### Record note — the vendored LOCALIZE row truncates the credit charge

The vendored LOCALIZE-ROWS copy of this theme's row ends its pattern-3 item with "pattern 3 deviation: …" — the deviation's text is cut off in the authority file itself, so what the deviation was cannot be recovered from the record. The bytes govern: the credit block as it stands carries all eight fields (section 1), and the ledger's §(c3) line records P3 FIXED without qualification. The truncation is noted here so a reader does not mistake the row's silence for a second, unresolved credit item.

## Appendix — residue blocks

| Block | Span | Resolution |
|---|---|---|
| B8 | orig 43-43 → cand 54-54 | A single translated line inside the rating exhibit (`**Rating:**` → `**評価:**`) that the aligner left unlabeled; its neighbours carry the exhibit's labels (B7, B9). Narrated in section 1. |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-shark-punching-centre-bhl-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** SPC Black Highlighter Theme
- **Author:** GreenGolem
- **Source:** https://scp-wiki.wikidot.com/theme:shark-punching-centre-bhl — revision 22
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
