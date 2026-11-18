# Review package — theme:magpie-swoops-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:magpie-swoops-jp — origin EN, population #111 [GOSIGN2-LEDGER (b) row 111]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 86e84fd8ba2601ba56c292ebdde4947777109eb16a20859ddf6ba1926e121afe); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 0 infos (hotlink×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 111; GOSIGN2-LEDGER (b) row 111]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + scp-wiki.wikidot.com; sample T2 no machine verdict (exit 2); T3 page wordmark "MAGPIE SWOOPS財団" overprints account links and clips at 375/320 (both engines). [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 111, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 111]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 111]
- Computed against: canonical commit 1e34c0b668faf170da8af14c127251af3e35fa26; candidate file pages/theme:magpie-swoops-jp.txt sha256:86e84fd8ba2601ba56c292ebdde4947777109eb16a20859ddf6ba1926e121afe; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/magpie-swoops-jp/candidate.txt (sha256 59e2c140e26ff72850a1922723a557f7b55fd102d0fd651777ea094ebd58b993)
Original: theme:magpie-swoops — scp-wiki, revision 12 (sha256 d190b999f1b79784d597036b6fd1c9d62f4e4b0db2a79dc538c7cd2328b14ea5)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Check | Verdict |
|---|---|
| Population row | PASS [GOSIGN2-LEDGER (b) row 111] |
| T1 source check | FINDINGS (classified) — 2 errors / 0 warns / 0 infos (hotlink ×1, pseudo-ref ×1) [T1-ROWS row 111] |
| T2/T3 render | FINDINGS — page runtime-hotlink site-theme chain + scp-wiki.wikidot.com; sample T2 no machine verdict (exit 2, coverage caveat); T3 wordmark overprint/clipping at 375/320 [RENDER-ROWS-2 (RENDER-S2-C (EN14))] |
| T4 localize patterns | FINDINGS — display-affecting 1 (P5) [LOCALIZE-ROWS row 111] |
| Generated stamp | STALE — the candidate changed after the ledger determination (one usage line, in the post-determination sweep); the pre-change verdict lines are preserved in the stamp and the change is recorded under Per-theme record below |

## Provenance

| Item | Value |
|---|---|
| Original page | theme:magpie-swoops (scp-wiki) |
| Reference revision | 12 — first-translation revision |
| Mirror class | COPY (stored mirror file used as-is) |
| Mirror file | R/review-mirrors/orig-magpie-swoops-rev12.txt |
| Original SHA-256 | d190b999f1b79784d597036b6fd1c9d62f4e4b0db2a79dc538c7cd2328b14ea5 |
| Candidate file | pages/theme:magpie-swoops-jp.txt |
| Candidate SHA-256 (this package) | 59e2c140e26ff72850a1922723a557f7b55fd102d0fd651777ea094ebd58b993 |

Provenance route: standard derivation from the EN branch original at the reference revision (sources.tsv kind `standard`, verdict PASS, notes empty). The candidate entered the canonical repository in the Stage 2 EN14 creation commit 49c7627 (the whole port, credit block included), then received the FIX-CREDIT-D attribution normalization in 1869877 and one usage-line repair in the post-determination sweep commit b5cb724; the wave acts are verified line by line under Per-theme record.

## Summary

A Black Highlighter layered theme: the original imports the BHL stylesheets, frames them at priorities 1–2, documents itself in a full prose body (About, How to use, Examples with samples and footnotes, Theme code), and self-delivers its exhibit CSS from code block /1 through a tail module and a priority-3 frame. The port keeps every layer: the JP BHL base include and JP-hosted BHL imports replace the CDN delivery, the body is translated in place wholesale (prose, samples, footnotes, exhibit strings), the exhibit's font imports move from bunny.net to Google Fonts, the font stacks gain JP system faces, and the tail self-delivery names the candidate's own draft-host code address. One defect is flagged by this review: the BHL base include is wrapped in a condition-less `[[iftags]]` gate (cand L1–3), the KB-08 anomaly shape, which no ledger row charges. Two tail-line form deviations (a missing semicolon, a space inside a frame parameter) are recorded as observations; the render record shows the delivery working.

## Class summary

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 39 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 7 |
| FONT-IMPORT | 1 |
| HEADERVAR | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 6 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 86 |
| TRANSLATION-ANCHORED | 23 |
| WS-ONLY | 3 |

Counts: 132 blocks, 38 specific, 83 heuristic, 11 residue, 0 skipped (comment text). Diff size (this package's generator): −191/+199 lines by GNU diff on the packaged pair (the generator's difflib count differs; original 551 lines, candidate 559).

Adjudication of the classifier's labels against the bytes, where they diverge: the heuristic mass (TRANS-UNANCHORED ×86 with COMMENT-TEXT ×39 inside it) is the expected shape of a whole-body in-place translation plus the exhibit's CSS comments; it resolves by shape in sections 6 and 9 and the Appendix, and the exhibit census is equal on both sides (collapsibles 8 = 8, code blocks 1 = 1, theme-squares 1 = 1, image-block samples 3 = 3, tabviews 2 = 2), so the seven EXHIBIT-RESTRUCTURE primaries are alignment artefacts of translated exhibit furniture, not restructures. FONT-IMPORT (B77) carries the signature table's KB-04 description (malformed family parameters), but both sides' family parameters are well-formed; the act is a host repoint (bunny.net → Google Fonts) at creation, recorded in section 4. COMPONENT-SWAP (B11) is the usage exhibit's include lines changing escape form (`>` quotation to `@@…@@`) while repointing; the same three includes stand on both sides, so it is adjudicated in sections 2 and 7, not as a component swap. CSS-BODY (B82) is the font-stack supplement zone, a P7 act in system-face form, narrated in section 4. The bare-gate shape at cand L1 is noted by the classifier on B1 but carries no signature; it is adjudicated as the KB-08 defect in sections 2 and 8.

## Standing sections

### 0. Header / provenance

**What.** The candidate's head is a delivery head, not a frame: a bare `[[iftags]]` gate wrapping the JP BHL base include (cand L1–3), then the body gate `[[iftags +テーマ]]` (cand L5), a head CSS module importing the two BHL stylesheets from the JP host (cand L7–10), and the two interwiki frames at priorities 1 and 2 (cand L12–20). The original opens with a single whole-page `[[iftags +theme]]` gate (orig L1), a head module importing BHL from cdn.scpwiki.com (orig L2–5), and the same two frames (orig L7–15). Provenance data is the table above; the theme's identity variables sit in the exhibit (:root at cand L276–284: --theme-base "black-highlighter", --theme-id "magpie-swoops", --theme-name "Magpie Swoopsテーマ").

**Why.** The head shape is the campaign's BHL layering form (P4/T9 delivery repoint plus the base include) with the gate localization of P2/T2 (KB-08, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): the base must load unconditionally and the documentation body only on theme-tagged pages. The condition-less wrapper around the base include breaks that split; it is flagged in section 8.

**Verify.** `head` both files: the gate forms and the frame priorities read off directly; `grep -n "iftags" candidate.txt` shows exactly two gates (L1 bare, L5 +テーマ) plus the closer at L549.

**Disposition.** No header item is charged against this theme in any row; the gate anomaly is this review's flag (section 8), outside the ledger's verdicts.

### 1. Credit and attribution

**What.** The candidate's credit block (cand L22–31, inside `:scp-jp:credit:start-preview`/`end-preview`) carries all eight TASL fields: タイトル "Magpie Swoops Theme", 翻訳責任者 "AI", 翻訳年 2026, 原題 "Magpie Swoops Theme", 著作権者 "Sinking_Otter", 作成年 2025, 初訳時参照リビジョン 12, and 元記事リンク to https://scp-wiki.wikidot.com/theme:magpie-swoops — the host recorded in sources.tsv for this theme, so no cross-host probe arises. The author field matches the original's own attribution: the About prose names the creator as "created by [[*user Sinking_Otter]]" (orig L27). The original's info module (orig L17–21, `:scp-wiki:info:start`/`more`/`end`) is removed with the swap (INFO-DEL inside B6); its placeholder instruction line is module furniture, and its one content sentence (the Australian-magpie territory fact, orig L20) is not carried anywhere in the candidate — stated here for the record; the theme's other magpie facts, which live in the body proper, are translated in place (footnote at cand L124, collapsible text at cand L140–141).

**Why.** The credit swap is P3/T1 (KB-21, KB-22): the JP environment's preview credit module is the rate-bearing form and the branch-original info module does not render here; carrying the TASL fields in the block is what lets a reader trace the port to its source and author. The field set was complete from creation (commit 49c7627); only the attribution value changed later (section: Per-theme record).

**Verify.** Read cand L22–31 against orig L17–21 and L27; `grep -n "scp-wiki.wikidot.com" candidate.txt` returns the credit link (L30) and the two P5 asset lines only.

**Disposition.** The T4 row charged P3-class credit content as complete for this theme (its one display-affecting finding is P5, section 4); population-wide, the ledger's assembly note records credit-missing-fields = 0 after the credit waves. The info-pane sentence's non-carriage rides inside the sanctioned module swap and is not separately dispositioned.

### 2. Includes and components

**What.** Includes, candidate side: the BHL base include (L2, inside the bare gate — see the flag below), interwiki-style frames ×3 (L12–15 priority 1, L17–20 priority 2, L556–559 priority 3; priority-distinct layers of one component, not duplication), the credit pair (L22, L31), theme-squares with translated color names (L57–…), image-block sample (L118–122), and the live toggle-sidebar include at the tail (L551). The usage exhibit (cand L46–48) shows the three user-facing includes in `@@…@@` escape form, all `:scp-jp:` with the self-include in -jp form. INCLUDE-REPOINT fires ×6 across these. The gate structure changed: the original's one whole-page `[[iftags +theme]]` (orig L1, closed at orig L540) became a bare gate for the base include (cand L1–3) plus a `[[iftags +テーマ]]` body gate (cand L5, closed at cand L549) — IFTAGS (B1).

**Why.** Repointing includes to the JP site is P1/T3: an include naming the EN site resolves there or nowhere in this environment. The gate localization is P2/T2 (KB-08): JP tag names in JP conditions. KB-08's anomaly clause is the failure this theme hits: a bare `[[iftags]]` with no condition is nonstandard, its empty-spec handling applies unpredictably, and an include wrapped in it loads under rules no other theme follows. The classifier notes the bare form on B1 but has no signature for it; the pattern's index instance is aesthetic-theme (REPORT-GOSIGN2-LOCALIZE-A row 1 note).

**Verify.** `grep -n "\[\[include\|\[\[iftags" candidate.txt` lists every include and both gates; the KB-08 detection is the same grep: a `[[iftags]]` line with no tag argument wrapping the base include at L1–3.

**Disposition.** The include repoints ride the port's P1 class, uncharged per-theme. **Flag (this review): the condition-less gate at cand L1–3 is the KB-08 class-A anomaly; no ledger row charges it for this theme (the T4 row's single display-affecting finding is P5). The pattern's recorded fix is to give the gate the standard +テーマ condition or remove the wrapper to match the original's structure. Recorded here and in the lane report; the candidate is not edited.**

### 3. Delivery and code loading

**What.** Two delivery paths, both repointed. Head: the BHL stylesheets move from cdn.scpwiki.com (orig L3–4, L9, L14) to scp-jp.github.io/Black-Highlighter (cand L8–9 in the module; the frame theme= parameters at cand L14, L19 — residue R1/R2, whose lines carry no signature of their own). Tail: the theme's own exhibit is self-delivered exactly as in the original — a tail module importing code block /1 and a priority-3 frame naming it (orig L544–551 → cand L553–559) — with the address repointed from the original's scp-wiki.wdfiles.com local--code/theme%3Amagpie-swoops/1 to the candidate's own sigma10-jp-test.wdfiles.com local--code/theme%3Amagpie-swoops-jp/1 (DELIVERY-HOST + DRAFT-HOST + SELF-DELIVERY on B130 and B132, class (iii) draft-stage form). The page holds exactly one `[[code]]` block (the Theme code exhibit, cand L270–…), so /1 names the CSS exhibit: the FIX-CODEADDR population audit lists no mismatch for this theme. Two form deviations ride on the tail lines: the candidate's @import at L554 lacks the trailing semicolon the original's line carries (orig L545), and the frame parameter at L558 reads `theme= https://…` with a space the original does not have (orig L550).

**Why.** Host repoints are P4/T9: deliveries are served from the JP hosts in this environment, and a self-delivery must name the candidate's own page or it serves the EN original's code (or nothing). The draft host in the tail lines is the class (iii) draft-form of KB-41: correct for the check environment, replaced at posting. The form deviations have no class; they are recorded because the render evidence (section 12) shows the delivery working despite them, so they are observations, not breaks.

**Verify.** `grep -n "local--code" candidate.txt` returns exactly the two tail lines; `grep -c "\[\[code" candidate.txt` returns 1; the FIX-CODEADDR audit (R/review-scout/FIX-CODEADDR.md) is the population cross-check.

**Disposition.** Class (iii) draft-form under T1 disposition class (iii), population-wide (KB-41); no delivery item is charged against this theme individually.

### 4. Fonts and assets

**What.** The exhibit's four display-face imports move from fonts.bunny.net to fonts.googleapis.com with identical family parameters (Creepster, Ubuntu Sans Mono, Averia Sans Libre, New Rocker; orig L263–266 → cand L271–274, FONT-IMPORT B77) — a creation act: no committed version of the candidate ever contained the bunny.net lines (git log -S "bunny" is empty for this file). The four font stacks gain JP system faces (cand L294–297: "Hiragino Maru Gothic ProN"/"Yu Gothic" on --UI-font, "Yu Mincho"/"Hiragino Mincho ProN" on --header-font, "Yu Gothic" on --title-font, "BIZ UDGothic" on --mono-font; CSS-BODY B82) — platform fonts, loaded by no import because none is needed. Every Latin face named in the stacks is loaded by the exhibit imports above, which are live through the tail /1 delivery. Assets: the magpie logo names EN storage twice — the image-block sample (cand L119) and --logo-image (cand L288) — both with the page-name colon %3A-encoded (KB-01); the --logo-image line also carries the original's own leading space inside url(" …") (orig L280), kept as-is.

**Why.** The import repoint is the pattern-2 shape (P5, KB-03/KB-04 family): bunny.net delivery was the campaign's named font-delivery problem, fixed per-theme where the bytes allow; here the porter made the change at creation, so no row charges it. The stack additions are P7 (KB-05) in system-face form: without JP faces in the stacks, Japanese text falls back to platform defaults and the theme's typeface design is lost on JP pages. The EN-storage logo is P5's charged item for this theme.

**Verify.** `grep -n "@import" candidate.txt` lists the head BHL imports, the four exhibit font imports, and the tail self-delivery; `grep -n "wikidot.com/local--files" candidate.txt` returns exactly L119 and L288.

**Disposition.** P5 DISPOSITIONED under T1 class (ii) (posting-procedure) / KB-58 [ledger (c3), magpie-swoops-jp line] — the EN-storage assets are the display-affecting finding of LOCALIZE-ROWS row 111, left for the posting step. The font acts are uncharged (creation-form, sections above).

### 5. Header, sidebar, site furniture

**What.** The header variables sit in the exhibit's :root: --header-title stays "Magpie Swoops" (cand L289, = orig L281) and --header-subtitle is translated, "Stories From Behind The Veil" → 「ヴェールの裏側からの物語」 (orig L282 → cand L290) — HEADERVAR ×2, split across the two variables. --theme-name reads "Magpie Swoopsテーマ" (cand L283, CONTENT-STRING B80), the mixed form. The toggle-sidebar component is included live at the tail (cand L551) and shown in the usage exhibit (cand L48), as in the original (orig L542, L40). The render record's furniture item is the T3 wordmark: "MAGPIE SWOOPS財団" overprints the account links and clips at 375/320 in both engines.

**Why.** Header variables are P9/T6 (KB-57): the theme's visible title surface. Ruling 2 takes header and title language choice out of migration-correctness scope; the subtitle's translation is a P10 act the porter chose, and the title's retention is the same choice in the other direction. The wordmark item belongs to the KB-35 responsive family (fixed site furniture text meeting a long theme wordmark at phone widths), not to the variable values.

**Verify.** `grep -n "header-title\|header-subtitle\|theme-name" candidate.txt` returns L283, L289, L290; the wordmark evidence is the RENDER-ROWS-2 row cited in section 12.

**Disposition.** No P9 item is charged or dispositioned for this theme in the ledger (its (c3) line carries P5 only); the T3 wordmark item is DISPOSITIONED in the render register (KB-35 family).

### 6. Text translation

**What.** The documentation body is translated in place, wholesale: About (cand L33–37), How to use (L42–50), the theme-color names inside theme-squares (L58–…, e.g. パンプキンオレンジ, スライムグリーン), Examples (L116–…) including the horizontal-rule prose with its magpie footnote translated (L124), the link samples' text (L126–127), the title-examples collapsible (L131–138), the swooping collapsible (L140–141), and the Theme code exhibit's strings — collapsible labels (L269), the :root comments (L277–284), section comments throughout (COMMENT-TEXT ×39 plus residue R5–R11), and the subtitle and theme-name strings of section 5. TRANSLATION-ANCHORED ×23 marks the anchored pairs; the remaining pairs are the heuristic mass adjudicated in the Class summary. The one non-carriage is the info pane's fact sentence, recorded in section 1.

**Why.** Body and comment translation is P10 (KB-18): the documentation is the theme's user surface in the JP environment, and the CSS comments are the exhibit's own documentation for porters. Unanchored pairs are the queue where restorations and exhibit changes hide, which is why the exhibit census in the Class summary is the deciding check here: it is equal, so the mass is translation, not loss.

**Verify.** The census commands of the Class summary (`grep -c` for collapsible/code/theme-squares/image-block/tabview on both files), then spot-read cand L116–141 against orig L108–135.

**Disposition.** T5 FINDINGS under the joint T4/T5 verdict [LOCALIZE-ROWS row 111]; the translation itself is the port's purpose and is not an open item.

### 7. Links

**What.** The visited-link sample is repointed from scp-wiki.wikidot.com to scp-jp.wikidot.com with its text translated (orig L118 → cand L126, LINK-REPOINT ×1); the nonexistent-link sample is translated as text (orig L119 → cand L127) and names no page. The credit block's source link is treated in section 1 (recorded host, exact). The usage exhibit's self-include reached its -jp form in the post-determination sweep (cand L47; Per-theme record).

**Why.** Sample-link repoints are P11: a documentation sample that sends JP readers to the EN site teaches the wrong environment; the repoint keeps the sample's semantics (a visited link) inside the JP site.

**Verify.** `grep -n "scp-jp.wikidot.com\|scp-wiki.wikidot.com" candidate.txt` returns L30 (credit), L119 and L288 (the P5 assets), and L126 (the sample).

**Disposition.** No link item is charged against this theme; the P5 asset lines are dispositioned in section 4.

### 8. Structure

**What.** The structural change is the gate restructure of section 2: one whole-page gate becomes two (bare base gate + +テーマ body gate), with the body otherwise in the original's order and the tail furniture (toggle-sidebar, tail module, priority-3 frame) in the original's positions (orig L540–551 → cand L549–559). Nothing is reordered inside the body; the exhibit census is equal. The KB-08 flag of section 2 is this section's item as well: the bare gate is a structural deviation from both the original's form and the campaign's BHL form (base include ungated or +テーマ-gated elsewhere).

**Why.** Gate structure is what decides where the theme's CSS and furniture apply (P2/T2, KB-08); a condition-less gate's empty-spec behavior is unpredictable by the pattern's own mechanism note, so the deviation is recorded as a defect even though this theme's render record shows styled output on the check pages.

**Verify.** `grep -n "iftags" candidate.txt` (L1, L5, L549) against `grep -n "iftags" original.txt` (L1, L540); the census of the Class summary for the body's integrity.

**Disposition.** No structural item is charged in the ledger; the bare-gate flag is open at this review and recorded for the coordinator (sections 2 and Per-theme record).

### 9. Formatting only

**What.** WS-ONLY ×3 and residue R4 (a whitespace-only line inside the exhibit, orig L302) are the formatting mass: whitespace-only hunks with no content change. The candidate preserves the original's indentation inside the exhibit (4-space rule bodies) and its blank-line rhythm in the prose body.

**Why.** No class: formatting-only hunks change no rendering and are recorded so the diff's line count is not mistaken for content churn (KB-18's census discipline).

**Verify.** classification.json's WS-ONLY spans; `diff` on the packaged pair shows the three hunks as whitespace-only.

**Disposition.** None required; not a ledger item.

### 10. Porter annotations

**What.** None. Neither file contains a `[!--` comment (grep count 0 on both sides); the candidate's only comments are the exhibit's translated CSS comments, treated in section 6.

**Why.** Porter annotations (T12) are the class that would need adjudication here; their absence is stated with its ground so the empty section is a checked fact, not an oversight.

**Verify.** `grep -c "\[!--" candidate.txt original.txt` returns 0 and 0.

**Disposition.** None; no annotation item exists for this theme.

### 11. Dispositions and exceptions

**What.** The theme's disposition set: P5 (the two EN-storage logo references) DISPOSITIONED under T1 class (ii) / KB-58 [ledger (c3)]; the T1 baseline classes (hotlink ×1, pseudo-ref ×1) dispositioned in register (c1) — the hotlink is the EN-storage class and the pseudo-ref the @@-exhibit class; the render items DISPOSITIONED in the render register (runtime-hotlink chain, KB-40; wordmark overprint, KB-35 family; the sample's T2 exit 2 is a coverage caveat, not a theme defect); the tail draft-host lines are class (iii) draft-form (KB-41). This review's KB-08 bare-gate flag is NOT in the disposition set: it is an open finding recorded by this package.

**Why.** Dispositions are the ledger's mechanism for separating "wrong here" from "wrong at posting" and "not measurable here"; restating them per theme keeps the package from re-litigating settled items while keeping genuinely open items (the gate) visible as open.

**Verify.** The theme's lines in ledger registers (c1), (c2), (c3) under review/AUTHORITIES/ledger-parts/, against sections 2–5 above.

**Disposition.** As stated per item; the population verdict is PASS [GOSIGN2-LEDGER (b) row 111] with FIX5: none.

### 12. Verification

**What.** The stamp's evidence chain: T1 baseline 2026-11-16, exit 1, 2 errors / 0 warns / 0 infos [T1-ROWS row 111]; T2/T3 combined FINDINGS [RENDER-ROWS-2 (RENDER-S2-C (EN14))] — page runtime-hotlink site-theme chain + scp-wiki.wikidot.com, sample T2 no machine verdict (exit 2), T3 wordmark "MAGPIE SWOOPS財団" overprinting and clipping at 375/320 in both engines, credit-modal line not recorded; T4 FINDINGS with display-affecting 1 [LOCALIZE-ROWS row 111]; FIX5: none. The generated stamp reads STALE because the candidate changed after the determination (the sweep line, below); its pre-change verdict lines stand as the ledger's judgement of the file.

**Why.** The four test layers are independent instruments (source, render, localize patterns, translation); the package's job is to let a third party re-derive each verdict from the cited record without trusting this README's prose.

**Verify.** Re-run the T1 checker on candidate.txt (2 classified findings expected at baseline classes); read the RENDER-ROWS-2 and LOCALIZE-ROWS rows named above; `python3 review/build_review.py --check` confirms this package's generated files match the canonical candidate.

**Disposition.** Population PASS at the ledger determination; the STALE stamp is a freshness marker, not a re-judgement.

## Per-theme record

Wave narration, each act verified against the diff and the file's git history (canonical repository):

1. **Stage 2 EN14 creation, commit 49c7627** — the whole port in one act: the BHL layering rebuilt on JP delivery (base include, scp-jp.github.io imports, frames at priorities 1–2), the credit block with all eight fields (attribution value "SCP-JP" at this point), the info module removed, the body translated in place wholesale, the exhibit font imports repointed from bunny.net to Google Fonts (no committed version of the file ever contained the bunny lines), the JP system faces added to the four stacks, the colon encodings applied, and the tail self-delivery written against the candidate's own draft-host code address. The bare `[[iftags]]` wrapper around the base include also dates from this act. The commit subject ("Stage 2 EN14: theme port candidates") claims exactly this scope; the bytes match it.
2. **FIX-CREDIT-D, commit 1869877** — one line in this file: 翻訳責任者 "SCP-JP" → "AI", the population attribution normalization. The subject matches the bytes exactly.
3. **Post-determination usage sweep, commit b5cb724** — one line: the usage exhibit's self-include `[[include :scp-jp:theme:magpie-swoops]]` → `theme:magpie-swoops-jp` (cand L47). This act postdates the ledger determination and is the whole cause of the stamp's STALE reading: the verdict lines in the stamp judge the pre-sweep file, and the sweep line is a repair in the campaign's own direction (a usage sample naming a nonexistent plain-form page was the sweep's target class), so the package records it here rather than treating the stamp as a defect.

Defect flag recorded by this review (not edited): the condition-less `[[iftags]]` gate wrapping the BHL base include (cand L1–3) is the KB-08 anomaly — class A, file-provable, with a recorded fix (condition the gate +テーマ or remove the wrapper). It is uncharged by every ledger row for this theme. Two lesser observations ride with it: the tail @import's missing semicolon (cand L554) and the space inside the tail frame's theme= parameter (cand L558); both deviate from the original's line forms, and the render record shows the delivery functioning, so they are recorded as form deviations for the coordinator's judgement, not as breaks.

Discrepancies between record and bytes: (i) the ledger's (c3) line for this theme charges only P5, yet the bytes contain two further campaign-class acts it never mentions — the pattern-2 font repoint (creation) and the P7 stack supplement; both are benign and verified above, and the silence is the record's, not the file's. (ii) The T4 row's display-affecting count (1) is consistent with the bytes once the creation-time repoint is understood: at T4 time there was no bunny.net line left to charge. (iii) The classifier's KB-04 description on B77 and its COMPONENT-SWAP primary on B11 do not fit the bytes; both are adjudicated in the Class summary.

### Post-package repairs (REFRESH3-G)

- **FIX-U7, landing `1e34c0b668faf170da8af14c127251af3e35fa26`** ("pages: U-7 repairs …", 2026-11-17, R/review-scout/FIX-U7.md item 2): the condition-less `[[iftags]]` gate at the file head was conditioned to `[[iftags +テーマ]]` (refreshed candidate L1; the closing `[[/iftags]]` at L3 and the file's second gate at L5 are unchanged). This is KB-08's recorded fix branch — restore the original's +theme condition rather than remove the wrapper, since the original's base delivery module stands under `[[iftags +theme]]` (orig L1) — using the candidate's own localized `+テーマ` form. The "Defect flag recorded by this review (not edited)" paragraph above is the as-built record; the gate is now conditioned in the recopied candidate. The two render-benign form deviations (unterminated tail @import, spaced `theme=` parameter) were untouched by the landing and remain as recorded. Checker: error 2 / warn 0 / info 0 before and after, finding set identical, class (i) 0.

The regenerated stamp reads `Overall: STALE` against the pre-repair verdict, by design; no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

None for this package: the theme's port, waves, and sweep act are all inside pages/theme:magpie-swoops-jp.txt, and no other canonical file changed for this theme in its wave commits (1869877 and b5cb724 are population commits; their other files belong to other themes' packages).

## Appendix — residue blocks

All 11 residue blocks resolve by shape; none needs a new signature.

- R1 (B3, frame theme= line, orig L9 → cand L14) and R2 (B5, orig L14 → cand L19): the head frames' theme= parameters repointed from cdn.scpwiki.com to scp-jp.github.io — section 3, the frame half of the P4/T9 delivery repoint (the module lines carry the DELIVERY-HOST signature; the parameter lines carry none).
- R3 (B26, orig L108 → cand L116): the "++ Examples" heading translated to 「++ 使用例」 — section 6, P10.
- R4 (B85, orig L302 whitespace line): whitespace-only inside the exhibit — section 9.
- R5–R11 (B86–B88, B118, B120, B126 and companions): CSS section-comment translations inside the exhibit (===Purples===, ===Greens=== → 緑, ===Black=== → 黒, ===TABLES=== → 表, ===TOC=== → 目次, SELECTION COLOUR → 選択範囲色) — section 6, the R1 comment half of P10; R5's comment additionally joins its rule line in the candidate, a line-join inside the same act.

## License and attribution

- **Title:** Magpie Swoops Theme
- **Author:** Sinking_Otter
- **Source:** https://scp-wiki.wikidot.com/theme:magpie-swoops — revision 12
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
