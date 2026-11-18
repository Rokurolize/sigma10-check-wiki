# Review package — theme:black-diamond-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:black-diamond-jp — origin EN, population #61 [GOSIGN2-LEDGER (b) row 61]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 312c584f52defbeaceb9b6ad7e0c86e00bf317f0a9cce002885113bd42e99b66); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 0 warns / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 66; GOSIGN2-LEDGER (b) row 61]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent large page-overflow 567/577px@320/375 (page) and 579/589px (sample) + white ☰ toggle overlapping body text at 320. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 61, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 61]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 61]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:black-diamond-jp.txt sha256:312c584f52defbeaceb9b6ad7e0c86e00bf317f0a9cce002885113bd42e99b66; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 61) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (class (iii)); the render row's candidate-inherent overflow and toggle-overlap items (ledger (c2), section 11); T4's findings per the ledger (c3) line (P1, posting-procedure convention class) and the class outcomes (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:black-diamond | theme:black-diamond-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16 (the candidate's credit block records 初訳時参照リビジョン: 16) | — |
| Source of this copy | Campaign mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:black-diamond-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 557 lines / 14,623 bytes | 568 lines / 15,899 bytes |
| SHA-256 | 74977569d2688b2fb8fa94895ce21e223600194acbc6afdcf155595cda55fa68 | 4ad907fd17d6bcf7ddc85c246a1d58f9f5231e2b8dbca8ecb9436c58baf6da86 |

Wave history: the candidate was created by the Stage 2 EN4 integration (commit 053fd41), normalized for code-block tabs by the same wave (ab523f4), and touched by FIX-CREDIT-D (1869877, translator attribution normalization; the stamp's computed-against commit).

## Summary

An EN theme for the Black Diamond Billions canon (MC&D-adjacent, blue-and-gold against the usual purple), built on the Sigma Plus component. The port's shape is relocation: the original keeps its two load-bearing includes at its tail (the sigma-plus include and its self-delivery module), and the candidate moves both to the head in JP form (the sigma-plus-jp component candidate and a draft-host delivery module), replaces the centered Rate with the preview credit block, re-homes the font supply from Bunny Fonts to Google Fonts with JP faces added, and restructures the original's tail attribution prose into a license box. The one open question the localize lane raised, whether the sigma-plus component exists on production JP, is answered by the campaign's own convention: the component is ported alongside the theme, and the include resolves at posting. Measured churn (diff.md, the generator's difflib count with autojunk off: +87/−76, 163 changed lines in 19 change blocks; a GNU-diff count of the same pair gives 149 changed lines — the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 19 change blocks — 12 specific (63.2%), 6 heuristic (31.6%), 1 residue (5.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 8 |
| DRAFT-HOST | 4 |
| EXHIBIT-RESTRUCTURE | 4 |
| INCLUDE-REPOINT | 2 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| SIGMA-PLUS-JP | 2 |
| WS-ONLY | 3 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the single residue block (B6) is the code banner's added port line (section 10). Three of the four EXHIBIT-RESTRUCTURE primaries (B16, B18, and B2) adjudicate against the census: B2 is the usage-include exhibit repointed (section 2), and B16/B18 are the tail attribution prose restructured into the license box (section 1) — a real restructuring, but of attribution furniture, not of exhibits dropped or replaced. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:black-diamond-jp; original theme:black-diamond on scp-wiki at reference revision 16; candidate `pages/theme:black-diamond-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN4 wave (sources.tsv kind: standard; no production JP counterpart exists, so the R4 adoption question does not arise). The frame order is the port's own: the candidate opens with its two component includes (candidate L1–2), its delivery module and frame (candidate L4–11), then the localized gate (candidate L13); the original opens with its gate and Rate, and keeps its includes at its tail.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for black-diamond-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original has no credit block: a centered `[[module rate]]` (original L3–5) and attribution in prose ("This theme was created by me, [[*user Fish^12]]", original L9). The candidate deletes the Rate and carries a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L15–24) with the eight ruling-3 fields (タイトル ブラック・ダイヤモンド テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Black Diamond Theme; 著作権者 [[*user Fish^12]]; 作成年 2025; 初訳時参照リビジョン 16; the source link, candidate L23, naming `scp-wiki.wikidot.com/theme:black-diamond` — the original's recorded host). No credit-module CSS supplement was added. License box (T4): the original's tail carries attribution prose for its three gold-ornament images; the candidate restructures that prose into a `:scp-jp:component:license-box-backend`/`license-box-end` pair (candidate L545–567, blocks B15–B18) with the same substance in field form: ornamenta/b/c.png, their original Commons file names, authors recorded as unknown (antique ornament images), license CC0 1.0, and the Commons source links.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09), and ruling 3 fixes the eight fields. The license box is T4's form applied to attribution the original already carried as prose — restructured, not invented.
- **Verify:** Read candidate L15–24 and L545–567 against original L3–9 and the tail prose in diff.md.
- **Disposition:** FIXED (credit fields, by the credit waves; the ledger (c3) outcomes for this theme's row).

### 2. Includes and components

- **What:** The candidate's head carries the port's two component includes: `[[include component:sigma-plus-jp]]` (candidate L1) and `[[include :scp-jp:component:toggle-sidebar]]` (candidate L2). The sigma-plus line is the relocation of the original's tail include (`:scp-wiki:component:sigma-plus`, original L548) in JP-candidate form: the component is ported alongside the theme as its own candidate, and the include names that candidate. LOCALIZE-ROWS row 61's item #11 charged two things here: prose links to EN components (the translated body at candidate L30 still links `scp-wiki.wikidot.com/component:sigma-plus` and `component:toggle-sidebar` as documentation references, carried from original L11 — links about the components, not includes of them), and the then-unconfirmed existence of the component on production JP. The usage exhibit (block B2) is repointed in branch only as built: the include specimen a reader copies read `:scp-jp:theme:black-diamond` — the repoint changed the branch prefix from the original's `:scp-wiki:` (original L16) but kept the plain slug, so it named a page that does not exist on scp-jp. The usage-example population sweep has since completed the name to the posting form, `:scp-jp:theme:black-diamond-jp` (candidate L35; SWEEP-USAGE.md; canonical commit b5cb724), and this package documents the corrected candidate. No other live include names a foreign target.
- **Why:** P1 (KB-15) for the repoints; the usage exhibit's repoint as built satisfied the branch half of that rule only, and the sweep's completion is what brings the specimen under it; the component-alongside convention (the campaign's standing rule that required components are ported with the theme rather than parking it) for the sigma-plus-jp form, with its production resolution charged to the posting procedure — exactly the ledger (c3) line's P1 disposition (posting-procedure convention class). KB-64 is the pattern family for the sigma-plus credit/component shape.
- **Verify:** `grep -n 'sigma-plus' candidate.txt` — the live include at L1 in -jp form, the prose links at L30; compare original L548.
- **Disposition:** DISPOSITIONED (P1, posting-procedure convention class).

### 3. Delivery and code loading

- **What:** The original self-delivers from its tail module (original L550–553, topology module-css [550,553]) importing its code block. The candidate moves delivery to the head: a `[[module CSS]]` (candidate L4–6) importing `local--code/theme%3Ablack-diamond-jp/1` from the draft host, the interwiki frame after it (candidate L8–11, priority 1, same address), and the original's tail module leaves with the tail collapse (block B19, original L546–557 → candidate L568). Inside the code, three DRAFT-HOST blocks (B12–B14) repoint the ornament image addresses to the draft host's `local--files` for this theme. T1's four pseudo-ref errors are these draft-host addresses (import, frame, and code URLs).
- **Why:** P4 (own-code delivery served from JP hosts) and P6/T3 (the frame); the draft-host form is KB-41, class (iii), rewritten at posting — the localize row's own note (draft host to be replaced by `scp-jp.wdfiles.com` at posting) states the same procedure.
- **Verify:** `grep -n 'local--code\|local--files' candidate.txt` — all name the draft host; compare original L550–553.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Font supply is re-homed and extended (block B7). The original imports three families from fonts.bunny.net (STIX Two Text, Roboto Flex, Zen Old Mincho; original L59–61, single weights). The candidate imports the same three from fonts.googleapis.com with their variable ranges (candidate L78–80) and adds a JP load under its own comment (`/* 日本語フォント (JP localization) */`, candidate L82): Noto Sans JP and Noto Serif JP (candidate L83–84). Zen Old Mincho, the original's own Japanese face, is retained in the set. Stacks in the code name these families (the FONT-IMPORT/JPFONT-LOAD labels ride with one COMMENT-TEXT for the added comment). Assets: the ornament images' code addresses are the draft-host repoints of section 3; the localize row also records an upstream gap, the undefined `--teac` variable, which is the original's own (present in neither file's definitions) and is noted for a keep-or-drop judgment before posting — an upstream-state item, not a port change.
- **Why:** P7/T5: same families, JP-reachable host, JP faces added with their loads and stacks consistent (KB-16). The Bunny host is a font CDN the JP environment does not use; Google Fonts is the campaign's settled supply.
- **Verify:** Read candidate L77–84 against original L58–61.
- **Disposition:** Font rewrite applied; the `--teac` item is standing (upstream's own, posting-time judgment per the row).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header text stays English: LOCALIZE-ROWS row 61's item #9 (header in English, display-affecting, judgment requested). The candidate adds no `--header-title` translation; its header identity is the theme's own (the Sigma Plus header with the theme's colors). The sidebar furniture is the toggle include at candidate L2 (section 2). The render row's toggle item is section 11's.
- **Why:** P9/T6 names no override change; the header language is dispositioned under ruling 2 (header/title language is translation taste, out of scope for migration correctness), the same ground the ledger's class outcomes apply to this row's family.
- **Verify:** The header rules in the candidate's code against the original's in diff.md.
- **Disposition:** DISPOSITIONED (ruling 2 family).

### 6. Text translation

- **What:** The short body is translated whole: the introduction (candidate L26–30, including the canon link repointed in text to the JP hub form's title while its address stays the EN hub page, as the original's does), the usage prose, and the exhibits — eight TRANS-UNANCHORED blocks with one COMMENT-TEXT (the font comment of section 4). The heading どうやって儲けるのか？ (candidate L26) translates the original's "HOW DO I MAKE MONEY?" — the body heading is translated even though the header furniture of section 5 is not, a distinction the bytes keep cleanly.
- **Why:** P10 and KB-18 (reader-visible strings).
- **Verify:** The body sections of diff.md in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L23) names the original's recorded host (section 1). The body's canon-hub and component links (candidate L28, L30) name scp-wiki pages, carried from the original: they are references to the EN canon hub and component pages, the records' homes, not delivery. The license box's Commons links (candidate L552, L558, L564) name the ornament images' source pages. No `http://` address remains in the candidate.
- **Why:** P11: links name the serving original or the record's home.
- **Verify:** `grep -n 'http://' candidate.txt` returns nothing.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** The closing rule holds with the relocations charged to their sections: includes and delivery moved from tail to head (sections 2–3), the attribution prose restructured into the license box (section 1), the gate and credit at the head, the body and code in the original's order, `[[/iftags]]` closing at candidate L568. The exhibit census is one-to-one: the usage exhibit, the code exhibit, and the tail attribution content are all present on both sides. The EXHIBIT-RESTRUCTURE labels adjudicate as stated in the class summary.
- **Why:** R3 exists to force this adjudication; the census decides for preservation with relocation, not deletion.
- **Verify:** Compare the section sequences of the two files in diff.md.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Three WS-ONLY blocks (B9–B11) inside the code: line pairs differing only in whitespace. The EN4 wave's tab normalization (commit ab523f4) is the file-level formatting event; it produced no re-indentation signature in the classifier's counts (0 blocks), and the three whitespace pairs are its residue at the diff level.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The WS-ONLY sections of diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One, in CSS comment form: the code block's banner, which in the original ends at its author line (original L56, "by Fish^12"), gains a second line in the candidate (candidate L75): "Ported for SCP-JP (theme:black-diamond rev 16)" — the port's provenance and its reference revision, recorded at the head of the CSS it describes. `grep -n '\[!--' candidate.txt` returns nothing; the annotation's form is a comment line because its position is inside the code banner. The font comment of section 4 (candidate L82) is a section label for the added loads, counted there.
- **Why:** R2: porter-added text is part of the change record; its form follows its position, and the check for the bracket form was run and is negative, stated with its ground.
- **Verify:** Read candidate L74–75 against original L56.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four pseudo-ref errors: class (iii) draft form (KB-41), the delivery addresses of section 3. (2) The render row's items, DISPOSITIONED in the ledger (c2) register: candidate-inherent large page-overflow (567/577px at 320/375 on the page; 579/589px on the sample) and the white ☰ toggle overlapping body text at 320 — recorded by the lane itself as candidate-inherent (by-design wide content), KB-37 family. "Candidate-inherent" here means the theme's own design produces the overflow on narrow screens, as the original's does; it is not a port-introduced breakage. (3) T4's findings (LOCALIZE-ROWS row 61): the component item DISPOSITIONED (P1, posting-procedure convention class, section 2); the header item under ruling 2 (section 5); the draft-host replacement note is the class (iii) procedure of section 3; the `--teac` item is upstream's own (section 4).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 2 and 3.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 66): exit 1, 4 errors / 0 warns / 1 info; the errors are pseudo-ref ×4, the standing class of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS, lane RENDER-S2-A): FAIL/FAIL with FINDINGS, the items of section 11(2), dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 61): FINDINGS jointly, display-affecting findings 1, dispositioned as in section 11(3) and the ledger §(c3) line (P1 DISPOSITIONED, posting-procedure convention class). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +87/−76 in 19 change blocks; the GNU-diff count of the same pair is 149 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:black-diamond-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 61; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The usage example at candidate L35 as built read `> @@[[include :scp-jp:theme:black-diamond]]@@`: the porting wave's repoint changed the branch prefix from `:scp-wiki:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:black-diamond-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-black-diamond-jp.txt` is the decoration sample the render checks ran against (its overflow figures are section 11(2)). And `pages/component:sigma-plus-jp.txt` is the ported component candidate the head include names (section 2): it belongs to this theme's record as its required companion, carries its own port record, and is the concrete form of the campaign's rule that required components are ported alongside their themes. There are no other companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Black Diamond Theme
- **Author:** Fish^12
- **Source:** https://scp-wiki.wikidot.com/theme:black-diamond — revision 16
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
