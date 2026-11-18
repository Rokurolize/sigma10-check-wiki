# Review package — theme:just-girly-things-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:just-girly-things-jp — origin EN, population #19 [GOSIGN2-LEDGER (b) row 19]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0efcc6cebc542e4d17a481203ec88cdb55ca5a63bd9d3029aa0d01c4e2408a16); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 19; GOSIGN2-LEDGER (b) row 19]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 page incomplete (exit 2→exit 1 baseline, no summary), sample credit-modal + 768px overflow 884px + cdn.jsdelivr.net/fonts.bunny.net direct links. [RENDER-ROWS-1 (RENDER-B row 19)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-B row 19)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 20, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 20]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 19]
- Computed against: canonical commit 1e34c0b668faf170da8af14c127251af3e35fa26; candidate file pages/theme:just-girly-things-jp.txt sha256:0efcc6cebc542e4d17a481203ec88cdb55ca5a63bd9d3029aa0d01c4e2408a16; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/just-girly-things-jp/candidate.txt (sha256 da9fe442f0255d016344965687c10c8a5096caf14a5c913521b7e621db9c6d8b)
Original: theme:just-girly-things — scp-wiki, revision 21 (sha256 e295cac7fe7c198bc1216ffd171b173b7e0244961cc6f4a044bf1e4fe8caca16)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 19); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme, the supplement carries no just-girly-things entries, and no FIX5 re-judgement was needed |
| Wave edits after creation | The credit block in two steps (b816e10: six fields; 5c32672: the translator pair), then one commit (1869877, FIX-CREDIT-D) carrying the attribution normalization, the pattern-2 font-host repair, the JP font load and stacks, and the interwiki-style frame |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 at baseline (the bunny line has since been repaired; the two wdfiles asset lines stand, class (ii), section 11); render items: T2 coverage caveat, sample credit-modal (preview form), 884px@768 overflow (ledger (c2)); T4 P4 asset half and P5 (ledger (c3)) |
| Flagged in this package | The original's license-box entries (orig L399–411) were dropped at creation and never restored, although the LOCALIZE row charged the drop inside pattern 3 and the ledger closed P3 as FIXED at field level (section 1, per-theme record). The original's demonstration body (orig L10–45) was likewise dropped at creation with no ledger row naming it (section 8) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:just-girly-things | theme:just-girly-things-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 21 (created 2023-09-27 01:58:40 per the fetch record), as recorded in the candidate's credit block: **初訳時参照リビジョン:** 21 | — |
| Source of this copy | Wikidot fetch of 2026-11-17 at the reference revision, via the campaign mirror store (class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:just-girly-things-jp.txt`, created in commit b0cfebd (eight standalone JP theme ports); its last content change is commit 1869877 (FIX-CREDIT-D) |
| Lines / bytes | 412 lines / 9,723 bytes (line count as the generator counts it in diff.md) | 383 lines / 9,540 bytes |
| SHA-256 | e295cac7fe7c198bc1216ffd171b173b7e0244961cc6f4a044bf1e4fe8caca16 | da9fe442f0255d016344965687c10c8a5096caf14a5c913521b7e621db9c6d8b |

Wave history: the candidate was created in b0cfebd with its delivery already restructured (the original's code-exhibit CSS inlined into the head module), the demonstration body and license box dropped, and the Lobster import moved to fonts.bunny.net. Commit 3010ef7 normalized trailing whitespace (22 lines); 8dcac74 recorded the reference revision in the tail prose; b816e10 (T1 fixes, rows 1–44) added the credit block with six fields; 5c32672 (FIX-CREDIT-C) completed the translator pair; 1869877 (FIX-CREDIT-D) is the file's last content change and did five things at once (per-theme record).

## Summary

A small, self-contained EN theme whose port is one creation decision plus a credit-wave tail. The creation inlined the original's 351-line code-exhibit CSS into a live head module (topology similarity 0.987), dropped the EN demonstration body and the license box, and substituted a bunny.net font import for the original's Google Fonts import. The waves then built the credit furniture in three steps and, inside the FIX-CREDIT-D commit, repaired the font host to the original's own Google Fonts URL, added the Noto Sans JP load and stacks, and added the interwiki-style frame the creation had omitted. Measured churn (diff.md, the generator's difflib count with autojunk off: +35/−64 in 8 classifier change blocks, 5 diff hunks; a GNU-diff count of the same pair gives the identical +35/−64). Two items deserve a reviewer's eye rather than a skim: the license-box attribution for the theme's two images never came back (section 1), and girly's ledger (c3) line credits none of the frame/font work its bytes contain (per-theme record).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 8 change blocks — 7 specific (87.5%), 1 heuristic (12.5%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DELIVERY-MOVE | 6 |
| DUPIMPORT-DEL | 1 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONT-IMPORT | 2 |
| IFTAGS | 2 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 2 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| WS-ONLY | 1 |

Adjudication for this README (every block was read against the bytes, and the sections below are written from classification.json's label_spans, not from the skeleton's primary labels — the skeleton's sections 1, 2, 4, 6, and 7 print "none" although their signatures fired inside multi-label blocks): the six DELIVERY-MOVE blocks are one act, the creation's relocation of the CSS body from the code exhibit into the head module, not six decisions. The three EXHIBIT-RESTRUCTURE primaries split three ways: B2 is the head/body zone (frame drop plus demonstration-body drop), B7 is an alignment merge of two different acts in two different commits (the license box's departure at creation, the frame's arrival in 1869877), and B8 is the credit zone, where the label rides the furniture swap. The DUPIMPORT-DEL label on orig L47–48 is the in-exhibit Lobster @import disappearing with its exhibit; the import was not duplicated in the original, it relocated to the head module with the body (and changed host twice on the way, section 4). The one heuristic block (B7) is resolved in the Appendix.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:just-girly-things-jp; original theme:just-girly-things on scp-wiki at reference revision 21; candidate `pages/theme:just-girly-things-jp.txt`. Provenance route: derived from the original at the reference revision by the standalone-ports commit b0cfebd. No production JP counterpart is recorded for this theme in review/sources.tsv, and the candidate's CSS body matches the original's code exhibit at 0.987 similarity, so the R4 adoption question does not arise: the body is the original's, relocated, not a production page's.
- **Why:** Section 0 declares the route so the delivery restructure in section 3 is read as a relocation of the original's own body, not as new content.
- **Verify:** The sources.tsv row for just-girly-things-jp; `sha256sum original.txt` against the Provenance table; classification.json's topology move (code-css → module-css, similarity 0.987).
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is threefold: an info pane (`[[include info:start]]` … `info:end]]`, orig L20–22, placeholder text), a bare Rate exhibit (orig L12–13, inside the demonstration body), and a license box (orig L399–411, treated at the end of this section). The candidate replaces the first two with the JP preview credit block (cand L361–370) carrying the eight ruling-3 fields: タイトル Just Girly Things Theme（SCP-JP）; 翻訳責任者 AI; 翻訳年 2026; 原題 Just Girly Things Theme; 著作権者 stormbreath; 作成年 2020; 初訳時参照リビジョン 21; 元記事リンク (host-verified in section 7). The block was built in three steps: b816e10 added six fields (all but the translator pair), 5c32672 (FIX-CREDIT-C) added 翻訳責任者 as "SCP-JP" plus 翻訳年, and 1869877 normalized the translator field to AI under ruling 3. The author field names stormbreath, matching the original's banner ("Created by stormbreath, aesthetic consultation from DianaBerry", orig L53), and the banner itself is carried verbatim inside the moved CSS (cand L7–13), so the DianaBerry consultation line and the "Logo Image by CalibriBold" line survive in the file. The bare Rate is deleted, not kept beside the block: the candidate contains no `[[module Rate]]`, and the preview credit module is rate-bearing, so no KB-09 duplication arises. The license box is the exception to this tidy picture: its two per-file entries (JGTLOGONEW.png — author "Calibold" in the box, against the banner's "CalibriBold", an original-side spelling split; tablecloth.png — Pixaline, Public domain, with the Pixabay source link, orig L401–409) have no counterpart anywhere in the candidate, and no JP license box exists in the file. The LOCALIZE row charged exactly this ("license attribution dropped") inside pattern 3; the credit waves completed the §3 fields (checker-verified: credit-missing-fields = 0 population-wide at ledger assembly) and the ledger §(c3) line closes P3 as FIXED. The closure is true at field level and incomplete at license level; the drop is **flagged** in the per-theme record rather than repeated as fixed here.
- **Why:** P3/T1 for the furniture swap (the preview module is rate-bearing, so the bare Rate goes, KB-09); ruling 3 for the eight fields and the translator form; T4/KB-63 for the license box (a dropped license box is a defect shape, not a supplement choice).
- **Verify:** Read cand L361–370 against the eight fields; `grep -n 'module Rate' candidate.txt` returns nothing; `grep -n 'license-box' candidate.txt` returns nothing, against orig L399–411; `git show b816e10`, `git show 5c32672`, `git show 1869877` on the candidate file reproduce the three build steps.
- **Disposition:** Field completion FIXED (credit waves). License-box entries **flagged** (per-theme record).

### 2. Includes and components

- **What:** The candidate carries three live includes, all `:scp-jp:`: the interwiki-style frame (cand L356) and the credit pair (cand L361, L370); a fourth include form appears as the usage line inside `@@` (cand L376, the candidate's own bare same-site form). The original's include set is larger: the EN frame (orig L5–8), the info pair (orig L20, L22), the usage line (orig L26, `:scp-wiki:` form), an image-block sample (orig L28, inside the dropped body), and the license-box pair (orig L399, L411). No foreign include survives in the candidate, so KB-15 does not arise; no T8 component swap exists in this file — the classifier's COMPONENT-SWAP span (orig L410–411 → cand L375–376) is an alignment pairing of the license-box end with the candidate's usage prose, not a swap. Ruling 4 is satisfied trivially: the theme needs no component port (its one component-shaped dependency, image-block, was a documentation sample, and the frame and credit modules are population furniture).
- **Why:** P1 (KB-15) for include targets; the license-box pair's absence is section 1's flag, recorded there rather than double-counted here.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three live includes plus the usage line, all JP-side; compare orig L5–411's include list above.
- **Disposition:** Applied (repoints and furniture); license-box absence flagged in section 1.

### 3. Delivery and code loading

- **What:** The original delivers its CSS from a `[[code]]` exhibit (orig L47–397): the head module imports the page's own local--code /1 (orig L2) and the EN frame's `theme=` names the same URL (orig L7) — the classifier's two SELF-DELIVERY spans, both original-side only. The candidate delivers from a live head module instead: the whole CSS body sits inside `[[module CSS]]` (cand L1–354), the topology pass measures the relocation code-css → module-css at 0.987 similarity, and both self-delivery lines are deleted as unnecessary — a module needs no import of itself, and the candidate contains no `local--code` reference at all, so the draft-host class (iii) never arises for this theme. The frame's history is two-stage: the creation dropped the original's frame outright (the created file has no frame include), and 1869877 added the JP frame (cand L356–358) with `priority=1` and no `theme=`/`css=` parameters — the correct KB-07 form for a module-delivered theme, since there is no separate stylesheet URL for the frame to name. DELIVERY-HOST (B1) is the head-module zone where the import line's host change rides the move.
- **Why:** P4/T9 for delivery source (own-wiki delivery; here the strongest form, no external delivery at all); P6/T3 with KB-07 for the frame and its surviving parameters. The restructure itself is the porter's creation decision; every later wave preserved it, and the T2/T3 record was measured against this form.
- **Verify:** `grep -n 'local--code' candidate.txt` returns nothing; classification.json's topology (candidate components: one module-css block, L1–354); `git show b0cfebd` shows the created file already in module form with no frame; `git show 1869877` shows the frame arriving.
- **Disposition:** Standing (the relocation and the frame's final form). The frame's absence between creation and 1869877 is history, recorded here; no ledger row charges it, because the render checks ran after the frame landed.

### 4. Fonts and assets

- **What:** Fonts, three acts. (1) The original loads Lobster from Google Fonts inside its code exhibit (orig L48). (2) The creation substituted fonts.bunny.net for the same Lobster import in the head module — the candidate state the LOCALIZE lane charged as pattern 4 ("bunny.net live font import L2", this theme's one display-affecting T4 finding) and the render row echoed as a bunny.net direct link. (3) Commit 1869877 repointed the import to fonts.googleapis.com (cand L2) — the pattern-2 fix, which the ledger's (c1) preamble credits as FIXED where named, this theme named — and in the same hunk added the JP supplement: the Noto Sans JP import (cand L3, wght 400;700), the body font rule (cand L5), and 'Noto Sans JP' inserted into the two Lobster stacks (cand L52, L64; classifier JPFONT-STACK B3/B4 — the skeleton's section 4 prints "none" only because both spans ride inside DELIVERY-MOVE primaries). Every face a stack names is loaded: Lobster (cand L2), Noto Sans JP (cand L3); verdana and arial are system faces. No @font-face exists on either side. Assets: the theme's two images stay on the original's own host, scp-wiki.wdfiles.com `local--files` with the colon percent-encoded (cand L25 tablecloth.png, cand L41 JGTLOGONEW.png; KB-01 form). These two lines, with the since-repaired bunny line, are the T1 baseline's hotlink ×3. Girly's ledger §(c3) line records "P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery)" and "P5 DISPOSITIONED (class (ii) / KB-58)": those dispositions describe the asset lines correctly, but they do not describe the font import, which was fixed, not dispositioned — the split is recorded here and in the per-theme record.
- **Why:** P5's host rule (only storage, Google Fonts, BootstrapCDN, and cdnjs may be hotlinked; bunny.net is not on the list, which is why the substitution needed repair rather than a disposition); pattern 2 is the campaign's name for that repair. P7/T5 with KB-16 for the JP supplement (a stack naming an unloaded face falls back silently — the failure the supplement prevents). KB-17/KB-58 for the asset lines (the original's own asset host kept as original state; re-hosting is the posting act and re-upload is barred by owner order).
- **Verify:** `grep -oE 'https?://[a-zA-Z0-9.-]+' candidate.txt | sort | uniq -c` — googleapis ×2, scp-wiki.wdfiles.com ×2, scp-wiki.wikidot.com ×2 (the credit links, section 7), pixabay ×1 (the banner comment, porter-visible only); `git show b0cfebd` shows the bunny line at creation; `git show 1869877` shows its repair.
- **Disposition:** Font-host repair FIXED (1869877, pattern 2). JP font supplement FIXED (same commit; girly's (c3) line does not credit a P7 fix — the bytes carry it, recorded as a discrepancy in the per-theme record). Asset lines DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, site furniture

- **What:** No P8 layout adaptation and no P9/T6 header-variable supplement: the candidate declares no `--header-title`, `--header-subtitle`, or `--logo-image` (grep count 0). The wordmark and subtitle are CSS `content:` strings carried inside the moved body in the original's English ("Just Girly Things!", cand L51; "By Girls, for Girls", cand L61) — the theme's own title text, not masthead variables, and this theme's rows carry no P9 charge, so no ruling-2 disposition was needed. The mobile `.open-menu` rule (orig L391–395 zone) is carried inside the moved body as unchanged context. The narrow-width render findings are the cross-cutting families of section 11, not furniture changes.
- **Why:** P8/P9 absence stated with its ground, per the standing-section rule that an empty section says why it is empty.
- **Verify:** `grep -c 'header-title\|header-subtitle\|logo-image' candidate.txt` returns 0; read cand L50–65 for the two content strings against orig L94–107.
- **Disposition:** Standing (none, with the ground stated).

### 6. Text translation

- **What:** The candidate's Japanese prose is a short porter-written tail (cand L372–382): a title line, a one-sentence description, the usage line (cand L376, the candidate's own bare include form naming theme:just-girly-things-jp — the post-sweep posting-name form), a credit thanks sentence, the reference-revision record, and the 出典 line. It replaces the original's English body prose, of which the only running text was the usage sentence (orig L24); the rest of the original's body was demonstration exhibits, whose non-carriage is section 8's subject, not a translation gap. The CSS banner comment stays in English (orig L50–56 → cand L7–13, verbatim): porter-visible only, the R1 comment half, which the campaign's NEGATIVE-LEDGER records as a known non-finding. No R5 glyph-form conversion arises (English source). TRANS-UNANCHORED (B8) is the credit-zone/prose translation mass.
- **Why:** P10 for the carried prose; R1's comment half is stated separately from reader-visible text, as the taxonomy requires.
- **Verify:** Read cand L372–382 against orig L24; `grep -n 'Just Girly Things Redux' candidate.txt` returns the banner at cand L8.
- **Disposition:** Standing for the carried prose; the exhibit body is section 8's flagged item.

### 7. Links

- **What:** The candidate's live outbound links are the credit block's source link (cand L369) and the 出典 line (cand L382), both `https://scp-wiki.wikidot.com/theme:just-girly-things` — the original's recorded host in review/sources.tsv, so the dead-host defect class does not arise and no probe was needed. The original's in-body link sample (`[[[theme:just-girly-things|Visited Link]]]`, orig L32) sat inside the dropped demonstration body. The Pixabay source link survives only inside the banner comment's header-image credit line (cand L11); its formal license-entry form (orig L409) is part of section 1's license flag.
- **Why:** P11, under the dead-reference evidence standard (a link is charged only on probe evidence; here the host matches the recorded original host, so there is nothing to charge).
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — exactly the two lines above.
- **Disposition:** Standing; no dead reference found in this file.

### 8. Structure

- **What:** For everything the candidate carries, the localize.md closing rule holds: the CSS body's variable names, selectors, and order are preserved through the relocation (0.987 body similarity; the move is channel-only), and the JP supplements arrive at the edges (head imports, tail frame and credit zone). Two structural drops stand, both at creation and neither named in any ledger row. (a) The demonstration body (orig L10–45): the Rate exhibit, the info pane, the usage line, the image-block sample, and the header/link/table/tabview samples are all absent from the candidate, replaced by the short JP prose tail (cand L372–382). The samples are wikitext demonstrations with no CSS payload, but the drop is unrecorded, so from the record alone it is indistinguishable from a silent deletion — **flagged**. (b) The license box (orig L399–411): section 1's flag (KB-63 shape). The classifier's EXHIBIT-RESTRUCTURE primaries adjudicate as: B2, the head/body zone (frame drop plus body drop); B7, an alignment merge of the license box's departure (creation) with the frame's arrival (1869877) — two acts, two commits, one block; B8, the credit zone, where the label rides the furniture swap of section 1. The bare-Rate exhibit's reasoning, which the skeleton's slot asks for explicitly: removed with the body, and correctly so, because the preview credit module that replaced the info pane is rate-bearing (KB-09) — a kept bare Rate beside it would be the duplicate the campaign charges elsewhere (ledger class B).
- **Why:** R3 exists because a sanctioned replacement and a silent deletion share a diff shape, and ledger class I charges the silent form when it reaches live structure. Here the census is unambiguous (exhibits present in the original, absent in the candidate), so the package states the census and flags the missing record instead of inventing a sanction.
- **Verify:** `grep -n 'tabview\|image-block\|module Rate' original.txt candidate.txt` — the original shows all three in its body; the candidate shows none (its one image-block hit is a CSS selector, cand L301).
- **Disposition:** **Flagged** (both drops, with the census above); the carried structure is standing.

### 9. Formatting only

- **What:** One WS-ONLY block (B5, a whitespace-only line pair inside the moved body, orig L237–238 → cand L194–195), plus one formatting commit in the history: 3010ef7 normalized trailing whitespace on 22 lines immediately after creation. No re-indentation (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is limited to the trailing-whitespace pass, which is recorded here so it is not mistaken for content churn.
- **Why:** R7 disclosure: formatting churn is stated as its own class.
- **Verify:** classification.json's label counts (WS-ONLY 1); `git show 3010ef7 --stat` on the candidate file (22 insertions, 22 deletions, whitespace only).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None in annotation form. The candidate carries no `[!-- --]` translator notes and no editor lines; the JP tail prose (cand L372–382) is page prose, counted in section 6, not annotation. The ANNOTATION signature did not fire, and a direct scan agrees.
- **Why:** R2: porter-added text is part of the change record; here the record is that there is none in annotation form.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (none, with the ground stated).

### 11. Dispositions and exceptions

- **What:** Three dispositioned groups, each with its ground. (1) The two wdfiles asset lines (cand L25, L41): class (ii) / KB-58 — the original's own asset host kept as original state; their remedy is the posting-time re-hosting act, and re-upload is barred by owner order. This is also the asset half of the ledger §(c3) line's P4/P5 dispositions. (2) The render row's items (RENDER-ROWS-1, RENDER-B row 19): the T2 page run was incomplete (exit 2→exit 1 baseline, no summary) — a coverage caveat, not a theme defect (ledger register (a)); the sample credit-modal is the preview-form property (credit:start-preview has no modal mechanism; ruling 5's form, KB-32); the 884px@768 sample overflow is the static credit replica's fixed width (KB-33), a cross-cutting shape whose per-theme figure matches the campaign-wide one. (3) T4's P4/P5 dispositions as recorded in §(c3), with the font-import correction of section 4: the disposition language covers the asset lines, not the repaired import. The license entries and the demonstration body are deliberately not in this list: they are flagged (sections 1 and 8), because a disposition must rest on grounds a reviewer can re-derive, and no record supplies grounds for those two drops.
- **Why:** AGENTS.md §3 classes and the named KB entries, as cited per item.
- **Verify:** Each item names its deciding record; the asset lines are enumerable by the host grep in section 4.
- **Disposition:** DISPOSITIONED (items 1–3); two items flagged separately.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 19): exit 1, 3 errors / 1 warn / 1 info — hotlink ×3 at the 2026-11-16 baseline (the bunny import plus the two wdfiles asset lines); the bunny line has since been repaired (section 4) and the asset lines are dispositioned (section 11); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, RENDER-B row 19): FINDINGS — the coverage caveat and the two cross-cutting items of section 11; engine coverage as run by the lane, with the row's inconclusive runs carried verbatim in the stamp. (c) T4/T5 (LOCALIZE-ROWS row 20): FINDINGS jointly, display-affecting findings 1 (the bunny import); the ledger §(c3) line closes P3 FIXED, P4 DISPOSITIONED, P5 DISPOSITIONED — with the corrections this package records: the P3 closure is field-level only (section 1), and the P6 frame and P7 font supplement stand in the bytes via 1869877 although the (c3) line credits neither (per-theme record). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +35/−64 in 8 change blocks; the GNU-diff count is identical (+35/−64).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:just-girly-things-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 19; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### One commit, five acts (1869877)

FIX-CREDIT-D's subject names one act — "translator attribution normalization over all candidates" — and for this file that act is real (翻訳責任者 SCP-JP → AI). But the same commit's girly hunk also repointed the Lobster import from fonts.bunny.net to fonts.googleapis.com (the pattern-2 repair the LOCALIZE row's pattern-4 charge demanded), added the Noto Sans JP import and the body font rule, inserted 'Noto Sans JP' into both Lobster stacks, and added the interwiki-style frame the creation had omitted. A reviewer reading only the commit subject, or only girly's ledger §(c3) line (which credits P3 FIXED and dispositions P4/P5, mentioning neither P6 nor P7), would conclude the frame and the font supplement never landed on this theme. The bytes say otherwise, and this package cites the commit for each act separately for that reason. The same understatement shape appears in this batch's other files and in U-1/U-2 before it: wave commit subjects name the wave's theme, not its full contents.

### The license entries (pattern 3's second half)

The LOCALIZE row's pattern-3 charge has two halves: "§3 fields mostly missing" and "license attribution dropped". The credit waves closed the first half verifiably (the eight fields stand at cand L362–369; the checker's credit-missing-fields count is 0 population-wide). The second half was never acted on: the original's license box (orig L399–411) credited the logo image to the box's "Calibold" (the banner's spelling is "CalibriBold", orig L55 — the original disagrees with itself, and the candidate's carried banner keeps "CalibriBold", cand L12) and the tablecloth image to Pixaline under Public domain with its Pixabay source. No JP license box (license-box-backend/end) exists in the candidate, so the Pixaline attribution and both formal license entries are simply absent. This package flags the item for the coordinator with the remedy form the campaign uses elsewhere: a JP license box carrying the two entries, placed where the original's box stood (after the CSS, in the gated zone). The PASS determination is the ledger's and is not re-opened here; the flag is about the record's completeness, in the same shape as the aces-and-eights holder-field flag in batch U-1.

### Post-package repairs (REFRESH3-G)

- **FIX-U7, landing `1e34c0b668faf170da8af14c127251af3e35fa26`** ("pages: U-7 repairs …", 2026-11-17, R/review-scout/FIX-U7.md item 4): the JP license box created at the candidate's tail inside its +テーマ gate — `component:license-box-backend` with `|author=stormbreath` (refreshed candidate L384–385), two per-file entries (JGTLOGONEW.png / `[[*user Calibold]]` / CC BY-SA 3.0 at L387–389; tablecloth.png / 名前 tablecloth-greeting-solemnly / Pixaline / Public domain / Pixabay source at L391–395), closed by `component:license-box-end` at L397, +16 lines. The original's box (orig L399–411) carried both entries; the drop was never charged. The "The license entries (pattern 3's second half)" subsection above is the as-built record that flagged the absent box; the box is now present in the recopied candidate. The banner's "CalibriBold" at cand L12 remains the original's own inconsistency and was not propagated into the license entry. Checker: error 2 / warn 0 / info 1 before and after, finding set identical, class (i) 0.

The regenerated stamp reads `Overall: STALE` against the pre-repair verdict, by design; no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-just-girly-things-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11, item 2); it belongs to this theme's record but carries no port change of its own to explain here. The original side's local--code /1 fragment was the code exhibit itself (section 3); the candidate has no delivery companion, because its CSS is a live module. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## Appendix — residue blocks

The classifier emitted no residue blocks for this pair. The one heuristic block is resolved here:

- **R1 — B7 (heuristic; orig L398–403 → cand L355–358, body → body).** The alignment pairs the license box's opening lines with the candidate's frame include, because both sit between the CSS body and the gated tail. Resolved as two separate acts in two sections: the license box's departure is section 1's flag (creation, b0cfebd), and the frame's arrival is section 3 (1869877). The classifier's note ("no translated counterpart on the added side; the writer's replaced-vs-dropped call is forced") is answered: neither replaced nor dropped — the two sides of this block belong to different changes that happen to share a boundary.

## License and attribution

- **Title:** Just Girly Things Theme
- **Author:** stormbreath
- **Source:** https://scp-wiki.wikidot.com/theme:just-girly-things — revision 21 (revision date 2023-09-27 01:58:40)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
