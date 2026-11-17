# Review package — theme:another-night-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:another-night-jp — origin CN, population #164 [GOSIGN2-LEDGER (b) row 164]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 164]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 15 errors / 3 warns / 1 info (hotlink×10, pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 141; GOSIGN2-LEDGER (b) row 164]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-rate + sidebar-not-opening (all combos) + runtime-hotlink site-theme chain with cdn.jsdelivr.net; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-E (CN1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-E (CN1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 163, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 163]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 164]
- Computed against: canonical commit 8c62b7b5207f684c8373dfe00f28b90427d28027; candidate file pages/theme:another-night-jp.txt sha256:8d99d4f19b3d0839bd3135cac73aa3fe816c6a5f0684df4bde1f6a07ea51f229; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 164) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×10 and pseudo-ref ×5 (classes (ii)/(iii)); the render row's hidden-rate, sidebar, and hotlink-chain items (ledger (c2), section 11); the sample's missing machine verdict is a coverage caveat, not a defect; T4's findings dispositioned per the ledger (c3) line (P5, class (ii) / KB-58) and the class outcomes (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:another-night | theme:another-night-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 1 (the candidate's credit block records 初訳時参照リビジョン: 1) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-another-night.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:another-night-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 766 lines / 25,148 bytes | 782 lines / 23,632 bytes |
| SHA-256 | dcf1a535ce634032ea3d8fefc02f614ea659a49671ae57f5c657dd26ff4cbedb | 8d99d4f19b3d0839bd3135cac73aa3fe816c6a5f0684df4bde1f6a07ea51f229 |

Wave history: the candidate was created by the Stage 2 CN1 integration (commit 4a2f4a5); FIX-P4 (f1138e4, pattern-4 repoint of base-theme CSS imports to the JP port candidates) and FIX4-IWA (8c62b7b, the interwiki frame added under KB-07a; the stamp's computed-against commit) touched it later. The original was superseded upstream after revision 1; a follow-up diff artifact (`diff-another-night-from1.txt`) is held in the campaign record (K5a-i, per review/sources.tsv).

## Summary

A full in-place port, the opposite shape from the EN batch's delivery pages: the candidate keeps the original's body, its tabview of exhibits, and its six code blocks, and translates them where they stand. The head changes are the standard ones (basalt include swapped to basalt-jp, five self-delivery imports repointed from the CN wiki to the draft host, the Rate-and-CN-credit furniture replaced by the preview credit block, the frame added by FIX4-IWA). The body is a translation job with three adjudicated subtleties: the theme's signature epigraph strings stay in Chinese in its `:root` defaults (section 6), five retained strings take Japanese glyph forms (R5), and its background images still serve from CN sandbox hosts under a class (ii) disposition (section 4). Measured churn (diff.md, the generator's difflib count with autojunk off: +145/−129, 274 changed lines in 62 change blocks; a GNU-diff count of the same pair gives 234 changed lines — the difference is alignment choice across the translated body, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 62 change blocks — 42 specific (67.7%), 16 heuristic (25.8%), 4 residue (6.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 17 |
| INCLUDE-REPOINT | 9 |
| COMMENT-TEXT | 7 |
| COLON-ENC | 7 |
| EXHIBIT-RESTRUCTURE | 7 |
| DELIVERY-HOST | 6 |
| DRAFT-HOST | 6 |
| SELF-DELIVERY | 6 |
| GLYPH-FORM | 5 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the seven EXHIBIT-RESTRUCTURE primaries all co-fire with INCLUDE-REPOINT inside exhibits that the census shows present on both sides — they are repoints, not restructurings (section 8). The four residue blocks resolve as two `http:` → `https:` scheme upgrades in exhibit include parameters (B41, B50; section 7) and two code-tail boundary artefacts (B61, B62; section 9). The COMMENT-TEXT blocks are R1 comment translations (section 6). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:another-night-jp; original theme:another-night on scp-wiki-cn at reference revision 1; candidate `pages/theme:another-night-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN1 wave (sources.tsv kind: standard; no production JP counterpart exists, so the R4 adoption question does not arise). The frame order differs from the EN batch's: the original opens with the hidden basalt include and its self-delivery module, then its gate; the candidate keeps that order (candidate L1–23), and the interwiki-style frame was added after the module (candidate L24–27) by the FIX4-IWA wave, ahead of the localized gate (candidate L29).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for another-night-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a `[[module Rate]]` in a right-aligned div (original L24–26) plus a `:scp-wiki-cn:credit:start` block whose body is an image-attribution list (the theme's backgrounds are CC-licensed photographs, credited by file name, author, and license). The candidate replaces the furniture (block B7): the Rate is deleted, and a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L31–41) carries the eight ruling-3 fields (タイトル 迷离夜 版式; 翻訳責任者 AI; 翻訳年 2026; 原題 迷离夜 版式; 著作権者 Gumillea; 作成年 2025; 初訳時参照リビジョン 1; the source link, candidate L40, naming `scp-wiki-cn.wikidot.com/theme:another-night` — the original's recorded host — with the theme's name as its label rather than the word ソース, a CN-wave label form recorded as it stands). The attribution list itself survives as translated body prose directly below, under a 画像の出典 heading (candidate L43 ff.): file names, image titles, authors (Riosolar, Vmenkov), licenses (CC BY-SA 4.0 / 3.0), and the Commons source links, all carried. No credit-module CSS supplement was added. License box (T4): neither side carries one; the CC licenses here are image licenses, carried in the attribution prose, not a page license box.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09), and the CN credit module is branch furniture, not JP furniture. Ruling 3 fixes the eight fields. The attribution list is license substance, so it is preserved entire and translated, not dropped with the module that carried it.
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns nothing for the old furniture; read candidate L31–55 against the fields and the original's list (original L27–55).
- **Disposition:** FIXED (credit fields, by the credit waves; the ledger (c3) outcomes for this theme's row).

### 2. Includes and components

- **What:** Nine INCLUDE-REPOINT blocks. The load-bearing one is B1: the hidden delivery include, `:scp-wiki-cn:theme:basalt` → `theme:basalt-jp`, parameter unchanged (`darkmode=a`, original L2 → candidate L2). The other eight are inside the exhibit body: the usage and ACS exhibits' includes repointed from `:scp-wiki-cn:` forms to their `:scp-jp:` or bare `component:` counterparts (B30, B37, B39, B42, B46, B48, B51, and the credit-adjacent B7), including the source-code exhibit's `component:coltop`/`component:colend` pair (candidate L270, L780). Every live include in the candidate names a JP-side target or a bare component name, as the original's bare forms did.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists; T8 for the basalt swap (ruling 4: the base is the dependency, its JP port exists). No foreign include is kept as an exception.
- **Verify:** `grep -n '\[\[include' candidate.txt` against the original's list — the sequences correspond, with targets repointed.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original self-delivers: a head module imports its own code blocks /1 (live) and /2–/5 (inside `{$option}` comment toggles) from `scp-wiki-cn.wikidot.com/local--code/theme:another-night/` (original L5–21). The candidate keeps the mechanism and repoints it (blocks B2–B6): all five imports name `sigma10-jp-test.wdfiles.com/local--code/theme%3Aanother-night-jp/` with the same indices and the same comment toggles (candidate L6–21). The candidate's six code blocks stay in the page (the main block at candidate L271–716, the option blocks behind it), so the /1–/5 addresses resolve to this page's own blocks as the original's did. The interwiki-style frame (candidate L24–27, priority 1, `theme=` naming the same /1) was added by FIX4-IWA (8c62b7b) under KB-07a; the original has no frame. FIX-P4 (f1138e4) is the wave that repointed the base-theme CSS imports to the JP candidates (the basalt include of section 2).
- **Why:** P4 (own-code delivery served from JP hosts) and P6/T3 (the frame). The draft-host form of the five imports and the frame line is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting. Keeping the option toggles as comments preserves the theme's delivery semantics exactly — the four optional blocks are off by default on both sides.
- **Verify:** `grep -n 'local--code' candidate.txt` — six lines (five imports, one frame), all draft-host; compare original L5–21.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Load (B53, JPFONT-LOAD): at the main code block's head the candidate adds a Google Fonts `@import` for Noto Serif JP (400;700, candidate L272) and re-homes the theme's Latin display face, Afacad Flux, to Google Fonts (candidate L274). Stacks: the one literal stack, `--title-font: 'Afacad Flux', 'Source Han Serif CN VF', serif` (candidate L276), keeps the CN serif as its second family and names no JP family — so the added JP load is not wired into the theme's own title stack, and Japanese in titles resolves through the base's stacks and the generic fallback. That is the precise residue of LOCALIZE-ROWS row 163's item (c) (no JP font guarantee), stated against the current bytes: the load exists, the stack guarantee is partial. Assets: the theme's background images serve from CN sandbox hosts in the `:root` defaults (candidate L278–281: `scp-sandbox-3.wikidot.com` ×2, `scp-sandbox-3.wdfiles.com` ×1, `scpsandboxcn.wikidot.com` ×1 — the night-panorama and subway photographs of the credit list), and the exhibit icon addresses include `scp-wiki.wdfiles.com` forms (section 7). Together with the delivery lines these are T1's ten hotlink errors. Colons (KB-01): seven COLON-ENC blocks (B54–B60) encode the page-name colon in `local--code`/`local--files` addresses inside the code blocks (`theme:another-night` → `theme%3Aanother-night`).
- **Why:** P7/T5 with KB-16 (the font load gap): the load half was applied; the stack half is recorded as found, not rounded up to a fix. P5 with KB-17/KB-58: the sandbox-hosted backgrounds are the original's own delivery state for its images; the settled disposition is class (ii), re-hosted at posting, and the ledger (c3) line dispositions this theme's P5 exactly so.
- **Verify:** `grep -n '@import\|--title-font' candidate.txt` against the lines above; `grep -o 'scp-sandbox[^/]*' candidate.txt | sort | uniq -c`.
- **Disposition:** Font load applied, stack gap recorded; the sandbox asset URLs DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header defaults are string variables in its `:root` (candidate L285–295): `--prologue`, `--prologue-author`, `--introduction`, and `--subtitle-content`, all carrying Chinese text (section 6), plus their `-setting` toggles, carried unchanged. No `--header-title`/`--header-subtitle`/`--logo-image` override exists on either side; the header image is the `--bg-img` variable of section 4. No sidebar or topbar adaptation was made; the render row's sidebar item is section 11's.
- **Why:** P9/T6 names no override change here. The defaults' language is a translation question, charged to section 6 (R1) with ruling 2 as its disposition ground, not a furniture change.
- **Verify:** Read candidate L283–296 against the original's `:root` in diff.md.
- **Disposition:** Standing (values); the strings' language is section 6's item.

### 6. Text translation

- **What:** The body is translated in place, in four counted groups. Seventeen TRANSLATION-ANCHORED blocks and twenty-two TRANS-UNANCHORED blocks (B8–B52 passim): the usage documentation, the tabview exhibits, the ACS and component samples, each read against the mirror for this README. Seven COMMENT-TEXT blocks (B18–B24) are R1 in-CSS/comment text: the documentation's embedded comments and code-adjacent strings, translated with the body. One CONTENT-STRING block (B23) is a reader-visible `content:`-class string. Five GLYPH-FORM blocks (B38, B40, B44, B47, B49) are R5: retained Chinese strings whose glyphs were converted to Japanese forms (simplified/traditional characters replaced by their shinjitai counterparts) rather than translated — the string is the same word in Japanese dress. What was NOT translated: the four epigraph/default strings of section 5 (candidate L285–291: the Pound epigraph lines 面庞在人潮中明灭 / 湿黑枝条上，花瓣朵朵, the author line, and the subtitle - 芸芸众生 -) remain in Chinese, as does the credit block's title field (candidate L33), which is the theme's name. LOCALIZE-ROWS row 163's item (a) charges exactly this: the delivery defaults' Chinese slogans are inconsistent with the (translated) documentation. The inconsistency is real and is recorded here as found; its disposition ground is ruling 2's family (the theme's signature epigraphs are its design text, like a header title), and the ledger determination is PASS.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings) for the translated groups; R1 and R5 name the two sub-shapes the classes would otherwise blur. The retained epigraphs are stated separately because a reviewer checking "was this string translated or left?" needs the answer per string, not per theme.
- **Verify:** A Han-character scan of candidate.txt returns the credit fields, the epigraph defaults of section 5, and the R5-converted strings; the translated pairs are diff.md's body sections in order.
- **Disposition:** Standing (the port itself); the retained Chinese defaults recorded with their ground.

### 7. Links

- **What:** Two residue blocks resolve here (B41, B50): inside the ACS exhibits, the anomaly-class-bar icon addresses are upgraded `http://` → `https://` (original L188 and L237 → candidate L203 and L252), the only scheme changes in the file. The credit attribution's Commons links (candidate L50, L55 and their kin) are carried unchanged — they name the images' source pages on commons.wikimedia.org, which is where those records live. The credit source link (candidate L40) names the original's recorded host (section 1). No prose link in the candidate targets a CN-wiki page.
- **Why:** P11 for the carried links (the serving original or the record's home). The scheme upgrades are the T12 shape in reverse: an `http:` address that the port touched takes its `https:` form, so no http residue remains in the file.
- **Verify:** `grep -n 'http://' candidate.txt` returns nothing; the two upgraded lines are candidate L203 and L252.
- **Disposition:** Standing; no dead link carried, no http residue.

### 8. Structure

- **What:** The closing rule holds. The candidate preserves the original's structure: hidden include, delivery module, gate, credit, attribution prose, tabview body, and the six code blocks in the original's order, with the JP corrections arriving as the head supplement (frame, credit block) and in-place repoints, not as a rebuild. The exhibit census is one-to-one: the tabview and its tabs, the ACS exhibits, the component samples, and the source-code exhibits are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise. The seven EXHIBIT-RESTRUCTURE primaries all co-fire with INCLUDE-REPOINT inside kept exhibits and adjudicate to section 2.
- **Why:** R3 exists to force this adjudication; here the census, not the label, decides, and it decides for preservation.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|component:col' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two boundary artefacts (B61, B62) at the file's tail: the last code block's closing braces realign against the candidate's added lines (original L761–762 → candidate L776–778) and the closing `component:colend` include sits one blank line further down (original L765 → candidate L780–781). No line's content changes in either block. The classifier finds no whitespace-only block pair and no re-indentation (0 and 0), so the R7 hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The tail sections of diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no `[!-- ... --]` translator note and no port-provenance comment: `grep -n '\[!--\|訳注' candidate.txt` returns nothing. The port's in-file explanations are its translated documentation itself; attribution rides in the credit block's fields (section 1).
- **Why:** R2: porter-added text is part of the change record; here the check was run and the answer is genuinely none, stated with its ground rather than left blank.
- **Verify:** The grep above.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's ten hotlink errors: class (ii), posting-procedure — the sandbox-hosted background images and exhibit asset addresses (section 4); posting re-hosts them. Its five pseudo-ref errors: the five draft-host `local--code` imports (section 3), class (iii) draft form (KB-41). (2) The render row's items, all DISPOSITIONED in the ledger (c2) register as one entry: page hidden-rate, sidebar-not-opening (all combos), and the runtime-hotlink site-theme chain with cdn.jsdelivr.net — candidate-own foreign/sandbox delivery hosts, posting-time rewrite or original-state delivery class (T1 class (ii); KB-41/KB-54 family), with the register's note that the pages render styled today and no error-box defect arises from these hosts. (3) The sample's T2 run returned no machine verdict (render_check exit 2, no summary): a coverage caveat recorded in the same register, KB-44 family — a measurement gap, not a theme defect, and not silently upgraded to a pass. (4) T4's findings (LOCALIZE-ROWS row 163): the P5 asset item DISPOSITIONED (class (ii) / KB-58) in the ledger (c3) line; the epigraph-language item (a) is section 6's, grounded on ruling 2's family; the font item (c) is section 4's, half-applied in the bytes as recorded there.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 3, 4, and 6.
- **Disposition:** DISPOSITIONED (items 1–4).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 141): exit 1, 15 errors / 3 warns / 1 info; the errors are hotlink ×10 and pseudo-ref ×5, the standing classes of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E): FINDINGS, the items of section 11(2)–(3), all dispositioned; the sample's missing verdict is recorded as a caveat, not a result. (c) T4/T5 (LOCALIZE-ROWS row 163): FINDINGS jointly, display-affecting findings 4, dispositioned as in section 11(4) and the ledger §(c3) line (P5 DISPOSITIONED, class (ii) / KB-58). The original having been superseded upstream after revision 1, the follow-up diff artifact `diff-another-night-from1.txt` is held in the campaign record (K5a-i). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +145/−129 in 62 change blocks; the GNU-diff count of the same pair is 234 changed lines, and the difference is alignment choice across the translated body, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:another-night-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 164; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The epigraph defaults (the strings that stayed Chinese)

This theme's design text is two lines of Ezra Pound's "In a Station of the Metro" in Chinese translation, carried as CSS string defaults (`--prologue`, `--introduction`, candidate L285–289) with the subtitle 芸芸众生 ("the teeming multitude") at L293. The port translated everything around them — documentation, exhibits, credit prose — and left them. The localize lane charged the inconsistency (row 163, item (a)): a reader of the documentation meets a Japanese theme whose delivered defaults are Chinese. The countervailing fact is also in the bytes: the lines are a quotation, attributed in the file itself to Pound's poem (`--prologue-author`, candidate L287), and the theme's identity is that quotation in that language, the way a header title is a name. This package does not settle the taste question; it records that the strings are Chinese by retention, not by oversight — the translator demonstrably reached them (the surrounding `:root` lines are the port's own edited region) and left them — so a future editor who translates them is making a design decision, not repairing a miss.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-another-night-jp.txt` is the decoration sample the render checks ran against (its T2 state is the caveat of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The candidate layers over `pages/theme:basalt-jp.txt` by the include of section 2; the base's own package is a separate record (class U). There are no companion fragments and no inbound-link repairs in other candidates for this theme.
