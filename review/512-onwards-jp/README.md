# Review package — theme:512-onwards-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:512-onwards-jp — origin EN, population #47 [GOSIGN2-LEDGER (b) row 47]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7e414dd1567df10bb6d8dbd9bdffaad6c50fb883c0d07498fafafa0a6ae9c001); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 25 errors / 1 warn / 1 info (hotlink×23, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 47; GOSIGN2-LEDGER (b) row 47]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent page-overflow 1415px@1366 + 425–428px@320/375 both engines (fixed min-width), floatbox right +142px; runtime-hotlink cdn.scpwiki.com. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 47, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 47]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 47]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:512-onwards-jp.txt sha256:7e414dd1567df10bb6d8dbd9bdffaad6c50fb883c0d07498fafafa0a6ae9c001; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 47) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×23 (class (ii)) and pseudo-ref ×2 (class (iii)/(ii)); the render row's overflow and hotlink items (section 11); T4's four findings dispositioned per the ledger (c3) line and FIX3-S2EN §5/§6.11 (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:512-onwards | theme:512-onwards-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-512-onwards.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:512-onwards-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 496 lines / 14,086 bytes | 1,356 lines / 36,970 bytes |
| SHA-256 | f231a50fc40d3290b44090a5828033d2248c11f5faf795459a2d06dfc2e427bd | bb0714240d769dcc00be675f9e1db888c2cfa5f526d7bc0654ead4f81e218aca |

Wave history: the candidate was created by the Stage 2 EN batch 1 wave (commit 3205f27) and has two later commits: f931619 (FIX2-COLON, unencoded-colon URL fixes) and a497307 (FIX4-MECH, duplicate-@import removal, KB-65; the stamp's computed-against commit). The original was superseded upstream after revision 10; a follow-up diff artifact (`diff-512-onwards-from10.txt`) is held in the campaign record (K5a-i, per review/sources.tsv).

## Summary

A Basalt reskin whose port is dominated by one delivery decision. The original imports EN Basalt's /1, /3, /5 code blocks and serves its own CSS from a `[[code]]` block; the candidate instead inlines the Basalt-JP base layer into a single `[[module CSS]]` and moves the theme's own code block into the same module behind it, so most of the +1,028 added lines are the base layer's CSS, not new theme content. The theme's own layer is recognizably itself (the `--onwards-*` variables and the memo-div rules, moved at 0.991 similarity). The candidate body is lean: credit block, a one-sentence description, a usage line, and a base note, where the original carries a full exhibit body; the exhibit census is stated in section 8 and the per-theme record, because no campaign record names that drop. Measured churn (diff.md, the generator's difflib count with autojunk off: +1,028/−168, 1,196 changed lines in 68 change blocks / 6 diff sections; a GNU-diff count of the same pair gives 1,140 changed lines — the difference is alignment choice around the moved code, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 68 change blocks — 65 specific (95.6%), 2 heuristic (2.9%), 1 residue (1.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 56 |
| TRANS-UNANCHORED | 5 |
| WS-ONLY | 4 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| HEADERVAR | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE count is one true move and a long artefact tail. The true move is the theme's own code block (original L220–486 → the tail of the candidate's module, from candidate L1086; topology similarity 0.991). The remaining DELIVERY-MOVE primaries pair original body lines with lines of the inlined Basalt layer by token similarity; they are not moves, and the body content they sit on is adjudicated in sections 6 and 8. The 2 EXHIBIT-RESTRUCTURE primaries (B16, B62) sit at the exhibit body's boundaries and adjudicate to section 8's census. The single residue block (B61, original L163–214) is the memo-div exhibit deletion of section 8. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:512-onwards-jp; original theme:512-onwards on scp-wiki at reference revision 10; candidate `pages/theme:512-onwards-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch 1 wave (sources.tsv kind: K5b-3 — the candidate layers over theme:basalt-jp, and this package's diff covers the theme's own layer plus the inlined base it carries; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order changed: the original opens with its tag gate `[[iftags +theme]]` (original L1) ahead of its Basalt-import module (L2–6); the candidate opens with the interwiki-style frame (candidate L1–4) and places the localized gate after it (candidate L6).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3), and the layering is the K5b-3 cross-theme form of T9.
- **Verify:** The sources.tsv row for 512-onwards-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L9) plus a `:scp-wiki:info:start`/`end` pair (original L11–13) whose body is one line of prose naming the author. The candidate deletes both (blocks B2–B3) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying the eight ruling-3 fields (タイトル 512以降テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 512 Onwards Theme; 著作権者 WaylandLaurencePan; 作成年 2026; 初訳時参照リビジョン 10; the source link, candidate L16, naming `scp-wiki.wikidot.com/theme:512-onwards` — the original's recorded host). No credit-module CSS supplement was added: `grep -n 'creditButton\|creditRate' candidate.txt` returns nothing, because the inlined Basalt base carries the family's own credit styling. License box (T4): neither side carries one — the original has no license include and none was added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'info:start\|info:end\|module Rate' candidate.txt` returns nothing; read candidate L8–17 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): credit fields FIXED by the credit waves).

### 2. Includes and components

- **What:** One surviving include change and one deletion. COMPONENT-SWAP (B5): the usage line now names the candidate itself, `@@[[include theme:512-onwards-jp]]@@` (candidate L21), where the original's exhibit block named `theme:basalt` and `theme:512-onwards` (original L19–20). The original's closing `[[include more-by:waylandlaurencepan]]` (original L490) has no candidate counterpart; it fell with the body tail (section 8). The credit includes (section 1) and the interwiki-style include (section 3) complete the candidate's include list; every include in the candidate names a `:scp-jp:` target or the candidate itself.
- **Why:** P1 (KB-15) for the frame and credit targets; the usage line is the theme's own name, so it follows the candidate's fullname. Ruling 4 is not engaged as a component port: the Basalt base is a delivery matter (section 3), and no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — four includes: the frame, the credit pair, and the usage exhibit naming the candidate itself.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers by import: its head module imports EN Basalt's code blocks /1, /3, /5 from `scp-wiki.wdfiles.com` (original L3–5), and its own CSS sits in a `[[code type="css"]]` exhibit (original L220–486) served by a tail module's `@import url(https://scp-wiki.wikidot.com/theme:512-onwards/code/1)` (original L495). The candidate replaces both routes (blocks B1, B7–B60, B67–B68). At the head, the interwiki-style frame (candidate L1–4) at priority 1 with `theme=` naming the candidate's own `local--code/theme%3A512-onwards-jp/1` on the draft host. The body of the file is one `[[module CSS]]` (candidate L24–1354) which (a) loads Noto Sans JP (L27, section 4), (b) inlines the Basalt-JP base layer — banner-headed Basalt CSS (L28–49), an `@import` of `theme%3Abasalt-jp/1` from the draft host (L50), the Sofia Sans load (L52) — and (c) carries the theme's own CSS, moved from the code block at 0.991 similarity, from candidate L1086 (its `:root` opens at L1089 with the `--onwards-*` variables, as at original L220). The tail self-import module is deleted (B68): delivery is inline now, and the candidate holds no `[[code]]` block at all.
- **Why:** P4/T9 (base delivery from the JP distribution: Basalt via its JP port, here in the K5b-3 layered form where the base rides inside the theme's own delivery) and P6/T3 (the interwiki-style frame, priority 1 for the theme's own layer). The draft-host form of the frame and base-import lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting. The inlined base is also the KB-20 shape (an oversize file because the base is inlined rather than imported in layers); it is the producing wave's chosen form for this family, recorded here so the file's size is not mistaken for theme content.
- **Verify:** `grep -n 'local--code\|@import' candidate.txt` — the frame line (L3), the font loads (L27, L52), and the basalt-jp import (L50); compare original L3–5 and L495.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the EN-host import routes are gone, not kept.

### 4. Fonts and assets

- **What:** Load (B8, JPFONT-LOAD): a Google Fonts `@import` for Noto Sans JP (400;700) added at the module's head (candidate L27); the original loads no JP font — its stacks are Basalt variables. FONT-IMPORT (B11): the Sofia Sans Google Fonts load (candidate L52) rides inside the inlined base layer; it is Basalt's own display face, carried with the base. The theme's own `font-family` lines are `var()` references to the base's variables and are unchanged in form. Stacks: no JPFONT-STACK block fired, because the theme names no literal stack of its own to append to. Assets: the theme's memo-div background images (23 `local--files` URLs on `scp-wiki.wikidot.com`, the author's `wlpan-artist-page` files — hr.png, hq.png, tnn.png and their kin) are carried in the moved CSS on the EN host, unchanged; they are exactly T1's 23 hotlink errors. The original's logo exhibit image (original L16, from the `theme:admo` folder) fell with the exhibits (section 8).
- **Why:** P7/T5 with KB-16 (the font load gap): Japanese text needs the JP face loaded, and neither the original nor the base loads one for this layer. P5 with KB-17 (asset hosts): the memo images are the theme author's own files with no JP-side copy in the record; the settled disposition for serving outside hosts is class (ii), re-hosted at posting, not a candidate edit.
- **Verify:** `grep -c 'local--files' candidate.txt` returns 23; `grep -n '@import' candidate.txt` against the list above.
- **Disposition:** Font load applied; the 23 EN-host asset URLs are DISPOSITIONED (class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The theme's own header overrides sit in its moved layer (candidate L1103–1104): `--header-title: 'SITE-512'` and `--header-subtitle: 'ONWARDS, FOREVER'`, carried from the original's code block in English, unchanged. The two HEADERVAR-labeled blocks (B15, B23) are inside the inlined base layer (Basalt's `--header-title: var(--title)` wiring at candidate L63–64 and L120–121), not theme-level changes. No sidebar or topbar rule of the theme's own was adapted; the furniture is the base's.
- **Why:** P9/T6 is the class that would name a header change; here the operative fact is that the values were kept in the original's language, which is ruling 2 territory (header language is out of scope for migration correctness), dispositioned in the ledger (c3) line for this theme. KB-57 is the standing form of that disposition.
- **Verify:** Read candidate L1103–1104 against the original code block's `:root` (original L220 ff., in diff.md's moved sections).
- **Disposition:** DISPOSITIONED (header language, ruling 2).

### 6. Text translation

- **What:** Five TRANS-UNANCHORED blocks (B2, B3, B4, B5, B6), all in the head: the credit prose (section 1), the one-sentence description (candidate L19, condensed from the original's intro at original L22–28), the usage line (L21), and the base note (L23). That is the whole of the candidate's body prose. The original's remaining body prose — the Settings, Elements, and Custom Divs sections and the Wrap-Up — was not translated into the candidate; section 8 gives the census and the ground. R1 (in-CSS text): the inlined base's comments are Basalt's own English banner and section comments, carried as the base carries them; the theme's own CSS holds no prose strings to translate. R5 glyph-form conversion: none — the source is English.
- **Why:** P10 (body and usage translation is the port's purpose) covers what was translated; the untranslated remainder is not a translation gap but a body-shape decision, which is why it is charged to section 8 (R3) rather than waved through here.
- **Verify:** Read candidate L19–23 against original L22–28; the exhibit sections' absence is diff.md's deletion sections.
- **Disposition:** Standing for the translated head; the exhibit body is section 8's item.

### 7. Links

- **What:** The candidate's one live outbound prose link is the credit block's source link (candidate L16), naming `https://scp-wiki.wikidot.com/theme:512-onwards` — the original's recorded host in review/sources.tsv, the host the mirror was taken from, so the link follows to the serving original. The original intro's hub and article links (original L22–24: the 512 Means Onwards hub, SCP-9628) sat in the prose that was condensed to one sentence and were not carried. No prose link in the candidate targets a foreign-wiki page other than the source link itself.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; the source link meets it on the recorded host. The dropped intro links are part of section 8's census, not a link-class change.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the asset URLs of section 4.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** The closing rule is deviated from in two named ways, and this section is where both are charged. First, delivery topology: the original's three-part delivery (import module, body, code exhibit plus tail import module) is rebuilt as frame plus one module (section 3) — a DELIVERY-MOVE of the code block, not an interleaved edit. Second, the exhibit body: an exhibit census finds the original's body sections — Settings (original L32), Elements (L48), Custom Divs (L77, including the seven memo-div exhibits of residue block B61, original L163–205), Wrap-Up (L208), and the Source Code collapsible (L214) — have no counterpart in the candidate, whose body is the credit block plus three lines (candidate L19–23). The two EXHIBIT-RESTRUCTURE primaries (B16, B62) sit at this body's boundaries. What the exhibits demonstrated survives: the memo classes' rules are in the moved code (e.g. `div.hr_memo` at candidate L1299, `div.hq_memo` at L1347), and the Source Code exhibit's content is the module CSS itself, now live rather than exhibited. The check composition's sample pages are two-line include stubs on both sides (`pages/theme-decoration-sample-512-onwards.txt` and its JP counterpart), so the exhibits live in neither side of the render record.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form. Here the census, not the label, decides: the exhibits were dropped, not replaced. No ledger record names the drop, and this package does not invent a sanction for it; it records the shape, notes that the theme's determination is PASS and its render record is unaffected (the exhibits are documentation prose, not live structure), and flags it for the patterns loop as the batch's R3 observation.
- **Verify:** Compare `grep -n '^+ ' original.txt candidate.txt` — five body sections against none; `grep -n 'hr_memo' candidate.txt` finds only the CSS rule.
- **Disposition:** Recorded as an R3 drop with the ground above; not charged as a defect against the determination, and not hidden.

### 9. Formatting only

- **What:** Four WS-ONLY blocks (B63–B66: original L310, L325, L348, L370), each a whitespace-only line pair inside the moved code block. The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered beyond the move itself, which is section 3's.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The four blocks in diff.md's mechanical section.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no `[!-- ... --]` translator note and no port-provenance comment: `grep -n '\[!--' candidate.txt` returns nothing, and the only comment banners in the file are Basalt's own (the base layer's ASCII banner and section comments, candidate L28 ff.), which are the base's content, not porter additions. Attribution rides in the credit block's fields (section 1).
- **Why:** R2: porter-added text is part of the change record; here the check was run and the answer is genuinely none, stated with its ground rather than left blank.
- **Verify:** The grep above; read the credit block at candidate L8–17.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's 23 hotlink errors: class (ii), posting-procedure — the `local--files` asset URLs on the EN host inside the moved and inlined CSS (section 4); posting re-hosts them, and fix lanes never "fix" them in the candidate. Its 2 pseudo-ref errors: the frame's draft-host `theme=` URL and the basalt-jp draft-host `@import`, class (iii) draft form (KB-41). (2) The render row's items: candidate-inherent page-overflow (1415px@1366 and 425–428px@320/375, both engines) and the floatbox offset — the Basalt family's fixed min-width, a by-design property of the base, recorded as candidate-inherent in the row itself; and the runtime-hotlink item naming `cdn.scpwiki.com`, recorded against the candidate as rendered — the current bytes contain no `cdn.scpwiki.com` reference (`grep` returns nothing), the EN dependency having been removed in the wave history, so the item does not survive into the documented file. (3) T4's structural suspicion (theme CSS living only inside the iftags gate, LOCALIZE-ROWS row 47): DISPOSITIONED per FIX3-S2EN §6.11 — the render reports did not confirm it; the theme renders with its CSS applied. (4) T4's candidate-added hide rules (`#page-title` / `.top-left-box>.item`): removed by FIX3-S2EN §5, and verified absent from the documented bytes — there is no `.top-left-box` rule in the candidate, and its `#page-title` rules are the base's own (candidate L839–849, including a `display: block !important`, the opposite of a hide rule).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 3, 4, and 8.
- **Disposition:** DISPOSITIONED (items 1–4).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 47): exit 1, 25 errors / 1 warn / 1 info; the errors are hotlink ×23 and pseudo-ref ×2, the two standing classes of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): FINDINGS, the items of section 11(2), all dispositioned; full engine matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 47): FINDINGS jointly, display-affecting findings 4, dispositioned as in section 11(3)–(4) and the ledger §(c3) line (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves). The original having been superseded upstream after revision 10, the follow-up diff artifact `diff-512-onwards-from10.txt` is held in the campaign record (K5a-i). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +1,028/−168 in 68 change blocks / 6 diff sections; the GNU-diff count of the same pair is 1,140 changed lines, and the difference is alignment choice around the moved code, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:512-onwards-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 47; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The exhibit body (an R3 drop, recorded)

The original page is a theme page in the EN style: a short intro, then Settings, Elements, and Custom Divs exhibits demonstrating the theme's variables and memo classes, a Wrap-Up, and the source in a collapsible. The candidate keeps none of that body. The porting wave that produced it (Stage 2 EN batch 1) built delivery pages: frame, credit, a three-line body, and the CSS. Nothing in the ledger, the localize row, or the FIX3/FIX4 records names the exhibit drop as a decision, and the render record cannot speak to it, because the composition's sample pages are include stubs on both sides. The classes the exhibits demonstrated remain usable (their CSS moved intact, section 8), so the loss is documentation, not function. This record exists so a reviewer does not have to discover the absence by census, and so the patterns loop can decide whether the EN batch-1 lean body is a convention to name or a gap to repair.


### Post-package repairs (REFRESH3-D)

Recopy brought one post-package repair in: built at `9068bb7` before 722ceb5, the candidate still carried the dead frame parameter; the recopy removed exactly that line (36,970 → 36,889 bytes).

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3A512-onwards-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- **Original evidence:** no original frame; tail `@import` of its own code/1 at original L495. No other repair touches this file.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-512-onwards-jp.txt` is the two-line decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The candidate layers over `pages/theme:basalt-jp.txt` (sources.tsv kind K5b-3); the base's own package is a separate record (class U), and the inlined copy of its layer inside this candidate is accounted in section 3. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
