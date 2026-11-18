# Review package — theme:a-problematic-theme-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:a-problematic-theme-jp — origin EN, population #49 [GOSIGN2-LEDGER (b) row 49]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2622fa334c30029475128ce5f6cd5c5db7b19a1dcc969fa1490e7f1eb5210a34); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 0 infos (hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 49; GOSIGN2-LEDGER (b) row 49]
- T2/T3 (render, combined verdict): PASS-WITH-NOTES — [combined T2/T3] report `NO candidate-specific defect established` — no candidate-specific defect; all lines cross-cutting preview/draft-form/by-design, FINDINGS limited to shared X2 preview-static-credit panel (not a per-theme fault). [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no sample credit-modal line in this theme's row; the row's only credit item is the shared preview-static-credit panel, recorded as cross-cutting, not a per-theme fault [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 49, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 49]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 49]
- Computed against: canonical commit 5d951775998e4a1eeccf8e8695a6518b328962ee; candidate file pages/theme:a-problematic-theme-jp.txt sha256:2622fa334c30029475128ce5f6cd5c5db7b19a1dcc969fa1490e7f1eb5210a34; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 49) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×1 (class (ii)); the render row is PASS-WITH-NOTES with no candidate-specific defect; T4's five findings dispositioned per the ledger (c3) line and FIX3-S2EN §5/§6.11 (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:a-problematic-theme | theme:a-problematic-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14 (the candidate's credit block records 初訳時参照リビジョン: 14) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-a-problematic-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:a-problematic-theme-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 457 lines / 13,013 bytes | 132 lines / 4,264 bytes |
| SHA-256 | db7375878496825ba2239ee61ba756e4e6b87bc0607ba3380d603e9fcf0df5d9 | c5c8078bd20f812802d859a49f29bc685fc7ff5802240432c4d6801ec94f740d |

Wave history: the candidate was created by the Stage 2 EN batch 1 wave (commit 3205f27) and has one later commit, 1869877 (FIX-CREDIT-D, translator attribution normalization; the stamp's computed-against commit). The original was superseded upstream after revision 14; a follow-up diff artifact (`diff-a-problematic-theme-from14.txt`) is held in the campaign record (K5a-i, per review/sources.tsv).

## Summary

The batch's most reduced port. The original is a Black Highlighter theme with an elaborate delivery: BHL imported from the EN author's GitHub Pages, three interwiki-style frames, and its CSS published as three `[[code]]` variants (Standard, Dark, Red) selected by a `{$version}` address. The candidate keeps exactly one of those variants — the Standard, which is the default `code/1` — in a single module, rewrites its four font loads from bunny.net to Google Fonts, and drops the other two variants, the exhibit body, and the BHL import itself. Two of the localize row's findings live exactly there: the candidate's body note claims "BHL (inline)" while the file carries no BHL CSS at all (section 3), and the Dark/Red variants have no counterpart (section 8). The render row is nonetheless PASS-WITH-NOTES with no candidate-specific defect, because in the JP composition the base arrives from the environment; both facts are recorded, neither is smoothed over. Measured churn (diff.md, the generator's difflib count with autojunk off: +29/−348, 377 changed lines in 8 change blocks / 3 hunks; a GNU-diff count of the same pair gives 371 changed lines — the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 8 change blocks — 6 specific (75.0%), 2 heuristic (25.0%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| EXHIBIT-RESTRUCTURE | 3 |
| DELIVERY-MOVE | 3 |
| SELF-DELIVERY | 2 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| WS-ONLY | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic CSS-BODY block (B2, original L3–6 → candidate L25) is the deletion of the original's BHL import module, a delivery change narrated in section 3. Of the three EXHIBIT-RESTRUCTURE primaries, B3 is the exhibit-body drop and B7 is the Dark/Red variant drop (both section 8), while B8 is the tail delivery furniture (the `{$version}` import module and the priority-3/4 frames) falling with them (section 3). The DELIVERY-MOVE primaries are the Standard variant's move into the module (B4 its font head, B6 its tail). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:a-problematic-theme-jp; original theme:a-problematic-theme on scp-wiki at reference revision 14; candidate `pages/theme:a-problematic-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch 1 wave (sources.tsv kind: standard; no production JP counterpart exists, so the R4 adoption question does not arise). The frame order changed: the original opens with its gate (original L1) and BHL import module; the candidate opens with the interwiki-style frame (candidate L1–4) and the localized gate after it (candidate L6).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for a-problematic-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module rate]]` inside the body (original L19). The candidate deletes it with the body (block B3) and installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying the eight ruling-3 fields (タイトル 問題作テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 A Problematic Theme; 著作権者 winkwonkboi; 作成年 2024; 初訳時参照リビジョン 14; the source link, candidate L16, naming `scp-wiki.wikidot.com/theme:a-problematic-theme` — the original's recorded host). The file's last commit (1869877) is the FIX-CREDIT-D attribution normalization arriving at this form. No credit-module CSS supplement was added (no `.creditButton`/`.creditRate` rules in the candidate). License box (T4): neither side carries one.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module rate\|module Rate' candidate.txt` returns nothing; read candidate L8–17 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): credit fields FIXED by the credit waves; the FIX-CREDIT-D pass is in the file's own history).

### 2. Includes and components

- **What:** No body include survives to repoint: the original's includes are its three interwiki-style frames (delivery furniture, section 3) and the credit-adjacent body holds none. The candidate's include list is the frame (candidate L1), the credit pair (L8, L17), and the usage line naming the candidate itself (L21). Every include names a `:scp-jp:` target or the candidate itself.
- **Why:** P1 (KB-15) is satisfied vacuously for body includes; the frame includes are P6's, recorded in section 3. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — four includes, all JP-side.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original's delivery has four moving parts: a head module importing BHL's normalize and black-highlighter stylesheets from `nu-scptheme.github.io` (original L4–5); an interwiki-style frame at priority 1 whose `theme=` is that same normalize stylesheet (original L8–10); three `[[code]]` variants (Standard L174–277, Dark L281–357, Red L361–438) exhibited under the Source Code section; and a tail furniture set — a module importing its own `code/1` and `code/{$version}` (original L445–446) plus interwiki-style frames at priorities 3 and 4 naming the same two addresses (original L449–457). The candidate replaces all of it (blocks B1, B2, B8): one interwiki-style frame at priority 1 with `theme=` naming the candidate's own `local--code/theme%3Aa-problematic-theme-jp/1` on the draft host (candidate L1–4), and one `[[module CSS]]` (candidate L25–130) carrying the Standard variant's CSS. The BHL import module is deleted (B2): the candidate carries no BHL CSS — no normalize, no black-highlighter rules — although its body note (candidate L23) reads **基盤:** BHL（インライン） ("Base: BHL (inline)"). That is LOCALIZE-ROWS row 49's finding (1), and the bytes bear it out: `grep -n 'nu-scptheme\|normalize' candidate.txt` returns nothing. In the JP check composition the base is supplied by the environment, which is why the render row establishes no candidate-specific defect; but the file as written does not do what its own note says, and a page that included this candidate outside that environment would get the theme's layer without its base.
- **Why:** P4/T9 (base delivery from JP distributions) is the class the port aimed at; the JP BHL distribution form is an import or a frame naming the JP host, and neither is present — the wave instead relied on the composition's environment. P6/T3 covers the surviving frame (priority 1, own layer). The draft-host form of the frame line is KB-41, class (iii).
- **Verify:** The greps above; read original L3–10 and L443–457 against candidate L1–4 and L25.
- **Disposition:** DISPOSITIONED (the frame line, class (iii); finding (1) dispositioned under the ledger (c3) class outcomes with the render row's no-defect result as its ground — recorded here with the caveat on the body note, which the disposition does not repair).

### 4. Fonts and assets

- **What:** Loads (B4, FONT-IMPORT): the Standard variant's four `@import`s are carried into the module with their host rewritten, `fonts.bunny.net` → `fonts.googleapis.com`, families unchanged (IBM Plex Sans Condensed 700; Podkova 400..800; Open Sans 300..800; Nanum Gothic Coding — candidate L29–32, from original L177–180). No JP font load was added: there is no Noto Sans JP import, and the candidate declares no `font-family` line of its own (`grep -n 'font-family' candidate.txt` returns nothing) — every stack it uses is a variable resolved by the base, so the theme inherits its JP rendering from the base entirely (the T5 inheritance case). Assets: one `url()` on a foreign host, the Standard variant's `--logo-image` (candidate L80, `scp-wiki.wdfiles.com/local--files/theme%3Aa-problematic-theme/standard37.svg`); it is T1's single hotlink error. The Dark and Red variants' logo files (original L285, L365) fell with their variants (section 8).
- **Why:** P5: bunny.net is not among the sanctioned hotlink hosts (storage, Google Fonts, BootstrapCDN, cdnjs), so the loads move or die; moving them to Google Fonts preserves the theme's typography, which is its stated design ("unique typography", candidate L19). P7/T5 with KB-16: the font-load-gap question is answered by inheritance — the file declares no stack that could lack a JP fallback, because it declares no stack at all.
- **Verify:** `grep -n '@import' candidate.txt` — four Google Fonts lines; the logo line at candidate L80.
- **Disposition:** Font loads applied (host rewrite); the logo asset DISPOSITIONED (class (ii), KB-17).

### 5. Header, sidebar, and site furniture

- **What:** The candidate's header variables are the Standard variant's own: its `--logo-image` (candidate L80, section 4) and the `--theme-name: "A Problematic Theme"` string variable (candidate L38, section 6). The HEADERVAR-labeled block (B7) sits on the Dark variant's `:root`, which was dropped (section 8). No `--header-title`/`--header-subtitle` override exists on either side; the furniture is the base's, and no P8 adaptation was made or needed in the composition.
- **Why:** P9/T6 names no change here; the header-language question (ruling 2) does not arise for values the theme never sets.
- **Verify:** `grep -n -- '--header-\|--logo-image\|--theme-name' candidate.txt` — the two lines above.
- **Disposition:** Standing.

### 6. Text translation

- **What:** One TRANS-UNANCHORED block in the head supplement (B1's prose half): the candidate's body prose is the one-sentence description (candidate L19), the usage line (L21), and the base note (L23, on which section 3). The original's body prose (What's This? at original L22, the Examples at L57) was not translated into the candidate; it fell with the body (section 8). R1 (in-CSS text): one string variable is reader-visible — `--theme-name: "A Problematic Theme"` (candidate L38), carried from the original's Standard variant in English; it is the theme's self-name inside its S-CSS-P integration block, a name, not prose, and names are not translated. The CSS comments (`/* Standard Version */`, the color-group comments) are the original's own English, carried with the moved code. R5: none — the source is English.
- **Why:** P10 covers the translated head; KB-18 covers reader-visible strings, and the one such string here is a proper name, which the class does not reach. The untranslated remainder is the body-shape decision charged to section 8.
- **Verify:** Read candidate L19–23 and L34–39.
- **Disposition:** Standing for the translated head; the exhibit body is section 8's item.

### 7. Links

- **What:** The candidate's one live outbound prose link is the credit block's source link (candidate L16), naming `https://scp-wiki.wikidot.com/theme:a-problematic-theme` — the original's recorded host in review/sources.tsv, the host the mirror was taken from. No other prose links survive; the original body's links sat in the dropped exhibits.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; the source link meets it on the recorded host.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the logo asset of section 4.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** The census, in three parts. (a) The exhibit body (B3, original L7–174): What's This?, Examples, the title samples, and the Source Code section's framing — no counterpart in the candidate, whose body is the credit block plus three lines (candidate L19–23). Same EN batch-1 shape as the batch's other themes; the demonstrated CSS survives as the live module, the loss is documentation prose. (b) The variant code blocks: the Standard variant moved into the module (B4, B6); the Dark (original L281–357) and Red (L361–438) variants have no counterpart anywhere in the candidate (B7) — the original's `{$version}` selection mechanism (tail imports and frames at original L445–457) fell with them (B8), so a reader cannot select Dark or Red from this candidate at all. (c) The Source Code collapsibles themselves: the Standard code is no longer exhibited, it is delivered (section 3), which is the one structural change that is an improvement in kind — the exhibited copy and the live copy can no longer drift apart.
- **Why:** R3 forces the adjudication for (a) and (b): dropped, not replaced, with grounds stated. For (b) the ground available in the record is thin — no ledger or localize line names the variant drop; the localize row's five findings charge the missing base, the iftags structure, the 404 specimen, and the class outcomes — so this package records the absence as a fact a reviewer can weigh, notes the render row ran the Standard form only, and flags it for the patterns loop. The closing rule's preservation demand (selectors, variables, channel order) holds inside the carried variant: the Standard CSS is the original's, moved, with its `:root` order intact (candidate L34 ff. against original L182 ff.).
- **Verify:** `grep -n 'Version' candidate.txt` — one banner, Standard; `grep -n '^+ ' original.txt candidate.txt` for the body census.
- **Disposition:** Recorded as R3 drops (exhibits; Dark/Red variants) with the grounds above; not charged against the determination, and not hidden.

### 9. Formatting only

- **What:** One WS-ONLY block (B5, original L264–265 → candidate L116–117) inside the moved Standard CSS. The classifier finds no re-indentation (0 blocks pair up after leading-whitespace normalization), so the R7 hazard is not triggered beyond the move itself, which is section 3's.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The block in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None as comments: the candidate carries no `[!-- ... --]` translator note and no provenance comment (`grep -n '\[!--' candidate.txt` returns nothing). The one porter-written text is the body base note (candidate L23), counted in section 6 and charged in section 3 for its content. Attribution rides in the credit block's fields (section 1).
- **Why:** R2: porter-added text is part of the change record; here the check was run and the answer is that the only addition is body prose, stated with its ground.
- **Verify:** The grep above; read candidate L23.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's single hotlink error: class (ii), posting-procedure — the logo asset on `scp-wiki.wdfiles.com` (section 4); posting re-hosts it. (2) The render row (RENDER-ROWS-1, RENDER-S2-A): PASS-WITH-NOTES, "no candidate-specific defect established" — every line cross-cutting (the shared X2 preview-static-credit panel, preview/draft-form/by-design), recorded as not-charged to this candidate. (3) T4's structural suspicion (theme CSS living only inside the iftags gate, LOCALIZE-ROWS row 49 item (2)): DISPOSITIONED per FIX3-S2EN §6.11 — the render reports did not confirm it; the theme renders with its CSS applied. (4) T4's 404 XHTML specimen (the original body's L127–137 specimen): the specimen page was removed by FIX3-S2EN §5 — a composition-level removal of a specimen file, not an edit to this candidate, whose own history (3205f27, 1869877) contains no FIX3 commit. Finding (1) of the same row (the missing BHL base) is section 3's item, dispositioned under the (c3) class outcomes on the render row's ground.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 3, 4, and 8.
- **Disposition:** DISPOSITIONED (items 1–4).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 49): exit 1, 1 error / 1 warn / 0 info; the error is hotlink ×1, the standing class of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): PASS-WITH-NOTES, section 11(2); full engine matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 49): FINDINGS jointly, display-affecting findings 5, dispositioned as in section 11(3)–(4), section 3, and the ledger §(c3) line (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves). The original having been superseded upstream after revision 14, the follow-up diff artifact `diff-a-problematic-theme-from14.txt` is held in the campaign record (K5a-i). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +29/−348 in 8 change blocks / 3 hunks; the GNU-diff count of the same pair is 371 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:a-problematic-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 49; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The missing base (the body note against the bytes)

The candidate's body makes one claim its file does not keep: **基盤:** BHL（インライン） — "Base: BHL (inline)". The original earns the equivalent claim: its head module imports BHL's two stylesheets, so a page built on the original gets the base. The candidate imports nothing of BHL's, inlines nothing of BHL's, and frames nothing of BHL's; its single module is the theme's own Standard layer only. The localize lane saw it (row 49, finding (1)) and the disposition rests on the composition: in the Sigma-10 check environment the base is present from the site side, the render row found no defect, and the determination is PASS. All of that is true, and none of it makes the note accurate. A reviewer meeting this theme outside the composition — which is the audience the owner's documentation standard names — would read the note, include the candidate, and get an unbased page. This record therefore keeps the finding attached to the package permanently: the note is the candidate's one prose-vs-bytes discrepancy, flagged here and in the lane report, for whoever next edits the candidate to either give it its base or correct its note.

### Post-package repairs (REFRESH3-E)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:a-problematic-theme-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FRAMED — frame sub-shape (D) treated as (B), own-address pointer dropped (landing 5d95177).** `FIX-FRAMED.md` records this theme's frame as sub-shape (D): the frame's `theme=` named the theme's own code block (/1) on the draft host, but the candidate carries no `[[code]]` block in any form (its CSS is live `[[module CSS]]`), so the named block does not exist — a dead pointer, verified in the report. The original's once-live form: it carries four frames, head priorities 1 and 2 naming the BHL GitHub Pages files, tail priorities 3 and 4 naming its own /1 and own /{$version}, live against block 1 (`[[code type="CSS"]]` L174–277, "Standard Version"); the candidate inlines the BHL base, so the dropped parameter is the own-layer pointer (priority 1, the candidate's only frame). The coordinator's ruling treats (D) as (B) and applies the minimal remedy: drop the single `| theme=https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aa-problematic-theme-jp/1` line, keep the `[[include :scp-jp:component:interwiki-style]]` frame, its priority, and every other byte unchanged. Commit 5d95177 deleted exactly that one line at candidate L3. The checker finding set is unchanged (1 error / 1 warn before and after; the dropped line was not a class (i) finding), as tabulated in FIX-FRAMED.md.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-a-problematic-theme-jp.txt` is the decoration sample the render checks ran against (its state is the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The 404 XHTML specimen page removed by FIX3-S2EN §5 was a separate composition file, not part of this candidate. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** A Problematic Theme
- **Author:** winkwonkboi
- **Source:** https://scp-wiki.wikidot.com/theme:a-problematic-theme — revision 14
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
