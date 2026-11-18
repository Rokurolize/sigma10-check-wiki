# Review package — theme:paramycota-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:paramycota-jp — origin EN, population #120 [GOSIGN2-LEDGER (b) row 120]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 375138353a1210dfe22635e8ac8ff3bd613f5366d257ab423cc7d4f8c500dfea); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 15 errors / 3 warns / 1 info (pseudo-ref×15); standing classes dispositioned in register c1 [T1-ROWS row 155; GOSIGN2-LEDGER (b) row 120]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form); T3 broken SCP logo image (deferred asset), content readable. [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 120, source LOCALIZE-S2-B]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 120]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 120]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:paramycota-jp.txt sha256:375138353a1210dfe22635e8ac8ff3bd613f5366d257ab423cc7d4f8c500dfea; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 120) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×15 (classes (ii)/(iii), section 11); the render row's items (KB-40 / KB-32 and a deferred asset, section 11). **FLAGGED by this package** — the two usage exhibits name the plain slug on the JP side (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:paramycota | theme:paramycota-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 37 (first translation; the candidate's credit block records 初訳時参照リビジョン: 37) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-paramycota.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:paramycota-jp.txt`, copied at worktree HEAD 9068bb7 |
| Lines / bytes | 1,002 lines / 29,088 bytes | 1,010 lines / 30,786 bytes |
| SHA-256 | 32b7aeebdde35d40a5bfae8dcbbd7f9c1f9ea2be97ed1a8d51e4b52b9e1aefb7 | aa674b6b8b70e5fb527c525d96dcc564160170b04ef453bfc06b6d833f4f73bd |

Wave history: the candidate was created by the Stage 2 EN16 integration (commit 88d2d99, the LOCALIZE-S2-B wave's port, lane-dsh-en16) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose paramycota hunk is the translator-field normalization. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. (The verdict stamp cites T1-ROWS row 155 for the T1 baseline; the theme's population number is 120. The row offset is the register's own, recorded here so the citation can be followed.)

## Summary

The cleanest port in this batch, and the one that shows the campaign's parameter-gated variation mechanism carried correctly. The theme ships an ACS recolor preset behind the same comment-gate trick our-open-veins uses for its color variation (`[!-- {$recolor-acs}` … `[!----]`), and here the candidate carries the gated module byte-identical, so the documented preset still activates. Everything else is the standing set, executed completely: the bare Rate becomes the preview credit block; the original's license-box-theme include becomes the JP backend box with its seven asset entries translated in place (artwork names glossed, committee names localized, source links untouched); the header title and subtitle variables are translated; the theme-squares exhibit's color names are translated while every variable and hex value is preserved; and the delivery pair takes the JP forms, the module import on the draft host and the frame already naming the production host. The two flags are the population family's: both usage exhibits (the plain include and the recolor preset's include) name the plain slug on the JP side. Measured churn (diff.md, the generator's difflib count with autojunk off: +171/−176 in 82 change blocks / 19 hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 82 change blocks — 57 specific (69.5%), 20 heuristic (24.4%), 5 residue (6.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 36 |
| TRANS-UNANCHORED | 21 |
| DRAFT-HOST | 14 |
| INCLUDE-REPOINT | 6 |
| LINK-REPOINT | 3 |
| HEADERVAR | 2 |
| COMMENT-TEXT | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 5 residue blocks (B8, B12, B23, B29, B56) are one-line translation pairings the anchor test missed (a section heading, two theme-squares parameter names, and two sample strings), resolved in the appendix; no residue block hides a structural change. The 14 DRAFT-HOST primaries are the CSS's asset url() re-hosts, one per locus (section 4). The specific share (69.5%) is the batch's highest, reflecting a port with no restructures: the exhibit census of section 8 is one-to-one throughout. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:paramycota-jp; original theme:paramycota on scp-wiki at reference revision 37; candidate `pages/theme:paramycota-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order is the original's own: the two header includes, the delivery module, the frame, the gated recolor module, then the tag gate (original L1–25; candidate L1–22), with the gate's tag localized to +テーマ (candidate L22).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2.
- **Verify:** The sources.tsv row for paramycota-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module Rate]]` directly after the gate (original L25), with the attribution in prose ("Made by [[*user tachymelia]]", original L27). The candidate deletes the bare Rate (block B5's BARE-RATE-DEL) and installs the preview credit block (candidate L24–33) carrying the eight ruling-3 fields (title Paramycotaテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Paramycota Theme; 著作権者 [[*user tachymelia]] — matching both the prose attribution and the license box's author parameter; 作成年 2026; 初訳時参照リビジョン 37; the source link https://scp-wiki.wikidot.com/theme:paramycota, whose host matches the sources.tsv record, its label the single word ソース）. The license zone: the original opens its box with `:scp-wiki:component:license-box-theme` (original L946) and closes with license-box-end (original L1001); the candidate substitutes the settled JP form, `:scp-jp:component:license-box-backend |author=tachymelia]]` on one line (candidate L954) with `:scp-jp:component:license-box-end` (candidate L1009), and translates the seven entries in place: field labels localize （ファイル名 / 名称 / 著者 / ライセンス / ソースリンク / 補足）, the artwork names keep their originals with Japanese glosses where the name is descriptive ("Mushrooms vector image（キノコのベクター画像）"), the committee artwork names are translated （分類委員会， 倫理委員会， O5司令部， RAISA kept), the authors and licenses are carried exactly (Rob Hille CC BY-SA 3.0; Olena Panasovska CC BY 3.0; Unattributed / Public Domain; EstrellaYoshte CC BY-SA 3.0), and every source link keeps its target, including the bare local `desk-of-junior-designer-s-yvonne` links, which resolve on the reader's own wiki on both sides. T7 credit-module CSS: none on either side.
- **Why:** P3/T1 with KB-09 (the preview module is rate-bearing; a kept bare Rate would double-render). Ruling 3 fixes the eight fields and the translator form; the file's last commit (1869877) is that form arriving. T4: the license box takes its settled JP form (the theme-form include is the foreign variant; KB-60), with entries preserved, not rewritten.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L24–33 against the eight fields; compare the entries at original L946–1001 and candidate L954–1009 entry by entry (seven on both sides).
- **Disposition:** FIXED by construction at creation (P3 credit fields and the T4 box form; T4 judged the theme PASS with 0 display-affecting findings, LOCALIZE-ROWS row 120).

### 2. Includes and components

- **What:** Six repoint blocks. The two header includes the theme auto-applies are repointed (`:scp-wiki:component:centered-header-sigma-9` and `:scp-wiki:component:toggle-sidebar` → `:scp-jp:` forms, candidate L1–2), and the prose note that users must not include them themselves is translated with them (candidate L66). The frame include keeps the original's bare form, `[[include component:interwiki-style …]]` (candidate L6–8; its delivery aspect is section 3). The theme-squares exhibit include is repointed to `:scp-jp:component:theme-squares` with its color-name parameters translated and every variable and hex value preserved (candidate L38–56; the translation aspect is section 6). The image-block exhibits keep the original's bare `component:image-block` form (candidate L86, L105; the original's are bare as well), which resolves on the reader's own wiki on both sides. The credit and license includes are section 1. No component swap (T8) was needed.
- **Why:** P1 (KB-15): includes name the JP counterpart that exists; bare names that already resolve locally are carried, not decorated.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the full list, JP-side or bare-local as above.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The original's module CSS imports its stylesheet in a hybrid form, `https://scp-wiki.wikidot.com/local--code/theme:paramycota/1` (original L4, the page host carrying a local--code path); the candidate imports `local--code/theme%3Aparamycota-jp/1` from the draft host (candidate L4). The frame's `theme=` names the same /1 on the production host form, scp-jp.wdfiles.com (candidate L8), so this candidate's two delivery lines sit one in each standing class ((iii) for the module, (ii) mechanics for the frame), the same mixed state as pack-of-peanuts in this batch. The theme's second module is the gated recolor preset (original L11–20): a `[[module css]]` restating the anomaly-bar container's five color variables, wrapped in the comment gate `[!-- {$recolor-acs}` … `[!----]`. The candidate carries the whole block byte-identical (candidate L10–20) — the parameter name, the gate markers, and every variable value — so the preset its documentation describes (candidate L94–95) still activates exactly as the original's does. This is the batch's control case for the mechanism: the same trick our-open-veins' port dropped.
- **Why:** P4/T9 and P6/T3 for the import form and the frame. The gated module is content the original carries, and the localize.md closing rule (preserve what the candidate carries) applies to it with full force: a parameter-gated module is invisible to a skim, which is why it is named here explicitly.
- **Verify:** `diff <(sed -n '11,20p' original.txt) <(sed -n '10,20p' candidate.txt)` — the gated block corresponds line for line (the candidate's block starts one line earlier in the file); `grep -n 'local--code' candidate.txt` — L4 and L8.
- **Disposition:** DISPOSITIONED (the draft-host module line, class (iii); the frame's production-host form, class (ii)).

### 4. Fonts and assets

- **What:** No font load changes: neither side carries a font @import or @font-face of its own (the theme inherits the Sigma base's faces), so no JPFONT signature fired and there is no KB-16 question to answer — the skeleton's "none" for this section is correct, and its ground is this inheritance, stated here rather than left blank. The asset work is the fourteen DRAFT-HOST loci: the theme's own images (scp.png, clavarioid.svg, the mycelium photograph, and the CSS's remaining url() targets) re-host from the original's file areas to the draft host's `theme%3Aparamycota-jp/` folder, filenames unchanged. Two of the original's asset URLs use the page-host form (`scp-wiki.wikidot.com/local--files/…`, e.g. --lgurl at original L333); their candidates take the wdfiles form like the rest (candidate L341). The license entries' external source links (Wikimedia Commons, the Noun Project, publicdomainvectors) are not assets of the theme and keep their targets (section 1).
- **Why:** P5/KB-17: a theme's own assets re-host to the JP side; third-party source links are attribution, not delivery, and stay.
- **Verify:** `grep -n 'sigma10-jp-test.wdfiles.com/local--files' candidate.txt | wc -l` and `grep -n '@import' candidate.txt` (only the delivery import of section 3).
- **Disposition:** Applied; the draft-host asset URLs are DISPOSITIONED (class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** The header variables are translated (block B64's HEADERVAR span): `--header-title: "SCP Foundation"` → `"SCP財団"` and `--header-subtitle: "Sustain Consume Proliferate"` → `"維持、消費、増殖"` (original L331–332 → candidate L339–340), and the two logo variables in the same block (--lgurl, --shroomurl) take the draft-host asset form (section 4). The custom-header exhibit's placeholder strings are translated as exhibit text (block B18: "Put your title here!" → ここにタイトルを入れてください！, and its three companions, candidate L74–77). Because the values were translated, ruling 2 is not engaged and KB-57 does not apply. The header and sidebar components themselves are section 2; no P8 layout adaptation was needed.
- **Why:** P9/T6: the header variables are the theme's visible title surface, and this port localizes them.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — the live pair at L339–340 and the exhibit pair at L74–75.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The translation is the port's bulk and its best-anchored: 36 TRANSLATION-ANCHORED label counts (prose paragraphs, the usage instructions, the collapsible section titles — How to Use → 使用方法, Wiki Formatting → Wiki構文, Special Formatting → 特殊構文， Table Formatting → 表構文 — and the sample strings) plus the one-line TRANS-UNANCHORED grain (21 counts), each verified against the mirror for this README. Two translation choices deserve a reviewer's note, both recorded rather than judged. The theme-squares color names are translated as names, not transliterated blindly: Button Mushroom → ツクリタケ (the species' Japanese name; the artwork's license entry keeps Agaricus bisporus), Growth Medium → 培地, Hyphal Habitat → 菌糸の生息地, Plaque Bacque → プラーク・バック, Slidebare Sepia → スライドベア・セピア, with variables and hex values untouched. And the original's pun in the usage prose ("Shrimply put", original L57) is rendered plainly （要するに, candidate L63): the joke does not survive, the instruction does. R1 in-CSS text: two section comments are translated inside the CSS; the remaining comments are structural labels carried in English, porter-visible only.
- **Why:** P10 and KB-18 (reader-visible strings localize). Exhibit parameters that carry display names are reader-visible strings; parameters that carry mechanism (variables, hex values) are not text and do not translate.
- **Verify:** The pairs are diff.md's body sections in order; the theme-squares parameters are at original L31–50 and candidate L38–56 side by side.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme PASS with 0 display-affecting findings (LOCALIZE-ROWS row 120).

### 7. Links

- **What:** Three LINK-REPOINT blocks. In the sample tabview exhibit, the original's bare local joke link `[[[scp-7764|http://www.beenz.com]]]` becomes the EN article's full URL, `[[[https://scp-wiki.wikidot.com/scp-7764|http://www.beenz.com]]]` (original L110 → candidate L118), so the exhibit's link lands on the serving original rather than on a same-named JP page. In the license zone (blocks B76, B77), the entries' source-link lines are carried with their targets unchanged and their field labels translated (section 1); the classifier files them here because the link lines moved with their entries. The credit block's source link (candidate L32) names the original on scp-wiki.wikidot.com, the host the campaign's provenance records name for it. No link in the candidate is dead on the evidence of the mirror.
- **Why:** P11: prose and exhibit links take the JP counterpart or the serving original, under the dead-reference evidence standard.
- **Verify:** `grep -n 'beenz.com' candidate.txt` — candidate L118.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds in full: the exhibit census corresponds one to one (the theme-squares swatch exhibit, the usage exhibit, the custom-header and custom-sidebar exhibits, the tabview and formatting samples, the ACS recolor section with its gated module, and the CSS code exhibit), the gated module of section 3 included, and the JP corrections arrive as the head delivery pair, the credit swap, and the license-box form swap. The classifier's EXHIBIT-RESTRUCTURE label rides inside multi-label blocks whose primaries are the repoints and translations of sections 2 and 6; adjudicated against the census, no exhibit was dropped, replaced, or reordered, so the R3 question does not arise for this theme.
- **Why:** R3 exists to force the census; here the census, not the label, decides, and it passes.
- **Verify:** Compare `grep -n '\[\[code\|theme-squares\|recolor-acs' original.txt candidate.txt` — the sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation anywhere in the pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. No comment-form annotations (`[!-- … --]` outside the recolor gate, which is mechanism, not annotation), no editor lines, and no porter-added record text: this port's additions all live inside the settled credit and license forms of section 1. The check was made against the bytes, not the skeleton.
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` — only candidate L10, the recolor gate opener.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) T1's fifteen pseudo-ref errors and three warns: the candidate's own draft-host local--code and local--files lines (class (iii), sections 3–4) and the frame's production-host theme= line (class (ii) mechanics, section 3); the posting procedure rewrites or re-hosts the draft lines, and fix lanes never "fix" them in the candidate. (2) The render row's items, all environment, capture, or asset layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the T3 capture's broken SCP logo image, recorded in the row as a deferred asset with the page's content readable (the --lgurl asset of section 5; its draft-host copy did not serve in that capture).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS (cited as row 155 in the stamp) and register (c1).
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS, cited as row 155 in the verdict stamp): exit 1, 15 errors / 3 warns / 1 info; the errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN16)): FINDINGS, the three items of section 11(2), all dispositioned or deferred in the row; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 120): PASS jointly, display-affecting findings 0; the ledger (c3) register carries no disposition line for this theme because nothing needed one. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +171/−176 in 82 change blocks / 19 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:paramycota-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 120; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibits' slug (flagged by this package)

Both usage exhibits were repointed from `:scp-wiki:` to `:scp-jp:` at creation, keeping the plain slug: the plain include exhibit, `@@[[include :scp-jp:theme:paramycota]]@@` (candidate L64), and the recolor preset's exhibit, `{{@@[[include :scp-jp:theme:paramycota | recolor-acs = --]]@@}}` (candidate L95). The candidate's own posting name is theme:paramycota-jp, so both documented syntaxes name a page that will not exist under that name on scp-jp; the file's own delivery lines use the -jp form throughout (candidate L4, L8). The second exhibit is the sharper case: it is the activation syntax for the gated module of section 3, so a reader following it fails twice over — the include names the wrong page, and only the right page's file carries the gate the parameter opens. This is the population-sweep family (the same shape is flagged in the plant, parawatch-pumpkin, and pack-of-peanuts packages in this batch). The ledger's determination for this theme is PASS and this package does not re-open it; the lines are flagged here with their loci, and the candidate is left unedited, as the sweep repairing this family is a coordinator matter.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-paramycota-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Paramycota Theme
- **Author:** tachymelia
- **Source:** https://scp-wiki.wikidot.com/theme:paramycota — revision 37
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
