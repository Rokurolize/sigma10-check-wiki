# Review package — theme:admo-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:admo-jp — origin EN, population #52 [GOSIGN2-LEDGER (b) row 52]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 52]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 12 errors / 1 warn / 1 info (hotlink×9, pseudo-ref×2, http×1); standing classes dispositioned in register c1 [T1-ROWS row 52; GOSIGN2-LEDGER (b) row 52]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent page-overflow 454–470px@320/375 (page) and 399–412px (sample), fixed-width layout; contrast 1.1 credit ghost by design. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 52, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 52]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 52]
- Computed against: canonical commit a497307c6e7eedc2580739ba55d2c3212d9cacd2; candidate file pages/theme:admo-jp.txt sha256:3b6c29e32ca7b21e05d901a31d01dfb490c7a9fb78b74dac9707c8d976f1dc5f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 52) |
| Wave history | Four commits touch the candidate, and this theme's class-U story is its delivery: creation with the base inlined (3205f27), a rework that restored the EN CDN base delivery (95fd1d1), the FIX2 wave that repointed the base to the JP candidate and carried the frame, font, and translator fixes with it (f931619), and a FIX4 dedupe (a497307). Each is narrated in section 3 and the per-theme record |
| Standing items | **DISPOSITIONED** — T1 hotlink ×9 and http ×1 (class (ii) family, section 11); the fixed-width page overflow (by-design, KB-37 family); the credit ghost contrast (KB-39). Two items are **flagged**, not dispositioned by this package: the dropped co-author name in the holder field, and the un-restored display-font imports (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:admo | theme:admo-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 66 (first translation; the candidate's credit block records 初訳時参照リビジョン: 66) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-admo.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:admo-jp.txt`, copied at worktree HEAD 1605bbd; the file's last content change is commit a497307 (FIX4-MECH) |
| Lines / bytes | 692 lines / 16,886 bytes | 618 lines / 15,666 bytes |
| SHA-256 | 79bbfede2636ce9bba9cab8801a73b3f479c087000fcfe959c9621bf957f7f88 | 3b6c29e32ca7b21e05d901a31d01dfb490c7a9fb78b74dac9707c8d976f1dc5f |

review/sources.tsv classifies this row K5b-3: the candidate's delivery references another population candidate's delivery (theme:basalt-jp). That reference is the theme's whole wave story, told in section 3.

## Summary

ADMO is a Basalt-based theme: the original loads Basalt through a hidden include with parameters, frames the base's two CDN stylesheets with two interwiki-style includes, presents its full CSS in an ungated module, and closes with a gated documentation body (a centered bare Rate, usage exhibits, an "+ Info" section, an "+ Astral Variant" section, and the end-card markup exhibit). The candidate wraps its content in a single gate (credit block, compressed prose, and the CSS module) and does not carry the documentation body's exhibits and sections (section 8); it swaps the credit furniture for the JP preview block, and delivers its base the way the campaign's ruling 1 requires — except that it arrived there in three steps, not one: the creation inlined the base and said so; a rework (rework2-p1) put the EN CDN delivery back, in the original's own form; FIX2-COLON then replaced the CDN imports with the JP base candidate's delivery and, in the same commit, added the frame, the JP font import, the translator normalization, and a run of URL colon-encodings; FIX4-MECH removed a duplicated base import the FIX2 edit had written twice. Measured churn (diff.md, the generator's difflib count with autojunk off: +36/−110 in 19 classifier change blocks; a GNU-diff count gives +35/−109). The small net is deceptive: most of the CSS body is unchanged context, and the real change mass is the head delivery, the credit zone, the colon-encodings, and the dropped second body. Two ledger closures do not match the bytes and are flagged rather than repeated: the holder field (per-theme record, item 2) and the font closure's scope (item 3).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 19 change blocks — 15 specific (78.9%), 2 heuristic (10.5%), 2 residue (10.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COLON-ENC | 9 |
| EXHIBIT-RESTRUCTURE | 3 |
| IFTAGS | 3 |
| CSS-BODY | 2 |
| DRAFT-HOST | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the nine COLON-ENC blocks are one act (the FIX2 commit's percent-encoding of colons in this file's `local--files` URLs, section 3), not nine decisions. The two residue blocks are alignment noise at boundaries: B5 pairs an original blank line with the candidate's CSS comment opening, and B18 sits on the closing `[[/module]]` boundary; neither carries content, and both are stated here so the residue count is not mistaken for unexplained change. The two heuristic blocks are B6 (the original's three fonts.bunny.net imports, deleted and never restored in this file — section 4) and B8 (the `--header-font-primary` stack line, the P7 stack supplement). The three EXHIBIT-RESTRUCTURE primaries are the head delivery zone (B1), the credit zone (B3/B4 area), and B19, which is a genuine content drop adjudicated in section 8 — the one place in this batch where the label means what it says.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:admo-jp; original theme:admo on scp-wiki at reference revision 66; candidate `pages/theme:admo-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch (commit 3205f27); no production JP counterpart exists, so the R4 question does not arise. The frame order differs from the batch's other themes: the candidate opens with a head `[[module css]]` (candidate L1–4) carrying the font import and the base delivery, then the interwiki-style frame (L6–9), then the gate (L11) — because the base delivery is a stylesheet @import, it rides in a module, not in the frame's `theme=` slot. sources.tsv kind K5b-3 records the cross-candidate delivery reference.
- **Why:** Section 0 declares the route and the K5b-3 shape so the delivery sections are read against the right baseline; the gate's tag is P2.
- **Verify:** The sources.tsv row for admo-jp; `sha256sum original.txt` against the Provenance table; read candidate L1–11.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside its gated body, plus the CSS header comment "Admonition Theme by Liryn & Placeholder McD" (original L17–20; the by-line is L20). The candidate deletes the Rate (block B10's zone) and installs the JP preview credit block (candidate L13–22) with the eight ruling-3 fields (title ADMONITIONテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 ADMONITION Theme; 著作権者 Liryn; 作成年 2021; 初訳時参照リビジョン 66; the source link, host-verified in section 7). The translator field took its ruling-3 form inside f931619 (FIX2-COLON) — this file has no credit-wave commit at all. The header comment is carried (candidate L32–34, "by Liryn & Placeholder McD"), so McD's name survives in the candidate — in the comment, not in the credit block. The LOCALIZE row charged the gap (pattern 3: 著作権者から Placeholder McD 欠落）, and the ledger §(c3) line closes the row's P3 as "FIXED (credit waves)". Both halves of that closure miss the bytes: no credit-wave commit touched this file, and the holder field still names Liryn alone. The discrepancy is flagged in the per-theme record (item 2); this package does not re-open the PASS determination and does not repeat the FIXED claim for the holder field.
- **Why:** P3/T1 (the preview credit module is rate-bearing, so the bare Rate is deleted, KB-09); ruling 3 fixes the eight fields and the translator form. As with theme:aces-and-eights-jp in this batch, the checker-verifiable part of P3 is the fields' presence and form; a holder-content addition is a different act, and no commit performs it.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; `grep -n 'Placeholder' candidate.txt` returns exactly one hit, candidate L34, inside the CSS comment; read candidate L13–22 against the eight fields.
- **Disposition:** The block swap is FIXED (creation) and the translator field FIXED (inside f931619). The holder-field item is **flagged** with evidence in the per-theme record. No license box exists on either side, so the T4/KB-63 question does not arise. This theme has no T7 credit-CSS supplement; the FIX2-era credit rules in its CSS are the theme's own, not a supplement.

### 2. Includes and components

- **What:** Candidate includes: the frame (candidate L6) and the credit pair (L13/L22), and no others. The original's include set is larger: a hidden-div include of `:scp-wiki:theme:basalt` with display parameters (original L1–3) that loads the base, and two EN interwiki-style includes at priorities 1 and 2 (original L5–13) naming Basalt's normalize and bedrock CDN stylesheets. All three are gone as includes: the base arrives by @import (section 3), and the frame collapses to the campaign's single priority-1 form naming the candidate's own delivery. The classifier's COMPONENT-SWAP block (B2) is the hidden-div include's removal zone. No foreign include survives; ruling 4 is satisfied in its delivery form — the needed base is ported (theme:basalt-jp is itself a population candidate) and referenced, not skipped.
- **Why:** P1 (KB-15) for include targets; ruling 1 for the base reference (a dependent theme imports the base theme's JP port candidate delivery, never the raw upstream delivery — the rule this file violated in its middle state and satisfies in its final one).
- **Verify:** `grep -n '\[\[include' candidate.txt` — three includes, all `:scp-jp:`; compare original L1–13.
- **Disposition:** Applied in the final state; the intermediate EN-CDN state is history, narrated in section 3.

### 3. Delivery and code loading

- **What:** Four states, one per commit. (1) Creation (3205f27): the base inlined — the candidate's prose declared **基盤:** Basalt（インライン） and no base delivery line existed. (2) rework2-p1 (95fd1d1, +6/−1): a head `[[module css]]` appeared importing the EN Basalt verbatim from cdn.scpwiki.com (`normalize-min.css` and `basalt-bedrock-min.css`), and the prose was rewritten to declare exactly that — the original's own delivery form, restored after the inlining dropped it. This is the state the LOCALIZE row charged (pattern 4: EN Basalt CDN delivery used verbatim). (3) FIX2-COLON (f931619, +20/−14): the CDN imports were replaced by the JP base candidate's delivery, `@import` of `theme%3Abasalt-jp/1` on the draft host (written twice in that commit, candidate L3 today carries it once); the same commit added the Noto Sans JP @import (candidate L2), the interwiki-style frame (L6–9, priority 1, `theme=` naming the candidate's own draft-host delivery), the translator normalization, the 基盤 prose rewrite to its current form (candidate L28: the head module imports the JP base candidate), the `"Noto Sans JP"` addition to `--header-font-primary` (candidate L54), and the percent-encoding of colons in nine `local--files` URL lines (the classifier's COLON-ENC ×9: `theme:admo` → `theme%3Aadmo`, `sigma:basalt` → `sigma%3Abasalt`, `theme:basalt` → `theme%3Abasalt`). (4) FIX4-MECH (a497307, −1): one of the two duplicated basalt-jp @import lines removed — the KB-65 duplicate-delivery defect, caught and repaired inside the campaign. The candidate's own CSS also delivers from the frame's `theme=` URL (its own draft-host /1), the standard self-delivery.
- **Why:** Ruling 1 is the deciding rule for states 2→3: cross-theme imports repoint to the JP fixed base candidate; the EN CDN form is the raw upstream delivery and cannot stand. P4/T9 and P6/T3 govern the frame; KB-01 is the colon-encoding signature (a literal colon in a `local--files` path segment breaks the file URL); KB-65 is the duplicate-import signature. The draft-host URLs (candidate L3, L8) are KB-41, class (iii), rewritten to production hosts at posting.
- **Verify:** `git log --oneline -- pages/theme:admo-jp.txt` shows the four commits; `git show` each in turn reproduces the four states above; `grep -n 'basalt' candidate.txt` shows the single surviving base import at L3 and the encoded `sigma%3Abasalt` asset lines.
- **Disposition:** The base delivery stands in its ruling-1 form (JP candidate, draft host, class (iii) for the host). The ledger §(c3) line's P4 wording ("DISPOSITIONED (delivery class (ii): original-state CDN delivery)") describes the charged state; the bytes superseded it — the current file does not import the EN CDN at all. Recorded here so the disposition language is not mistaken for the current state.

### 4. Fonts and assets

- **What:** Fonts, two halves. (a) The JP supplement: candidate L2 adds the Google Fonts Noto Sans JP @import, and candidate L54 adds `"Noto Sans JP"` to the `--header-font-primary` stack (`'Poppins', 'Noto Sans JP'`) — both inside f931619. (b) The original's own font loads: the original imports three display faces from fonts.bunny.net (Poppins 700, Spline Sans, Roboto Condensed; original L26–28, the classifier's heuristic block B6). The candidate carries none of them — they were deleted at creation and no later commit restored them in this file. The stacks still name the faces (`'Poppins'` at candidate L54 and throughout), so the faces fall back unless the base delivery loads them; whether theme:basalt-jp's delivery loads Poppins is outside the two diffed files and is not claimed here either way. The LOCALIZE row charged the deletion as display-affecting (pattern 7: フォント@import削除で3書体フォールバック), and the ledger §(c3) line closes P7 as "FIXED (font wave)". The JP half of that closure is real; the display-face half is not in this file. Flagged in the per-theme record (item 3). Assets: nine image URLs stay on scp-wiki.wikidot.com `local--files` (candidate L47, L458, L590, L594, L598, L602, L606, L610, L614 — the theme's own logo and the memo-logo variables, colon-encoded by FIX2), and these nine lines plus the two draft-host lines are the T1 checker's hotlink ×9 and pseudo-ref ×2. One of the nine is worse than hotlink: candidate L458 loads the logo over plain `http://` from a test wiki (scptestwiki.wikidot.com) — the T1 checker's http ×1, and T12's named instance of the test-wiki CSS-asset defect (KB-42).
- **Why:** P7/T5 with KB-16 for the JP supplement (real, and verified above). For the display faces, the honest statement is the one in What: the charge and the closure are both in the record, and the file satisfies only the JP half. P5 with KB-17/KB-58 for the nine asset lines (posting-procedure re-hosting, class (ii)); the http test-wiki line is the KB-42 signature — its remedy is the same re-hosting act at posting, but its presence in a candidate is a defect shape the campaign names, so it is called out individually rather than folded into the nine.
- **Verify:** `grep -n 'bunny\|Poppins+700\|Spline' candidate.txt` returns nothing; `grep -n 'fonts.googleapis' candidate.txt` returns the L2 import only; `grep -n 'scptestwiki' candidate.txt` returns L458.
- **Disposition:** JP font supplement applied (f931619). The nine asset lines DISPOSITIONED (class (ii) / KB-58), with the L458 http line individually flagged as KB-42's named instance. The display-font item is **flagged** (per-theme record, item 3).

### 5. Header, sidebar, and site furniture

- **What:** The theme is a fixed-width Basalt layout, and the render row's finding is candidate-inherent: page overflow of 454–470px at 320/375 on the theme page (399–412px on the sample), recorded by the render lane itself as by-design for this layout family. The second render item is the credit ghost text at contrast 1.1, likewise by design in the original. The theme's own `:root` header variables (including `--header-title: 'ADMONITION'`, original L38) are carried as designed; the header font stack is section 4's.
- **Why:** The overflow is the fixed-width-layout family (KB-37): a layout that declares fixed widths overflows narrow viewports by construction, and the campaign's disposition is that the port preserves the design rather than redesigning it. The ghost contrast is KB-39 (an original design element whose low contrast is the design).
- **Verify:** The render record is RENDER-ROWS-1 (RENDER-S2-A (EN2)); the layout's fixed widths are in the CSS body (unchanged context in diff.md).
- **Disposition:** DISPOSITIONED (both items, as by-design preservations).

### 6. Text translation

- **What:** The candidate's prose is the compressed intro (candidate L24–28): two sentences naming the theme and its author, the usage line (`[[include theme:admo-jp]]`, candidate L26), and the 基盤 declaration (L28, rewritten twice with the delivery, section 3). The original's gated documentation body carries the fuller prose (its Info section) and the exhibit captions; the translation keeps the substance of the intro and drops the rest with the exhibits, which is section 8's subject. The CSS header comment stays in English (porter-visible only). R5 glyph-form conversion: none (English source). The credit block's fields are section 1's.
- **Why:** P10 for what is translated; the boundary of what was not carried is R3's question, answered in section 8 rather than smoothed over here.
- **Verify:** Read candidate L24–28 against original L635–643 (the gated body's Info prose).
- **Disposition:** Standing for the carried prose; the uncarried body is section 8's flagged item.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L21): `[*https://scp-wiki.wikidot.com/theme:admo ソース]`. Its host is the original's recorded host in review/sources.tsv (scp-wiki.wikidot.com), so the jiha-class defect does not arise and no probe was needed. The original's prose links (its hub and exhibit links) sit in the zones section 8 covers. The CSS file URLs are sections 3 and 4.
- **Why:** P11, under the dead-reference evidence standard.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link plus the section 4 asset lines.
- **Disposition:** Standing; no dead reference found in this file.

### 8. Structure

- **What:** The localize.md closing rule holds for everything the candidate carries: the CSS body's names, selectors, and order are preserved (the body's long unchanged runs are diff.md's context), and every JP correction arrives at the edges or as a declared supplement. One genuine structural drop stands, and it is this theme's R3 item: the original's gated documentation body (original L616–692) is not carried as a body. Its furniture is accounted elsewhere (the centered bare Rate is section 1's swap; the Info prose is section 6's compression), but its exhibits and sections — the usage exhibits, the "+ Info" heading structure, the "+ Astral Variant" section (original L645) with its own include exhibit, the span exhibits, and the `admo-end_card` markup exhibit — have no counterpart in the candidate. The candidate's own gate closes at its L618 with no documentation zone after the CSS; its CSS still carries the `.admo-end_card` rules (candidate L221, L227, L566) for markup it no longer exhibits. The vendored LOCALIZE row's final charge begins "Astral …" and the record truncates there, so the campaign's own charge text for this drop is incomplete in the vendored authorities; the ledger §(c3) line does not name the item at all. This package therefore records the drop with its evidence and flags the record gap, and neither invents a sanction for the drop nor hides it. The classifier's EXHIBIT-RESTRUCTURE primaries B1/B3/B4 are the head and credit zones (delivery and furniture, sections 2–3 and 1); B19 is this drop.
- **Why:** R3 exists because a restructure and a deletion share a diff shape and ledger class I charges the silent form. Here the census is unambiguous: exhibits and sections present in the original (the gated body, ~76 lines) are absent in the candidate, while their CSS survives — the signature of a documentation-body drop, not a relocation.
- **Verify:** `grep -n 'Astral\|admo-end_card' original.txt candidate.txt` — the original shows the section and the markup exhibit; the candidate shows only the CSS rules. Read original L616–692; the candidate has no corresponding zone (its file ends at L618 with the gate close).
- **Disposition:** **Flagged** (the drop and the truncated charge record), with the PASS determination left where the ledger put it.

### 9. Formatting only

- **What:** None classified. The classifier reports no WS-ONLY blocks for this pair: every whitespace-adjacent change rides inside a labeled block (the colon-encodings and the delivery rewrites carry their own signatures). The two residue blocks are adjudicated in the class summary as boundary noise. No re-indentation was found (0 blocks pair up after leading-whitespace normalization), so the R7 hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class; here the honest entry is that there is none standing alone.
- **Verify:** classification.json's label counts (no WS-ONLY entry).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no `[!-- --]` translator notes, no editor lines, and no porter comments; a direct scan for annotation forms returns nothing. The 基盤 prose line (candidate L28) reads like an annotation but is the page's own delivery documentation, counted in sections 3 and 6.
- **Why:** R2: porter-added text is part of the change record; here the record is that there is none.
- **Verify:** `grep -n '\[!--\|訳注\|Edited for\|JP localize' candidate.txt` returns nothing.
- **Disposition:** Standing (none, with the ground stated).

### 11. Dispositions and exceptions

- **What:** Four dispositioned items, each with its ground. (1) T1's nine hotlink errors and the http error's host half: class (ii), posting-procedure re-hosting (section 4); the http line's KB-42 aspect is individually flagged there. (2) The two pseudo-ref errors: the draft-host delivery lines (candidate L3, L8), class (iii) / KB-41. (3) The fixed-width overflow: by-design preservation (KB-37 family). (4) The credit ghost contrast 1.1: by-design (KB-39). The holder-field and display-font items are not in this list: they are flagged in the per-theme record, because a disposition must rest on grounds a reviewer can re-derive from the record, and for those two the record's closure language and the bytes disagree.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above; the T1 lines are enumerable by the greps in sections 3 and 4.
- **Disposition:** DISPOSITIONED (items 1–4); two items flagged separately.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 52): exit 1, 12 errors / 1 warn / 1 info — hotlink ×9, pseudo-ref ×2, http ×1, all accounted in sections 3, 4, and 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN2)): FINDINGS, the two by-design items of section 5, both dispositioned; engine coverage the full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 52): FINDINGS jointly, display-affecting findings 4; the ledger §(c3) line closes P3 FIXED, P4 DISPOSITIONED, P5 DISPOSITIONED, P6 FIXED, P7 FIXED — with the corrections this package records: P3's credit-wave attribution and holder content (section 1), P4's superseded disposition language (section 3), P6's and P7's landing commit being f931619 rather than their named waves, and P7's scope (section 4). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +36/−110 in 19 change blocks; the GNU-diff count is +35/−109, alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:admo-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 52; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The delivery saga, as a timeline

This theme is the batch's clearest case of why class U exists: no single wave's report describes the file. Creation inlined the base (a form no wave report mentions). rework2-p1 restored the EN CDN delivery — the exact form the LOCALIZE row later charged — because the inlining had dropped the base's live delivery. FIX2-COLON, a wave named for URL colon-encoding, performed the ruling-1 repoint to the JP base candidate and, in the same commit, the frame addition the ledger credits to "frame waves", the font supplement it credits to "the font wave", and the translator normalization it credits to "credit waves" (which never otherwise touched this file). FIX4-MECH then removed the duplicate base import FIX2 had written. A reviewer reading only the ledger's §(c3) line would believe four separate waves edited this file in four separate passes; the git history shows two passes after creation, one of which did almost everything. The package cites commits throughout for this reason.

### Item 2 — the holder field and Placeholder McD

LOCALIZE-ROWS row 52 charges: クレジット著作権者から Placeholder McD 欠落 (pattern 3). The original's header comment credits both authors ("by Liryn & Placeholder McD"); the candidate's credit block names Liryn alone (candidate L18), and the only commit that touched the credit block after creation is f931619, whose credit edit is the translator field. The ledger §(c3) closure "P3 FIXED (credit waves)" therefore fails on both its halves for this file: the wave attribution and the holder content. As with theme:aces-and-eights-jp (same batch, same pattern-3 shape, different author relation — there a helper, here a named co-author in the theme's own comment), this package flags the gap with its evidence and leaves the PASS where the ledger put it. The pair suggests the pattern-3 closures across the sweep were verified at the field-form level; a credit-content pass, if the campaign ever runs one, has at least these two files to start from.

### Item 3 — what the font closure covers

The LOCALIZE charge (pattern 7) has two halves in one sentence: the deleted display-font imports (three typefaces falling back) and the missing JP font. f931619 fixed the JP half completely (import plus the header stack). The display half was never restored in this file: the three fonts.bunny.net imports (original L26–28) are absent from every version of the candidate after creation. Whether the theme renders its display faces correctly in the JP environment depends on what theme:basalt-jp's delivery loads, which is outside this package's two files; the campaign record does not argue the point for this theme. The closure "P7 FIXED (font wave)" is therefore accurate for the JP supplement and unevidenced for the display faces, and this package records exactly that split.

## Change set outside the two diffed files

The diff covers two files; the port's record is larger in a way that matters here. `pages/theme:basalt-jp.txt` is the base candidate this file's delivery imports (candidate L3) — the K5b-3 reference; its own package carries its own record. `pages/theme-decoration-sample-admo-jp.txt` is the decoration sample the render checks ran against (the render row's page/sample overflow pair). There are no companion fragments and no inbound-link repairs in other candidates for this theme.
