# Review package — theme:foundom-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:foundom-jp — origin CN, population #190 [GOSIGN2-LEDGER (b) row 190]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 09396f9cb345ad4aad85bd9c296031ca4fa2589018fda13ef85ed488a75bea13); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 3 warns / 0 infos (hotlink×4, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 168; GOSIGN2-LEDGER (b) row 190]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 509–519px@320/375 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 189, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 189]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 190]
- Computed against: canonical commit 05dd295f2874b21920630066cf955283d2b77d5d; candidate file pages/theme:foundom-jp.txt sha256:09396f9cb345ad4aad85bd9c296031ca4fa2589018fda13ef85ed488a75bea13; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 190, whose T1/T2/T4 cells all read FINDINGS) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×4 + pseudo-ref ×1 (classes (ii)/(iii), section 11); the T4 items P1, P2, P7 (section 11, quoted exactly). All four T4 charges were subsequently repaired by canonical commit 05dd295 (FIX-FOUNDOM.md): the four include slots restored, the malformed gate closer fixed, the CSS split into code/1 + code/2 with both delivered, and the split font state unified to Noto Sans JP. This package documents the corrected candidate; sections 2, 4, and 8 record the byte state with the repair history, and the Per-theme record explains the mechanism |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:foundom | theme:foundom-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 7 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-foundom.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:foundom-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 1,007 lines / 85,482 bytes | 984 lines / 87,380 bytes (repaired) |
| SHA-256 | 7372c610893fdef3e2e61e50cbc66ae05979be3e3718be54ac0800c9190eb35f | b398c66ee2cbba88fb1cf24300e0018bb9e3208e9e6798bd05d61469d02912a4 |

Wave history: the candidate was created by the Stage 2 CN6 integration (commit 4166a2f, the LOCALIZE-S2-D wave's port); commit 95fd1d1 (rework2-p1) restored base deliveries for nine dropped pairs, this theme among them; 1869877 (FIX-CREDIT-D) normalized the translator attribution; the sweep (b5cb724) completed the usage exhibits' self-references; and canonical commit 05dd295 (FIX-FOUNDOM.md) restored the four include slots, split the delivered CSS into code/1 and code/2, fixed the malformed gate closer and unified the font state — the package's computed-against commit. No production JP counterpart exists, so the R4 adoption question does not arise.

## Summary

A CN theme built on Wikidot's include-slot mechanism: the original's head defines four parameter slots (`{$inc-css}`, `{$inc-color}`, `{$inc-chara-start}`, `{$inc-chara-end}`) that let an including page switch the theme's palette and invoke its Chara character-card component. The port translates the page fully and repoints everything it keeps. As built it did not carry the slot definitions over — the T4 row charged the mechanism's absence and the ledger dispositioned it under the posting-procedure convention (P1) — but canonical commit 05dd295 (FIX-FOUNDOM.md) has since restored all four definitions at the head (candidate L3–30), split the delivered CSS into code/1 (main) and code/2 (LETTERS palette) with both delivered, fixed the malformed `[[/iftags]` closer (P2), and unified the split font state to Noto Sans JP (P7); the usage exhibits' self-references were also completed to the `-jp` posting name by the sweep (b5cb724). The candidate layers the theme on a base include the original did not have (`theme:parallel-jp`, the JP counterpart of the original's fragment:parallel base). Four asset references remain on a third-party sandbox host (KB-58 class). Measured churn (diff.md, the generator's difflib count with autojunk off, recomputed against the repaired candidate: +178/−215 in 7 hunks; the 80-block classification was computed on the as-built pair).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 80 change blocks — 40 specific (50.0%), 37 heuristic (46.3%), 3 residue (3.8%), 0 skipped. The classifier has no signature for the slot-mechanism deletion, which rides inside B1 and B5 (both labeled SELF-DELIVERY); sections 2 and 8 adjudicate those blocks from the bytes. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COLON-ENC | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| GLYPH-FORM | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 4 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 38 |
| TRANSLATION-ANCHORED | 32 |

Adjudication for this README (every specific block was read against the bytes): the two EXHIBIT-RESTRUCTURE primaries are exhibit-adjacent line changes (section 8). The three residue blocks resolve as a usage-region alignment pair (B7), the escaped copy of the image exhibit's colon encoding (B53), and a near-identical Chara exhibit line whose difference sits inside its style parameter (B66). The original's bare rate module is spelled `[[module rate]]` in lowercase (original L61), which the BARE-RATE-DEL signature does not match; its deletion rides inside B5 and is narrated in section 1 from the bytes. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:foundom-jp; original theme:foundom on scp-wiki-cn at reference revision 7; candidate `pages/theme:foundom-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: standard). As built, the candidate's head differed from the original's in kind, not just in form: where the original opens with its four slot definitions (original L1–28) and its delivery modules, the candidate opened with a base include (candidate L1: `[[include theme:parallel-jp]]`), the localized gate `[[iftags +テーマ]]` (L3), and the credit block (L5–14). Canonical commit 05dd295 has since restored the four slot definitions at candidate L3–30, between the untouched L1 base include and the gate (now L32); the credit block follows the gate. Section 2 adjudicates that head change; it is the theme's defining port decision.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, and the slot question is P1's include-mechanism class.
- **Verify:** The sources.tsv row for foundom-jp; `sha256sum original.txt` against the Provenance table; compare the two heads directly (original L1–30, candidate L1–30).
- **Disposition:** Standing (the route itself); the head changes are recorded in sections 1–3 and adjudicated in sections 2 and 8.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare rate module (`[[module rate]]`, original L61, inside B5's range) and nothing else — no info pair, no license box. The candidate deletes it and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L5–14) carrying the eight ruling-3 fields （タイトル Foundom版式； 翻訳責任者 AI; 翻訳年 2026; 原題 Foundom版式； 著作権者 Dr Hormress; 作成年 2024; 初訳時参照リビジョン 7; the source link to scp-wiki-cn.wikidot.com/theme:foundom). The theme's name stands in Chinese in both title fields — it is the theme's proper name (the port's own page name is its romanization), and no record charges it. T7 credit-module CSS: none on either side (grep returns 0/0); nothing was added and no correction was needed. No license box is added: the original carried none.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; FIX-CREDIT-D (1869877) is the translator form arriving.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L5–14 against the eight fields.
- **Disposition:** Applied.

### 2. Includes and components

- **What:** Three facts, in ascending order of weight. (1) The ordinary repoints are complete: the usage exhibits' self-includes name `:scp-jp:theme:foundom-jp` with their parameters carried over (as built `:scp-jp:theme:foundom`; the sweep b5cb724 completed the `-jp` posting form — candidate L48, L54, and the Chara exhibits at L238/L242), the credit pair is section 1's, and the candidate adds a base include the original did not have, `[[include theme:parallel-jp]]` (candidate L1) — the JP counterpart of the base the original imported as CSS from fragment:parallel (original L32). (2) As built, the original's four include-slot definitions were absent from the candidate (`grep -c '{\$inc' candidate.txt` returned 0), the state the T4 row charged as its largest class and the ledger dispositioned as P1 (posting-procedure convention). Canonical commit 05dd295 (FIX-FOUNDOM.md) has since restored all four definitions byte-for-byte at candidate L3 (`{$inc-css}` → local--code /1), L9 (`{$inc-color}` → /2), L15 (`{$inc-chara-start}`) and L24 (`{$inc-chara-end}`), ported from original L1–28 with only the two @import URLs repointed to the candidate's own draft-host delivery — exactly the mechanical repair this package anticipated. (3) The usage section documents the slot usage as working instructions (`inc-css=--` for the standard palette at L54, `inc-chara-start=--`/`inc-chara-end=--` with parameters at L238/L242); with the definitions restored, the documented parameters now feed the mechanism and the Chara card can be raised. This package documents the corrected candidate; the ledger's P1 disposition remains the frozen verdict record and the stamp reads STALE against it by design.
- **Why:** P1 (KB-15) governs include forms; the slot mechanism is this theme's component architecture, so its absence is a structural fact about the port, recorded at the same prominence as the repoints.
- **Verify:** `grep -n '{\$inc' original.txt candidate.txt` — four hits on each side (the candidate's at L3, L9, L15, L24 after the repair). Candidate L54 and L238–242 for the documented usage.
- **Disposition:** DISPOSITIONED (P1, posting-procedure convention class; GOSIGN2-LEDGER §(c3) line for this theme).

### 3. Delivery and code loading

- **What:** The original delivers through its slots and a main module: the slot modules import the theme's code/1 and code/2 from CN storage (original L3, L9), and a further module (original L31–34) imports the base's fragment:parallel/code/1 together with the theme's code/1 and code/2. As built, the candidate replaced that whole apparatus with a base include (section 2) and a tail delivery (as-built candidate L945–951, B80) whose single `[[code]]` block held both CSS copies concatenated. Canonical commit 05dd295 restored the original's two-fragment structure: the delivered CSS is now split at the `/* LETTERS Ver. */` boundary into code/1 (main CSS, candidate L301–937) and code/2 (the 32-line LETTERS palette, candidate L939–972), byte-verified against the original's two code blocks; the restored slot imports (L5 → /1, L11 → /2) mirror original L3/L9; the tail delivery module now imports both fragments (L978 → /1, L979 → /2, newly added), mirroring original L31–34, so the palette still reaches the theme's own page; and the interwiki frame at L983 continues to name /1, the principal CSS. The frame's served CSS no longer includes the 32-line palette because no single fragment holds both copies — that merged target was an artifact of the defect being repaired, and the palette reaches the page through the tail module. The rework2-p1 restoration (95fd1d1) is this theme's separate base-delivery repair: the parallel-jp include is the restored form.
- **Why:** P6/T3 for the own-layer delivery (draft-host form, KB-41, class (iii)); T9 for the base, with the form difference (CSS import of a fragment → include of a theme candidate) recorded as the wave's choice for this base.
- **Verify:** `grep -n 'local--code\|\[\[code' candidate.txt` — slot imports L5 (/1) and L11 (/2), tail imports L978 (/1) and L979 (/2), frame L983 (/1); code blocks at L301 and L939.
- **Disposition:** DISPOSITIONED (draft-host own-layer lines, class (iii)); the base restoration is applied.

### 4. Fonts and assets

- **What:** Fonts (P7), a split state that existed as built and is now repaired. As built, the candidate loaded Noto Sans JP (Google Fonts, weights 100;300;400;700;900) and its second CSS copy connected the load (`"Rubik Mono One", "Noto Sans JP"` header stack; `"Rubik", "Noto Sans JP"` body stack), while the first copy named the unloaded Chinese face `"Noto Sans SC"` in both stacks — the T4 charge "Noto Sans JP font-family not connected" (type 7), which the ledger dispositioned as P7. Canonical commit 05dd295 (FIX-FOUNDOM.md) unified the state: `Noto Sans SC` now occurs 0 times in the candidate, and the first copy's stacks read `--header-font: "Rubik", "Noto Sans JP", sans-serif` and `--body-font: "Rubik", "Noto Sans JP", sans-serif` (candidate L312, L314 after the head insertion); the second copy's stacks remain at L673–674. Only the face name was changed in each line (the header stacks differ in their first entry, "Rubik" vs "Rubik Mono One"), so the two copies are not made byte-identical — they simply name a loaded face. The checker added no class (i) error. Assets: four references stay on a third-party sandbox host (ah-sandbox, in wikidot.com and wdfiles.com forms): the image-block exhibit's logo file (candidate L80), the screenshot image and its escaped copy (candidate L178, L194), and the Chara exhibit's image URL (candidate L235) — the line numbers shifted +29 from the head insertion; same four lines, no asset change. These are the T1 row's four hotlink errors and the T4 row's sandbox-link item.
- **Why:** P7/T5: a JP face loaded but not named in a stack does no work in that stack's scope, and a stack naming an unloaded face falls back — the two copies of one theme must agree, and here they do not. P5/KB-58 for the assets: third-party sandbox hosting is the deferred state — re-upload is barred by owner order, and posting is where the hosting question is settled.
- **Verify:** `grep -n 'Noto' candidate.txt` — the JP load inside the delivered code, the two JP stacks at L312/L314 and L673/L674, and no SC occurrence. `grep -cn 'ah-sandbox' candidate.txt` — 4 lines.
- **Disposition:** DISPOSITIONED (P7, per the ledger's §(c3) line, with the row tension flagged above and in section 11; assets, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** This theme sets no `--header-title`/`--header-subtitle`/`--logo-image` variables on either side (the font variables of section 4 are its furniture interface); its header and navigation are the base's, and the candidate's prose notes the original's top navigation was designed for the CN wiki — a design fact the translation carries over as documentation. Sidebar and topbar rules are inherited from the base and the theme body. No P9 item stands in this theme's T4 row.
- **Why:** P9/T6 is the furniture class; the absence of header variables is recorded so a reviewer does not have to diff-hunt for a header change that never happened.
- **Verify:** `grep -n -- '--header-title\|--logo-image' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose is translated in full: the description (candidate L16), the usage instructions (L18–30, including the palette-switching instruction whose mechanism is section 2's subject — the instruction text is faithfully translated; its operability is the separate question recorded there), the parameter documentation tables (the Chara variables table at candidate L227 and its siblings), the specimens, and the source-code section headings. One GLYPH-FORM block fires (a simplified-form conversion inside a translated line). The 38 TRANS-UNANCHORED and 32 TRANSLATION-ANCHORED label occurrences are this mass, resolved by shape in the appendix. Chinese survives as live text in the credit title fields (the theme's proper name, section 1) and inside the sandbox URLs' file names — names and citations, not untranslated instructions.
- **Why:** P10 and KB-18: reader-visible strings are translated.
- **Verify:** diff.md's prose sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The candidate's live outbound links are the credit block's source link (candidate L13), naming scp-wiki-cn.wikidot.com/theme:foundom, the original's recorded host in sources.tsv — the serving form, not a defect — and the description's link to the Letters entertainment hub page (candidate L16, carried over from the original as the theme's subject reference). The sandbox asset URLs are CSS and exhibit references, not prose links (section 4). No prose link in the candidate targets a page the records charge as dead.
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve or a JP counterpart exists; neither is charged here.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only prose hit besides asset lines.
- **Disposition:** Standing.

### 8. Structure

- **What:** This is the batch's one package where the R3 question has a real answer. Two structural facts stood as built and have been repaired. (1) The slot-mechanism deletion (section 2): the original's head apparatus (L1–28) had no counterpart and the candidate was 56 lines shorter than the original despite adding a credit block and a base include; the T4 row charged it as its largest class and the ledger dispositioned it (P1). Canonical commit 05dd295 restored the four slot definitions byte-for-byte at candidate L3–30, with only the two @import URLs repointed. (2) A malformed gate closer: as built the candidate's gate opened at L3 and closed correctly at L943, but at as-built candidate L265 stood `[[/iftags]` with a single closing bracket — a broken token the original does not have, charged by the T4 row (type 2) and dispositioned P2/T1 class (ii). The same commit fixed the token to `[[/iftags]]` (now candidate L294, +29 from the head insertion); the gate's other closer is now L975. The classifier's two EXHIBIT-RESTRUCTURE primaries, by contrast, are exhibit-adjacent line changes and do not survive as restructures; the exhibit census (parameter tables, Chara demonstrations, specimens, source code) stands in the original's order on both sides.
- **Why:** R3 exists to force exactly this adjudication, and ledger class I charges the silent form of a structural deletion; here the deletion was charged by the row and dispositioned by the ledger, so the package's duty is to keep the byte state and the disposition visibly connected.
- **Verify:** `grep -n 'iftags' candidate.txt` — the opener at L32, the repaired closer at L294, the gate close at L975 (no malformed token remains). `grep -c '{\$inc' original.txt candidate.txt` — 4 and 4.
- **Disposition:** DISPOSITIONED (P1 for the slot deletion, P2 for the malformed closer); both charges have since been repaired by 05dd295, and this package documents the corrected candidate.

### 9. Formatting only

- **What:** None as a class: the classifier finds no WS-ONLY block, no re-indentation, and no line-ending conversion (0, 0, 0). The section stands so the absence is on record; this candidate's formatting was not normalized, which distinguishes it from the batch's whitespace-normalized packages.
- **Why:** Formatting churn is disclosed as its own class (R7); a clean zero is a finding, not a gap.
- **Verify:** classification.json's formatting counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. This candidate carries no `Ported for SCP-JP` banner, no `[JP]` markers, and no translator-note comments; its provenance record is the credit block and this package.
- **Why:** R2: the absence is recorded so a reviewer does not have to wonder whether annotations were overlooked.
- **Verify:** `grep -n 'Ported for\|\[JP\]\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Five items, quoted as the ledger records them. (1) T1's four hotlink errors: class (ii) — the sandbox-host asset lines of section 4, posting-time hosting state (KB-58); the ledger's §(c1) hotlink line dispositions the class, and this theme's §(c3) line does not name a separate P5 item. (2) T1's one pseudo-ref error: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3). (3) P1 (the include-slot deletion, section 2): "DISPOSITIONED (posting-procedure convention class)". (4) P2 (the malformed iftags closer, section 8): "DISPOSITIONED (T1 class (ii))". (5) P7 (the font state, section 4): "DISPOSITIONED (recorded without a display-affecting mark; T4 bar)". Two record tensions were flagged, not smoothed, and all three T4 items have since been repaired by canonical commit 05dd295 (FIX-FOUNDOM.md). First, the P7 wording: the LOCALIZE-ROWS row for this theme counts 4 display-affecting findings with the font item among them, while the ledger's parenthetical says the item was recorded without a display-affecting mark; the as-built bytes (section 4) showed a real, if partial, display consequence, so the row's characterization was the accurate one — and the split font state is now unified to Noto Sans JP. Second, the P1 class: a posting-procedure convention is a disposition about how includes are settled at posting, applied here to a mechanism deletion the row called its largest structural class; the four slot definitions are now restored byte-for-byte. The P2 malformed closer is likewise fixed. The frozen ledger verdict stands; the stamp reads STALE against it by design.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; where the grounds and the bytes pull apart, the package's job is to show both, which is what the third-party documentation standard is for.
- **Verify:** Each item names its deciding record above; the ledger lines are GOSIGN2-LEDGER §(c3) at its foundom entry and §(c1) for the T1 classes.
- **Disposition:** DISPOSITIONED (all five items), with the two tensions flagged.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 168): exit 1, 5 errors / 3 warns / 0 infos (hotlink×4, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN6)): FINDINGS at the row level, with the coverage caveat recorded in the ledger's §(c2) block for this theme: the sample's T2 produced no machine verdict (exit 2, no summary), so no render finding is charged or cleared for the sample; the ledger dispositions the row on the remaining record, and this package records the caveat rather than papering over it. (c) T4/T5 (LOCALIZE-ROWS row 189): FINDINGS jointly, display-affecting count 4 (the slot deletion, the malformed closer, the font state, the sandbox links); the ledger's §(c3) line dispositions P1, P2, and P7 for this theme. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off), recomputed against the repaired candidate: +178/−215 in 7 hunks (the 80-block classification describes the as-built pair). The repaired candidate adds three pseudo-ref errors (the two restored slot @imports and the added tail /2 import), all the same class-(ii) draft-form as the pre-existing tail line, with no new class-(i) error, per FIX-FOUNDOM.md.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; a check that produced no verdict is reported as such.
- **Verify:** Re-run the checker on `pages/theme:foundom-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 190; go-sign, COMPLETION-REPORT §10), with the coverage caveat and the section 11 tensions recorded.

## Per-theme record

### The include-slot mechanism, for a reader who has not met it

Wikidot's include system lets a page accept parameters: a page included as `[[include theme:foundom inc-css=--]]` receives the variable `{$inc-css}`, and sections of the included page wrapped as `[!-- {$inc-css} … --]` take effect for that inclusion. Foundom's original builds its whole composition on this: the default inclusion renders the theme plainly, `inc-css=--` switches in the foundation-standard palette (the code/2 CSS), and `inc-chara-start=--`/`inc-chara-end=--` wrap a character card in the Chara component's parameterized markup. It is the theme's component architecture, not decoration. As built, the candidate kept the theme's appearance and translated its documentation — including the parameter instructions — but the four definitions that make the parameters work were absent (section 2 gave the grep proof: 4 hits in the original, 0 in the candidate). A user following the candidate's own usage page got the default rendering regardless of parameters and could not raise a Chara card at all: the concrete content of the T4 row's largest charge and of the P1 disposition, and the reason this package leads its Per-theme record with a mechanism explanation — the diff alone did not make the loss legible because the deleted lines look like four comment-wrapped modules among many.

Canonical commit 05dd295 (FIX-FOUNDOM.md in R/review-scout/) has since repaired the mechanism. The four definitions are restored byte-for-byte at candidate L3–30 (`{$inc-css}` → local--code /1, `{$inc-color}` → /2, `{$inc-chara-start}`, `{$inc-chara-end}`), placed after the untouched L1 base include and before the gate, matching the original's own slot-before-gate arrangement. The determination that /1 is the main CSS and /2 the LETTERS palette came from a two-block census of both files and the original's own slot imports; the candidate's single delivered copy was split at the `/* LETTERS Ver. */` boundary into code/1 (L301–937) and code/2 (L939–972), the latter byte-identical to the original's code/2. The tail delivery module gained a second @import (L979 → /2) so the palette still reaches the theme's own page; the frame at L983 continues to name /1, the principal CSS. The misaligned font stacks were unified to Noto Sans JP (L312, L314; `Noto Sans SC` now 0 hits), and the malformed `[[/iftags]` closer was fixed (L294). This package documents the corrected candidate; the stamp reads STALE against the pre-repair verdict by design, no re-judgement is fabricated, and the frozen ledger remains the verdict record.

## Appendix — heuristic and residue mass, resolved by shape

Class M treatment: the 37 heuristic blocks are not listed one by one; they fall into the shapes below, each verified against the bytes at the cited ranges. The 3 residue blocks are listed in full.

| Shape | Blocks | Where | Resolution |
|---|---|---|---|
| Prose and table translation (unanchored) | The TRANS-UNANCHORED body mass (38 label occurrences across heuristic and mixed blocks) | candidate L16–260 | P10 translation (section 6) |
| CSS body mass in the two delivered copies | The CSS-BODY portions of mixed blocks | candidate L272–941 | Carry-over with the section 4 font state |
| Residue: usage-region alignment pair | B7 | candidate L24–25 | The usage exhibit's code-div form (section 2's exhibits) |
| Residue: escaped image exhibit, colon encoding | B53 | candidate L165 | The B50 change's escaped copy (section 4) |
| Residue: Chara exhibit line, style-parameter difference | B66 | candidate L206 | Exhibit carry-over; the Chara mechanism question is section 2's, not this line's |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-foundom-jp.txt` is the decoration sample the render checks ran against (its T2 produced no machine verdict; section 12); it belongs to this theme's record but carries no port change of its own to explain here. The base include `theme:parallel-jp` is another candidate in the population with its own package; this theme's record names it as a dependency, not a change. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
