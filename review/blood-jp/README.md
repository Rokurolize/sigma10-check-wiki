# Review package — theme:blood-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:blood-jp — origin EN, population #64 [GOSIGN2-LEDGER (b) row 64]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4a1340aacc1f4fc848cd527312e91dcbdf473dfbdf1c41c335c113415fd28ae8); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 0 infos (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 69; GOSIGN2-LEDGER (b) row 64]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent page-overflow 328px@320 both engines and 799px@chromium-768; large code dump / red-swatch `div.cell` +59px warn. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 64, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 64]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 64]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:blood-jp.txt sha256:4a1340aacc1f4fc848cd527312e91dcbdf473dfbdf1c41c335c113415fd28ae8; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 64) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×5 (class (ii), section 11); the render row's candidate-inherent overflow and code-dump warning (section 11); T4's items (header text in English, the font note, and the T5 wording items including the stray bracket that stands in the bytes at candidate L640), each with its ledger disposition in section 11; the credit fields are FIXED |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:blood | theme:blood-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 12 (first translation; the candidate's credit block records 初訳時参照リビジョン: 12) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs2-en4/CACHE/orig/blood.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:blood-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 1,240 lines / 34,124 bytes | 1,253 lines / 36,733 bytes |
| SHA-256 | 1b5218d7b4e5e6a3e94b9dfd9ff1f5fa1bd1ed8de95e7cfee0dd33e07de63fcf7 | c26c68b2d2b38c0c26c5f9d68b803020365016c0cfef7c1963220739ca9d487b |

Wave history: the candidate was created by the Stage 2 EN4 integration (commit 053fd41, the LOCALIZE-S2-A wave's port), restructured by one wave commit of its own (9082176, "put the full applied CSS in the first code block" — the delivery change section 3 describes), and touched last by 1869877 (FIX-CREDIT-D, the translator-attribution normalization that swept all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A 2026 Sigma-9 theme (dark red, built as a reskin of the EN Dark theme) whose original does something none of its batch siblings do: it applies its CSS from a ~486-line module at the very top of the file, before the page's gate even opens, and only then presents the prose page with its exhibits. The port normalizes that into the campaign's delivery form — a head module importing the theme's own local--code, one interwiki-style layer at priority 1, and the full applied CSS placed in the first code block, which is what the delivery serves (the wave's own commit message says exactly this). The credit apparatus is fully replaced (bare Rate and the EN info pair out, preview credit block in), the original's hand-rolled license box becomes the JP license-box component with translated per-file entries, and the header logo variable is re-pointed from a DigitalOcean CDN copy of the BHL logo to the candidate's own attachment. What stands is recorded: the header title and subtitle stay in English in both CSS copies (ruling 2), the font stacks name no JP font (T4's minor note), and one example link in the second exhibit still carries a stray closing bracket and a retargeted Wikipedia link (T5 wording items, verified in the bytes at candidate L640). Measured churn (diff.md: +190/−177 in 55 change blocks; a GNU-diff count of the same pair gives 369 changed lines, and the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 55 change blocks — 24 specific (43.6%), 31 heuristic (56.4%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 34 |
| TRANSLATION-ANCHORED | 11 |
| DELIVERY-MOVE | 8 |
| DRAFT-HOST | 5 |
| IFTAGS | 2 |
| LICENSE-BOX | 2 |
| WS-ONLY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 31 heuristic blocks are prose translations (section 6), verified line by line; there is no residue. The 8 DELIVERY-MOVE blocks are the head module's relocation into the first code block (section 3). The 2 LICENSE-BOX blocks are the license box's conversion to the component form (section 1). The RESTORATION block is the license/citation text carried across that conversion. The 2 WS-ONLY blocks are whitespace-only and are counted in section 9. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:blood-jp; original theme:blood on scp-wiki at reference revision 12; candidate `pages/theme:blood-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame is this theme's peculiarity: the original opens with its applied CSS module (L1–486) *before* the gate, then wraps the prose page in `[[iftags +theme]]` (L488–1239) and has no tail module at all. The candidate puts the delivery frame first (head module and interwiki-style include, candidate L1–8), localizes the gate to `+テーマ` (candidate L10–1252), and keeps everything else inside it.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for blood-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L491) plus an EN info pair (`:scp-wiki:info:start`/`end`, original L496/500) around its credit prose. The candidate deletes both (BARE-RATE-DEL and INFO-DEL blocks) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) carrying the eight ruling-3 fields (title ブラッド・テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Blood Theme; 著作権者 [[*user ubergoober]]; 作成年 2026; 初訳時参照リビジョン 12; the source link, naming scp-wiki.wikidot.com/theme:blood, the recorded host, which serves the original). The ledger §(c3) line records the outcome as "charges DISPOSITIONED (…); credit fields FIXED by credit waves". T7 credit-module CSS: none added. License box: the original's hand-rolled box — a `licensebox` div with a collapsible, a ListPages citation module, and per-file entries in English (original L1223–1237) — is converted to the JP component form (candidate L1235–1250): `component:license-box-backend` with `|author=ubergoober`, the entries translated （ファイル名 / 名称 / 作者 / ライセンス / 出典）, recording chernobyl.jpg as public domain (Wikimedia Commons) and logo.svg as CC BY-SA 3.0 sourced from the SCP Foundation Wiki's CDN copy; the ListPages citation module is not carried over, its function being the component's.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate and the EN info pair are deleted rather than duplicated (KB-09; the pair is ledger class C residue). Ruling 3 fixes the eight fields. The license conversion keeps the original's per-file license facts in the JP component's form instead of a hand-rolled div.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L12–21 against the eight fields and L1235–1250 for the box.
- **Disposition:** FIXED (credit fields, credit waves); the license conversion stands in the bytes.

### 2. Includes and components

- **What:** The candidate's includes: the credit pair (section 1), one interwiki-style include (candidate L5–8, section 3), and the license-box pair (section 1). The usage line as built taught a blockquoted include, `:scp-jp:theme:blood` (candidate L27): the repoint changed the branch prefix but kept the plain slug, so it named a page that does not exist on scp-jp, not the posting form. The usage-example population sweep has since completed the name to the posting form, `:scp-jp:theme:blood-jp` (candidate L27; SWEEP-USAGE.md; canonical commit b5cb724). The original's includes are the EN info pair (deleted, section 1) and its license-box component reference inside prose. Every live include in the candidate names a `:scp-jp:` target. The grid demonstration module inside the prose (candidate L29–72, "Grid CSS - NOT part of theme", carried over from the original's second module at L508–551) is a module, not an include, and is unchanged in role.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. The usage line's repoint as built satisfied the branch half of that rule only; the sweep's completion is what brings it under it. Ruling 4 is not engaged: no new component had to be ported for this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — five includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original applies its CSS from the head module itself (original L1–486, the full CSS as live module text, outside the gate). The candidate serves the same body through the campaign's form: a head module importing the candidate's own `local--code/theme%3Ablood-jp/1` from the draft host (candidate L1–3, SELF-DELIVERY), an interwiki-style include at priority 1 naming the same /1 delivery (candidate L5–8), and the full applied CSS placed in the first code block (candidate L110–597) — the restructuring the wave's commit 9082176 names. The 8 DELIVERY-MOVE blocks are this relocation; the CSS body travels nearly verbatim (its internal changes are sections 4 and 5). The theme is Sigma-9-based, so the layering has the one own layer only: no base imports exist on either side. The page's second and third exhibits (candidate L599–620, L744–1230) correspond to the original's (L589–610, L733–1218) and are display copies, not delivery.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame; priority 1 for the own layer of a Sigma-9-based theme). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L2 and L7 live, the rest exhibit text; compare `grep -n '\[\[module' original.txt candidate.txt` for the relocation.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: no webfont is loaded on either side, and the port added no JP supplement — the stacks in the applied CSS name Latin system faces ('Lucida Sans Unicode', 'Lucida Grande', 'Times New Roman', Helvetica, Roboto; candidate L278 and L912) exactly as the original's do, so Japanese text falls back to the platform's default JP font. That is T4's item #7 for this theme ("JP font not considered"), which the row itself marks minor and the ledger carries as a note, not a charge (section 11). Assets: the header logo variable `--lgurl` is re-pointed from the original's DigitalOcean CDN copy of the BHL logo (`scp-wiki-cdn.nyc3.cdn.digitaloceanspaces.com/theme/en/black-highlighter/img/logo.svg`, original L13) to the candidate page's own attachment on the draft host (`local--files/theme%3Ablood-jp/logo.svg`, candidate L123, and repeated in the second exhibit copy at L606 region) — re-hosted, with the license entry in section 1 recording the logo's source and CC BY-SA 3.0 license. The theme's background photograph (chernobyl.jpg) is referenced from Wikimedia Commons in the license entry, as in the original.
- **Why:** P7 is the class the font note answers (no supplement added; the fallback is the platform's, and the ledger accepted the note as minor). P5 is satisfied for the logo by re-hosting rather than by disposition.
- **Verify:** `grep -n -- '--lgurl' candidate.txt` — the draft-host attachment; `grep -n 'font-family' candidate.txt` — system stacks only.
- **Disposition:** Standing (the logo re-host is in the bytes); the font note is recorded in section 11.

### 5. Header, sidebar, and site furniture

- **What:** The header variables sit in the applied CSS, twice (the delivery body and its second-exhibit copy): `--header-title: "SCP Foundation"` and `--header-subtitle: "Secure, Contain, Protect"` stand in English at candidate L121–122 and L604–605, exactly as in the original (L11–12). T4's item #9 counts the header text as kept in English at three places (the two CSS copies and the rendered header they produce) and marks it display-affecting; the ledger dispositions it under ruling 2 (section 11). The `--lgurl` change in the same block is section 4's re-host. No sidebar or topbar rule was adapted beyond what the moved CSS body already carried.
- **Why:** P9's JP-header expectation is what T4 measured; ruling 2 (header text language is translation taste, and this masthead is the Foundation's own name and motto) is the ground the ledger dispositioned it on — recorded here because the header is always displayed.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — L121–122 and L604–605, English.
- **Disposition:** DISPOSITIONED (P9, ruling 2, GOSIGN2-LEDGER §(c3) line for this theme).

### 6. Text translation

- **What:** The prose is translated throughout (the 34 TRANS-UNANCHORED heuristic primaries and 11 TRANSLATION-ANCHORED blocks, verified line by line): the intro (which keeps its EN absolute link to the Dark theme this one reskins, as the original had it), the usage text, the examples, the grid demonstration's labels, the license entries (section 1), and the exhibit prose. English survives only as quotation: the credit fields (candidate L16, L20), the header strings (section 5), and the CSS bodies, which are code. One translated line carries a defect of wording, counted in section 7: the unvisited-link example at candidate L640.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings).
- **Verify:** The pairs are diff.md's body sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One link was deliberately retargeted and carries a wording defect, both verified in the current bytes. The link-style examples include an unvisited-link specimen: the original links the EN Wikipedia's 1921–22 Clarkson Golden Knights season article (original L630); the candidate links the Japanese Wikipedia's Clarkson Golden Knights article instead (candidate L640, the LINK-REPOINT block) — a reasonable JP target — but the candidate's line ends `…でしょう。]]`, a stray extra closing bracket after the link's own `]`. These are T4/T5's recorded items for this theme (the row's L640 numbering is the candidate's, and both items stand there today). The ledger's line 1701 adjudication covers them: "T5 stray-bracket items are recorded wording items without a display-affecting mark". The remaining links are sound: the credit source link (candidate L20, recorded host, serves); the intro's Dark theme link (candidate L23, EN absolute, kept from the original, serves); the license entries' Commons and CC links (candidate L1242, L1247). The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no unintended divergence.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard. The Wikipedia repoint follows it; the stray bracket is a wording blemish the ledger has already weighed.
- **Verify:** `sed -n '640p' candidate.txt` against `sed -n '630p' original.txt`.
- **Disposition:** DISPOSITIONED (the T5 wording items, per the ledger's line-1701 adjudication).

### 8. Structure

- **What:** Apart from the delivery relocation (section 3), the skeleton corresponds: prose sections in order, the grid module in place, three code exhibits on each side with corresponding roles (applied CSS; the short second exhibit, whose opening tag carries a trailing space on both sides, original L589 and candidate L599; the large third exhibit), footnoteblock, and the license box at the tail. The RESTORATION block is the license/citation text carried across the box's conversion (section 1). Exhibit census: three exhibits on each side, no exhibit added, dropped, split, or merged; the first exhibit's *role* changed (it is now the delivery body as well as the display copy), which is section 3's change, not a restructure of content.
- **Why:** R3 requires the census before a restructure is narrated; here the census shows correspondence.
- **Verify:** `grep -n '\[\[code' original.txt candidate.txt` — three exhibits each, at the positions above.
- **Disposition:** Standing (correspondence established).

### 9. Formatting only

- **What:** Two whitespace-only blocks (the WS-ONLY primaries), in the module-boundary regions where the delivery relocation re-anchored the text. They carry no content change, and they are the whole of this section: the classifier finds no re-indentation (0), so the R7 follow-up-diff hazard is confined to those two spots.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json (2 whitespace-only blocks).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate contains no `[!-- ... --]` comments and no 訳注 footnotes; the port's judgments (the English header, the font stacks, the Wikipedia repoint) are not announced in the page — their record is the T4 row, the ledger lines, and this package.
- **Why:** R2: porter-added text is part of the change record; its absence is stated, not assumed.
- **Verify:** `grep -n '訳注\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (as an absence, stated).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's five errors: pseudo-ref ×5, all class (ii) — the candidate's own draft-host delivery references (section 3) and its own attachment line (section 4); there is no class (i) error and no hotlink error (this theme's T1 row is the cleanest in the batch). The 1 warn is recorded verbatim in T1-ROWS row 69 and is not classified. (2) The render row's items: a candidate-inherent page overflow of 328px at the 320 viewport (both engines) and 799px at chromium-768, and a warning for the large code dump / the red-swatch grid cells (+59px) — the lane's own classification is candidate-inherent (the theme's wide code exhibits and demo grid are its design), and no credit-modal line exists in this theme's row. (3) T4's items and their ledger dispositions (§(c3) line for this theme, with the line-1701 adjudication): the header text — DISPOSITIONED (ruling 2); the asset hosts — DISPOSITIONED (class (ii); the logo has since been re-hosted in the bytes, section 4); the font note — recorded as minor; the T5 wording items (the stray bracket and the Wikipedia target at candidate L640) — recorded wording items without a display-affecting mark; and the credit fields — FIXED by the credit waves. The theme's determination is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a lane-classified inherent property is recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1 and 3); item 2 recorded as candidate-inherent by the render lane; credit fields FIXED.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 69): exit 1, 5 errors / 1 warn / 0 infos; all five errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): FINDINGS — the candidate-inherent overflow and code-dump warning of section 11(2); engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 64): FINDINGS jointly, display-affecting findings 1; the ledger §(c3) line records the theme's charges as DISPOSITIONED and its credit fields as FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +190/−177 in 55 change blocks; the GNU-diff count of the same pair is 369 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:blood-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 64; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The usage example at candidate L27 as built read `> @@[[include :scp-jp:theme:blood]]@@`: the porting wave's repoint changed the branch prefix but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:blood-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-blood-jp.txt` is the decoration sample the render checks ran against; it belongs to this theme's record but carries no port change of its own to explain here. The original-side sample `pages/theme-decoration-sample-blood.txt` is the campaign's mirror-side fixture, likewise outside the port. The re-hosted logo (section 4) is an attachment of the candidate page itself, recorded in the license box, not a separate repo file. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Blood Theme
- **Author:** ubergoober
- **Source:** https://scp-wiki.wikidot.com/theme:blood — revision 12
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
