# Review package — theme:our-open-veins-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:our-open-veins-jp — origin EN, population #118 [GOSIGN2-LEDGER (b) row 118]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 657edfa124b63bd5f192cd030b3b1f683815290a07d23309e1f71049e109c97a); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 0 warns / 1 info (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 118; GOSIGN2-LEDGER (b) row 118]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form); T3 broken OurDark20Mode.png (deferred), "使用方法" heading wraps one char/line at 320 (cosmetic). [RENDER-ROWS-2 (RENDER-S2-C (EN15))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN15))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 118, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 118]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 118]
- Computed against: canonical commit 2437aa62e7ab39f7b737695a8887924de1428fe7; candidate file pages/theme:our-open-veins-jp.txt sha256:657edfa124b63bd5f192cd030b3b1f683815290a07d23309e1f71049e109c97a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items (GOSIGN2-LEDGER (b) row 118) |
| Standing items | **DISPOSITIONED** — the P9 masthead strings (ruling 2; sections 5, 11). **FLAGGED by this package** — the original's parameter-gated color-variation module (original L948–1151) is absent from the candidate while the candidate still documents the variation and its activation syntax (per-theme record); the two usage exhibits keep the original's bare local include form |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:our-open-veins | theme:our-open-veins-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 17 (first translation; the candidate's credit block records 初訳時参照リビジョン: 17) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-our-open-veins.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:our-open-veins-jp.txt`, copied at worktree HEAD 9068bb7 |
| Lines / bytes | 1,151 lines / 25,307 bytes | 968 lines / 25,039 bytes |
| SHA-256 | 09b2e97a02aef9ba8ee5e5e35a3faaef2bdaa6c2dc46f7ee8d48b2b26abfb8b4 | 255bdca194b7ef6054b09800675003cc884ab2adb842e6272f1e260615370106 |

Wave history: the candidate was created by the Stage 2 EN15 integration (commit fde02f3, the LOCALIZE-S2-B wave's port, lane-dsh-en15) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose our-open-veins hunk is the translator-field normalization. No FIX5 commit touches this file.

## Summary

A canon theme (for the Our Open Veins setting) whose port carries the standing classes plus one substantive loss this package flags. The standing part: the original's info-module credit zone and its floated bare Rate become the preview credit block; a license box the original never had is installed in the JP backend form with four porter-authored entries that state plainly that the original records no license for the theme's images; the delivery import moves from the page-URL form to the JP wdfiles form; the frame the original includes twice, identically, is carried once; the theme's fonts gain loaded Noto Sans JP and Noto Serif JP companions; and the body, including the footnote samples and the color-variation documentation, is translated. The loss: the original ends, after its tag gate, with a 204-line second CSS module holding the "Our Dark Veins" color variation, wrapped in a comment that the documented include parameter breaks open. The candidate documents the variation and prints its activation syntax, but the module itself is gone, so the documented feature cannot activate. That drop is flagged in the per-theme record with both sides' line ranges; the candidate is not edited here. Measured churn against the current (post-repair) candidate (diff.md, the generator's difflib count with autojunk off: +136/−119 in 13 hunks; a GNU-diff count of the same pair gives 196 changed lines). The pre-repair figures quoted in the original package record were +108/−291 in 71 change blocks.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 71 change blocks — 37 specific (52.1%), 30 heuristic (42.3%), 4 residue (5.6%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 35 |
| TRANSLATION-ANCHORED | 15 |
| DELIVERY-MOVE | 11 |
| EXHIBIT-RESTRUCTURE | 5 |
| DRAFT-HOST | 4 |
| JPFONT-STACK | 4 |
| COMMENT-TEXT | 2 |
| DELIVERY-HOST | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE mass splits three ways — B59–B68 are single-line edits inside the CSS code exhibit (the JP font loads and stacks and the asset re-hosts, sections 3–4) that the label groups by their delivery context, and B71 is the deletion of the original's tail variation module (original L947–1151 → candidate at L969), which is not a move at all and is flagged in the per-theme record; the standing warning that DELIVERY-MOVE can hide a dropped module is exactly this block. The 5 EXHIBIT-RESTRUCTURE labels ride inside multi-label blocks whose primaries are the translation and credit changes; the exhibit census of section 8 confirms no exhibit was restructured beyond them. The 4 residue blocks (B7, B18, B58, B69) are one-line alignment pairings at the credit zone, the variation prose, the code exhibit's opening, and the collapsible close, resolved in the appendix. After adjudication one block remains a defect, not an explanation: B71.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:our-open-veins-jp; original theme:our-open-veins on scp-wiki at reference revision 17; candidate `pages/theme:our-open-veins-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order is the original's own: delivery module, sidebar toggle, frame, then the tag gate (original L1–18; candidate L1–14), with the gate's tag localized to +テーマ (candidate L14).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2.
- **Verify:** The sources.tsv row for our-open-veins-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is the info module: `:scp-wiki:info:start` / `:scp-wiki:info:end` wrapping the attribution prose (original L20–22), with a right-floated bare `[[module Rate]]` beside it (original L24–26). There is no CN-style credit module and, notably, no license box anywhere in the original. The candidate replaces the whole zone (block B6) with the preview credit block (candidate L16–25) carrying the eight ruling-3 fields (title アワー・オープン・ヴェインズ テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Our Open Veins Theme; 著作権者 [[*user Dc_Yerko]], [[*user Kilerpoyo]] — both names, matching the original's prose "created by Dc_Yerko with indications of Kilerpoyo"; 作成年 2025; 初訳時参照リビジョン 17; the source link https://scp-wiki.wikidot.com/theme:our-open-veins, whose host matches the sources.tsv record). The attribution prose itself survives as body text (the original prints it twice, once inside the info module and once as the lead paragraph; the candidate's translated lead paragraph is candidate L29). At the tail the candidate installs the license box the original lacks (block B70): `:scp-jp:component:license-box-backend |author=Dc_Yerko]]` and `:scp-jp:component:license-box-end` (candidate L946–967) with four porter-authored entries — the header and loader images (author Dc_Yerko; license: none stated in the original, with confirm-with-the-author guidance), linea-horizontal.png (distributed in the original from the author's own other wiki, scp-yerko-7; no license stated), and the fonts entry (Jost / Road Rage / Rubik Distressed under the SIL Open Font License via Google Fonts, with Noto Sans JP / Noto Serif JP noted as the Japanese companions). T7 credit-module CSS: none on either side.
- **Why:** P3/T1 with KB-09 (the preview module is rate-bearing; the floated bare Rate goes with the zone it floated in). Ruling 3 fixes the eight fields and the translator form; the file's last commit (1869877) is that form arriving. T4: the license box must be present in its settled JP form (KB-60/KB-63); where the original has none, the box is authored from the theme's actual asset usage, and its entries say "not stated in the original" rather than inventing terms — the same construction the T4 supplement records for this theme.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L16–25 against the eight fields and candidate L946–967 against original L894–912's absence (the original has no license zone to compare; the entries' asset names are the CSS's own url() targets).
- **Disposition:** FIXED by construction at creation (P3 credit fields; the T4 box authored at creation, T4 supplement).

### 2. Includes and components

- **What:** The sidebar toggle is repointed (`:scp-wiki:component:toggle-sidebar` → `:scp-jp:component:toggle-sidebar`, candidate L5). The frame include is repointed to `:scp-jp:component:interwiki-style` (candidate L9–12; its delivery aspect is section 3), and the original's second, byte-identical frame include (original L14–17, same priority, same theme=) is not carried: the candidate holds the frame once. The two image-block exhibits keep the original's bare form, `[[include component:image-block …]]` with the asset re-hosted (candidate L43, L58; the original's bare form is original L39 and its twin) — a bare component name resolves on the reader's own wiki, so the carried form names the JP component on scp-jp exactly as it named the EN one on scp-wiki. The credit and license includes are section 1. No component swap (T8) was needed.
- **Why:** P1 (KB-15) for the repoints. The frame deduplication removes a redundancy of the original's own making: two identical layers at the same priority apply the same stylesheet twice, and one application is the whole effect.
- **Verify:** `grep -c 'interwiki-style' original.txt candidate.txt` — 2 and 1; `grep -n '\[\[include' candidate.txt` — six includes, JP-side or bare-local as above.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The original's module CSS imports its stylesheet in the page-URL form, `https://scp-wiki.wikidot.com/theme:our-open-veins/code/1` (original L2); the candidate imports `local--code/theme%3Aour-open-veins-jp/1` from the draft host (candidate L2, block B1), the settled JP delivery form. The frame's `theme=` names the same /1 on the draft host (candidate L11) — where pack-of-peanuts in this batch already carries the production-host form in its frame, this candidate's frame is still in draft form, and both of its delivery lines are therefore class (iii). Inside the CSS, the asset URLs re-host to the draft folder (blocks B60, B64, B67, B68, DRAFT-HOST). The original's second module, the tail variation block, is treated in the per-theme record: it is a delivery element (a real `[[module css]]`, not an exhibit), and its absence is the package's flag, not a delivery decision this section can narrate as normal.
- **Why:** P4/T9 and P6/T3 for the import form and the frame. The draft-host lines are KB-41, class (iii).
- **Verify:** `grep -n 'local--code\|module CSS' candidate.txt` — L1–3 and L11; the original's second module is at original L950 (`[[module css]]` inside the comment at L948).
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)); the variation module's absence is flagged below, not dispositioned.

### 4. Fonts and assets

- **What:** The original's three display faces (Rubik Distressed, Road Rage, Jost) load from Google Fonts on both sides (the loads sit at the CSS head; original L175–176 zone, candidate L173–177, block B59), and the candidate adds the two JP companions the license box's fonts entry names: Noto Sans JP and Noto Serif JP loads (JPFONT-LOAD inside B59), with 'Noto Sans JP' / 'Noto Serif JP' appended in the font stacks at four loci (blocks B61, B62, B63, B65, B66, JPFONT-STACK). Both added faces are loaded in-file, so the KB-16 gap (a named face loaded nowhere) does not arise. Assets: the theme's own images (Dark Mode.png, Florcita.png, the header and sidebar images) re-host from `scp-wiki.wdfiles.com/local--files/theme:our-open-veins/` to the draft host's `theme%3Aour-open-veins-jp/` folder, filenames unchanged (candidate L43, L58 and the CSS's url() targets); the render row records one of them, Dark Mode.png, as broken in the T3 capture and deferred (section 11).
- **Why:** P7/T5 with KB-16 (load and stack append together). P5/KB-17 for the asset re-hosts (the draft folder is the candidate's own).
- **Verify:** `grep -n 'Noto Sans JP\|Noto Serif JP' candidate.txt` — the loads at the CSS head and the stack appends; `grep -n 'sigma10-jp-test.wdfiles.com/local--files' candidate.txt | head`.
- **Disposition:** Applied; the draft-host asset URLs are DISPOSITIONED (class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** The theme's masthead surface keeps its in-universe strings in English: that is the T4 row's single display-affecting finding for this theme, recorded verbatim as "P9 (in-universe masthead strings EN, display-affecting)" (LOCALIZE-ROWS row 118) and dispositioned under ruling 2 in the (c3) register. No header variable was translated, so KB-57's kept-form mechanics are the ground here, and the disposition is the campaign's own, not this package's. The sidebar toggle include is section 2; the sidebar's rules are carried apart from the font stacks and asset hosts of section 4. No P8 layout adaptation was needed.
- **Why:** P9/T6 with ruling 2: header title language is case-by-case translation taste and out of scope for migration correctness; the ledger recorded the choice and its display effect openly (the finding is counted, not hidden).
- **Verify:** LOCALIZE-ROWS row 118 states the finding in the words quoted above.
- **Disposition:** DISPOSITIONED (ruling 2; (c3) register, our-open-veins line).

### 6. Text translation

- **What:** The body is translated throughout: the usage prose, the two footnote samples (both translated, candidate L35), the color-variation documentation (candidate L39–53), and the formatting examples, in fifteen TRANSLATION-ANCHORED blocks and the one-line TRANS-UNANCHORED grain (30 primaries), each verified against the mirror for this README. Two exhibit texts are kept byte-identical rather than translated or repointed: the usage exhibits (candidate L33 and L53), treated in the per-theme record. R1 in-CSS text: two section comments are translated inside the CSS (COMMENT-TEXT labels inside B59 and one further block); the CSS's remaining comments are structural labels carried in English, porter-visible only. The attribution prose's second printing (the lead paragraph) is translated at candidate L29, as section 1 records.
- **Why:** P10 and KB-18 (reader-visible strings localize). The variation documentation's translation is complete and competent — which is precisely why the missing implementation of section 3 stands out: the text promises a feature the file no longer carries.
- **Verify:** The pairs are diff.md's body sections in order; an English-prose scan of candidate.txt outside the credit fields returns the two exhibits, the masthead strings of section 5, and proper nouns.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme FINDINGS with the one dispositioned item of section 5 (LOCALIZE-ROWS row 118).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L24), naming the original on scp-wiki.wikidot.com, the host the campaign's provenance records name for it. The body keeps its link to the setting's hub on the original wiki, `[https://scp-wiki.wikidot.com/our-open-veins-hub Our Open Veinsカノン]` (candidate L29): the hub is an EN-wiki page the JP environment does not replace, so the serving original is the correct target and only its label is translated. The license entries' source links name the original's file area (candidate L954 zone), which is where those files are in fact distributed. No link in the candidate is dead on the evidence of the mirror.
- **Why:** P11: prose links take the JP counterpart or the serving original; the hub has no JP counterpart in this campaign's scope.
- **Verify:** `grep -n 'our-open-veins-hub' candidate.txt` — candidate L29.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds for the carried content: the exhibit census corresponds one to one (usage exhibit, variation section with its image exhibits, the formatting examples, the footnote samples, and the CSS code exhibit at original L172–943 → candidate L169–943), and the JP corrections arrive as the head delivery pair, the credit swap, and the license-box installation. The one structural fact that does not fit the rule is the tail: the original continues for 204 lines after its tag gate with the variation module (original L948–1151), and the candidate ends at its license box. Because a color variation is a feature, not an exhibit, the census above is stated over the gated body and the tail is handled as its own item below rather than absorbed into a "corresponds" claim.
- **Why:** R3: a restructure and a silent deletion share a diff shape; the census decides for the body, and the tail fails it, which is the flag.
- **Verify:** `wc -l original.txt candidate.txt` — 1,151 and 968; `grep -n 'module css' original.txt` — the second module at original L950 has no counterpart line in the candidate.
- **Disposition:** Standing for the gated body; the tail module is flagged below (not dispositioned by any record this package can cite).

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation anywhere in the pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** No comment-form annotations (`[!-- … --]`) and no editor lines exist in the candidate — checked directly, not inferred from the skeleton (the candidate contains no `[!--` at all; the only comment-opener in the pair is the original's variation gate, section 3). The license box's four entries (section 1) are porter-authored record text in the box's own form, not annotations. One absence is worth stating here because a reader will look for it: the original's variation block carries the author's own parameter marker (`{$our-dark-veins}`), which is mechanism, not annotation, and it left with the module.
- **Why:** R2: porter-added text is part of the change record; here the added text lives in the credit and license forms and is recorded in section 1.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) The P9 masthead strings (section 5): kept in English as in-universe text, counted by T4 as the theme's one display-affecting finding, and dispositioned under ruling 2 in the (c3) register. (2) The render row's items, all environment, capture, or asset layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); the T3 capture's broken Dark Mode.png, recorded as deferred in the row itself (the asset's draft-host copy did not serve in that capture; its re-host is section 4); and the "使用方法" heading wrapping one character per line at 320 width, recorded in the row as cosmetic. The T1 register's seven pseudo-ref errors are the candidate's own draft-host delivery and asset lines, class (iii). The variation module's absence (per-theme record) is deliberately not listed here: no record dispositions it, and listing it would manufacture a ground the campaign never gave.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes; ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 118 and register (c1).
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 118): exit 1, 7 errors / 0 warns / 1 info; all seven errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN15)): FINDINGS, the items of section 11(2), all dispositioned or deferred in the row; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 118): FINDINGS jointly, display-affecting findings 1 (the section 5 item); the (c3) register dispositions it under ruling 2. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Churn counts quoted above describe the pre-repair candidate; the regenerated diff.md for the current candidate reports +136/−119 in 13 hunks (GNU-diff 196 changed lines), and that is the authoritative count for the bytes now in this package. One limit of the record deserves stating: every check above ran against a candidate that lacks the variation module, and none of them charged its absence — the T2/T3 row's sample exercised the theme page and its decoration sample, not a page including the theme with the variation parameter — so the PASS and this flag coexist without contradiction: the flag is new evidence, not a re-judgement of the checks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:our-open-veins-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 118; go-sign, COMPLETION-REPORT §10), with the per-theme flag below standing as this package's addition to the record.

## Per-theme record

### The color-variation module is absent (flagged by this package)

The original ends, after its tag gate, with the "Our Dark Veins" variation implementation (original L948–1151): a Wikidot comment opener carrying the include parameter, `[!-- {$our-dark-veins}`, a full second `[[module css]]` (original L950–1150) restating the theme's variables and rules in the variation's dark palette (its `--hover-color: rgb(100,7,14)` at original L953 against the base theme's rgb(158,173,66)), the module close, and the comment close `[!----]` (original L1151). The mechanism is the theme's documented one: a page includes the theme with the parameter set (`|our-dark-veins= --`, the exhibit at candidate L53), the parameter substitution breaks the comment open, and the variation module applies. The candidate contains no trace of it: no `[!--` anywhere, no second module, none of the variation's values (a search for `100,7,14` returns nothing). At the same time the candidate keeps, translated, both the variation's documentation (candidate L45–53: what the variation is, that it suits darker tales) and its activation exhibit (candidate L53). A JP author following the candidate's own instructions would include a parameter that nothing in the file reads, and get the base theme. The classifier files the deletion as block B71 under DELIVERY-MOVE, the label the campaign's standing warnings single out as able to hide a dropped module; no ledger line, T4 item, or (c3) entry for this theme mentions the variation, so the drop is undispositioned. This package flags it with the line ranges above and leaves the candidate unedited; restoring the block (translated comments, re-hosted assets) or documenting the variation as not ported is a coordinator decision.

The restoration has since landed — FIX-GATES1, canonical commit `2437aa62e7ab39f7b737695a8887924de1428fe7` ("pages: our-open-veins variation module restored", 2026-11-17; report `R/review-scout/FIX-GATES1.md`). On the current candidate the "Our Dark Veins" module stands at candidate L970–1173 (the file's last line), a pure append after `[[/iftags]]` in the original's gated form: `[!-- {$our-dark-veins}` opens it (L970), the `[[module css]]` carries the dark palette (`--hover-color: rgb(100,7,14)` at L974) and the restated rules, and `[!----]` closes it. Its one asset reference, the dark header image, was repointed to the candidate's own draft-host `local--files/theme%3Aour-open-veins-jp/header-coso-darks.png`; otherwise the 204-line block is byte-identical to the original. The checker reported no new class (i) error before or after, and the module is now read by the activation exhibit at candidate L53. This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:our-open-veins-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

### The usage exhibits keep the original's bare form (flagged by this package)

Both usage exhibits print the include in the original's bare local form: `@@[[include theme:our-open-veins]]@@` (candidate L33) and the variation form (candidate L53). They are byte-identical to the original's exhibits (original L33, L53 zone), so this is not the repointed-plain-slug family flagged in the plant, parawatch-pumpkin, and pack-of-peanuts packages, where a porter rewrote the wiki prefix and kept the plain slug. But the user-facing fact is the same shape: on scp-jp the bare name resolves locally, to a page theme:our-open-veins that will not exist (the candidate posts as theme:our-open-veins-jp). The exhibits are flagged here with their loci so the coordinator's exhibit sweep can take the bare form into its scope if it chooses; the candidate is left unedited.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-our-open-veins-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments and no inbound-link repairs in other candidates for this theme; the variation module, if restored, would return to this same file's tail.

## License and attribution

- **Title:** Our Open Veins Theme
- **Author:** Dc_Yerko, Kilerpoyo
- **Source:** https://scp-wiki.wikidot.com/theme:our-open-veins — revision 17
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
