# Review package — theme:cosmonaut-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:cosmonaut-jp — origin EN, population #8 [GOSIGN2-LEDGER (b) row 8]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now f039a0db30cbb999cff34dd09e5ca9ecb557cd3b3e8c5cda2457b79ac4786583); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 8; GOSIGN2-LEDGER (b) row 8]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 934px@768 / 327px@320, header/account clip, sidebar x=24, contrast 3.2 (readable—machine warn), sample credit-modal. [RENDER-ROWS-1 (RENDER-A row 8)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 8)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 9, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 9]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 8]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:cosmonaut-jp.txt sha256:f039a0db30cbb999cff34dd09e5ca9ecb557cd3b3e8c5cda2457b79ac4786583; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/cosmonaut-jp/candidate.txt (sha256 a6d1f77696876a9b7e3f71459146972dd3cc12e15fc17f6470f3a7df70f7201c)
Original: theme:cosmonaut — scp-wiki, revision 27 (sha256 7d315826293db9af4419d47ffd594a19bfbe6bd458493de0dc410f34693a18a4)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 8), and the generated stamp as built read PASS: the candidate's bytes had not changed since the verdict era (its last change, commit 8dcac74, predated the determination). A later landing, canonical commit 358955e (FIX-SNIPPET, the production-predecessor reference audit), repaired two usage-example lines, so the regenerated stamp now reads STALE with the record verdict standing |
| Wave history | This theme's history is not the Stage 2 creation-plus-fix-waves shape. The candidate is the Sigma-10 check copy of the migration of an existing SCP-JP production page (kind K6): the production page was translated from revision 23 by a human translator, re-translated against revision 27 in the campaign's Phase 17, and imported into this repo whole (commit d727e92), with two small reconciliations after (commits ffad285, 8dcac74). The GOSIGN2 waves touched nothing in the file; their record for it is examination and disposition. Each act is narrated in the Per-theme record |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (ii)); the narrow-width header/sidebar geometry family (KB-35; FIX3-S2EN §6.5, X1–X9); the sample credit-modal (preview-form property, ruling 5's ground); the localize lane's two honest items (an untranslated name inside a fake footer specimen; a header-only JP font), dispositioned on the lane's own "display-unbreaking" severity framing; the credit label variants (staff-normalization item). No item is flagged |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:cosmonaut | theme:cosmonaut-jp (check copy of the production migration; the production page is theme:cosmonaut) |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revisions | **Two**: 23 (first translation) and 27 (re-translation); this package's mirror is revision 27, the revision the current JP text was made from | — |
| Source of this copy | Re-fetched at revision 27 by the campaign (mirror store class FETCH-REGEN; whitespace-compared against the localize lane's cache in the freeze audit), because the S2-era cache held an earlier revision state | Canonical file `pages/theme:cosmonaut-jp.txt`, imported whole in commit d727e92 (canonical sources for the display-check composition); its last content change is commit 8dcac74 (Phase 17) |
| Lines / bytes | 1,940 lines / 104,618 bytes (the last line carries no trailing newline, so `wc -l` reports 1,939) | 1,960 lines / 109,345 bytes (last line unterminated; `wc -l` reports 1,959) |
| SHA-256 | 7d315826293db9af4419d47ffd594a19bfbe6bd458493de0dc410f34693a18a4 | a6d1f77696876a9b7e3f71459146972dd3cc12e15fc17f6470f3a7df70f7201c |

Provenance route: this is the K6 shape — a production page already exists on SCP-JP (theme:cosmonaut, held in this repo at `pages-existing/existing:theme-cosmonaut.txt`), and the migration is delivered as a delta against it, recorded in `pages/phase17-diff-cosmonaut-jp.txt`. The candidate in this package is the check-composition copy of the migrated page; its exact relationship to the production page (seven enumerated differences, 73 diff lines) is set out in the Per-theme record, because for this theme the production page is a third source a reviewer needs. Reference-revision currency: the follow-up artifact `diff-cosmonaut-from27.txt` in the campaign record records rev27 → rev27, no changes, so revision 27 is still the upstream latest; the sources.tsv note for this row says otherwise and is dealt with in the Per-theme record. The TSV's production-drift column for this row reads 一致 (in agreement).

## Summary

Cosmonaut is a large Oneiroi Collective theme (the diff runs to 17 hunks over a 1,940-line original) with a two-part stylesheet: a main exhibit and a second, smaller exhibit carrying the "twilight" variant, switched by an include parameter. Unlike the other themes in this batch, the JP text is not a campaign creation: SCP-JP already had the theme, translated by nebula2700 from revision 23, and the campaign's work was a re-translation against revision 27 plus the Sigma-10 environment adaptations (a delivery frame the EN original does not have, credit-modal selector extensions inside the exhibit, and two appended correction modules for the credit modal and the mobile navigation). The GOSIGN2 examination found no defect to fix in the file: its charges are the narrow-width geometry family the whole EN population shares, the preview-form credit modal, and two items the localize lane itself framed as display-unbreaking (a name left in English inside a fake footer specimen, and a JP font that covers the header stack only), all dispositioned. The reviewer's real work in this package is the provenance: three sources (EN revision 27, the production page, the candidate) and the deltas among them, each stated where it belongs.

## Class summary

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 41 |
| TRANSLATION-ANCHORED | 19 |
| CSS-BODY | 19 |
| ASSET-REHOST | 6 |
| DRAFT-HOST | 3 |
| SELF-DELIVERY | 3 |
| ESCAPED-INCLUDE | 2 |
| INCLUDE-REPOINT | 2 |
| DELIVERY-HOST | 2 |
| T7-CREDIT-CSS | 2 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |

Counts: 96 blocks — 34 specific (35.4%), 59 heuristic (61.5%), 3 residue (3.1%), 0 skipped. The heuristic share is this file's size speaking: most of its mass is the two CSS exhibits, whose rule-level edits the classifier can only label CSS-BODY, plus the long translated sample. Topology: both sides carry two code-css components and two tail delivery modules; the candidate adds a frame and two correction modules at the tail (the topology pass lists them as candidate-side components with no original counterpart, which is correct — they are JP-side additions, sections 3 and 8). Labels are sets per block; these sections were written from classification.json's label spans. Four adjudications matter. (1) The 19 CSS-BODY blocks are the exhibits' rule-level delta: font imports and stacks (section 4), the credit-modal selector extensions (blocks B90–B92, section 8), the mask/data-URI values carried unchanged in substance, and the tail corrections (B96, section 3); none is an unexplained rewrite, and the residue three are among them (Appendix). (2) The six ASSET-REHOST blocks are the production lineage's storage moves (section 4). (3) The single EXHIBIT-RESTRUCTURE primary is a repoint inside an exhibit line; the exhibit census is one-to-one (section 8). (4) The derived-presence pass reports HTTP-KEPT ×8; every `http://` occurrence in the candidate (grep: 9 lines — cand L281–286, L504–505, L1895) sits inside a `data:image/svg+xml` value as the W3C namespace string, so the signature false-fires on all of them (section 11).

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with the gate (orig L1), a bare Rate in a right-aligned div (orig L5–8), and the prose attribution (orig L10: made by EstrellaYoshte for Luxaiko, forked from the Newspaper Theme). It has no frame and no head module; its delivery lives entirely at the tail (section 3). The candidate opens with the localized gate (cand L1), the credit block (cand L4–14), and the translated prose (cand L16), the userlinks of the production text rendered as plain names in this check copy (Per-theme record). Provenance route: K6 production migration (see Provenance); the two reference revisions (23 first translation, 27 re-translation) are both recorded in the candidate's credit block, which is the only file in this batch whose provenance needs two numbers.
- **Why:** For a K6 theme the header zone is where the migration's nature is declared: the credit block's pair of revision fields is the declaration, and a reviewer who misses it will misread every later delta as a fresh port's choice rather than a re-translation's.
- **Verify:** Read original L1–12 against candidate L1–16; the credit block's two revision fields at cand L11–12.
- **Disposition:** Recorded; the credit reading is section 1, the delivery reading section 3.

### 1. Credit and attribution

- **What:** The candidate's credit block (cand L4–14) is the production page's own, carried through the migration: nine fields — title Cosmonautテーマ, translator **nebula2700** (the human translator of the production page, named in plain form in this check copy; the production page carries the `[[*user nebula2700]]` form), translation year 2025, original title Cosmonaut Theme, copyright holder EstrellaYoshte, creation year 2022, first-translation reference revision 23, re-translation reference revision 27 (added by the Phase 17 commit 8dcac74), and the source link labeled ソース. The original's bare Rate (orig L5–8) has no candidate counterpart: the production lineage already rates through the credit block, so there was never a KB-09 duplicate in this file's JP life. Attribution beyond the block: the prose sentence (orig L10 → cand L16) names EstrellaYoshte as maker and Luxaiko as the commissioning reader, and the ornament credits survive translated (section 6): the header logo by Aethris, the cloud graphics by Luxaiko, and the three Wikimedia Commons ornament files with their links (the candidate's links gain `?uselang=ja`). There is no license box on either side. The label variants a reviewer will notice — the ソース link label, the plain-name forms — are the production page's forms, and the ledger records exactly those variants as the staff-normalization item (below).
- **Why:** Ruling 3's TASL discipline is satisfied by the production block's own fields; ruling 3 also keeps human translator names where they are the record, and this block is a human translation's record, not a campaign credit — the FIX-CREDIT waves that normalized the Stage 2 creations' blocks (translator AI) correctly did not touch it. The re-translation revision field is the Phase 17 addition that makes the two-revision provenance auditable from the file itself.
- **Verify:** Read candidate L4–14; `diff pages-existing/existing:theme-cosmonaut.txt pages/theme:cosmonaut-jp.txt` for the block's exact deltas against production (userlink forms, the added revision field); `git show 8dcac74 -- pages/theme:cosmonaut-jp.txt` for the field's addition.
- **Disposition:** Standing. The label variants are DISPOSITIONED as the posting-procedure staff-normalization item (ledger (c3), via the LOCALIZE-S2-C checklist item 9 reference); no credit defect is charged.

### 2. Includes and components

- **What:** The candidate's complete include list (grep): the credit pair (cand L4/L14), `:scp-jp:component:image-block` (cand L28, its asset a JP-storage file, section 4), the two escaped usage includes (cand L20: `:scp-jp:theme:cosmonaut`; cand L24: the same with `twilight=--`), and the tail frame (cand L1929). The usage names deserve a reviewer's attention: they name theme:cosmonaut, the production fullname, not the candidate's -jp name. That is correct for a K6 migration — the deliverable is the production page itself, updated in place, so its usage instructions name the page readers will actually include. (The documentation-era sweep that rewrote self-references to -jp forms across the Stage 2 population did not touch this file, for the same reason.) The twilight usage is the theme's own mechanism: the second stylesheet is gated by the include parameter (section 3). The image-block include is repointed from the original's form; no `:scp-wiki:` include remains (grep: 0). No include is duplicated.
- **Why:** P1 repoints foreign includes to the JP site; the self-name question is answered by the migration's topology (the candidate's posting target is the production page), not by the population's default. Ruling 4's component rule does not engage: the theme needs no component port beyond the standard furniture.
- **Verify:** `grep -n '\[\[include' candidate.txt` (six lines); read cand L20/L24 against the K6 provenance in section 0.
- **Disposition:** Standing; no foreign include is kept, so KB-15/KB-54 do not engage.

### 3. Delivery and code loading

- **What:** The stylesheet lives in two code exhibits on both sides: the main CSS (orig L238–1886 → cand L245–1883) and the twilight variant (orig L1888–1928 → cand L1885–1925), so the fragments are /1 and /2 on both sides, and the self-delivery addresses are correct (SELF-DELIVERY ×3). The original delivers them with two tail modules (orig L1932–1939): the first @imports /1 unconditionally; the second @imports /2 inside a comment-gate — `[!-- {$twilight}]` … `[!-- --]` — which is the include-parameter mechanism: a page including the theme with `twilight=--` substitutes the parameter so the comment markers neutralize and the module renders. The candidate keeps both modules, repointed to its own /1 and /2 on the draft host (cand L1934–1943, the comment-gate byte-preserved in form), and adds two things the original does not have. (a) An interwiki-style frame at the tail (cand L1929–1932, `priority=1`, theme= own /1 on the draft host): the Sigma-10 environment's standard delivery frame, which the production page also carries in its production form (naming scp-jp.wdfiles.com/local--code/theme%3Acosmonaut/1 — the candidate↔production delta is the host and name form only). (b) Two appended correction modules (cand L1945–1960), in English-commented JP-side form: a credit correction (`#u-credit-view .modalbox .modalbox-ratemodule { position: static; }` plus a ≤359px box-sizing rule, keeping the modal's rating in document flow below the license control) and a navigation correction (anchoring the rightmost mobile submenu at ≤767px and ≤359px). Both are candidate-side additions of the check composition (the production page does not carry them; Per-theme record), of the T7 credit-CSS family for the first and a furniture repair for the second.
- **Why:** P4/T9: a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting — here, to the production page's own /1 and /2, since the posting target is theme:cosmonaut itself. The frame addition follows the environment's delivery standard (the M-frame population's P6 form). The correction modules are the JP environment's supplements, of the same standing as the in-exhibit selector extensions in section 8: they exist because the Sigma-10 credit module and mobile navigation differ from what the EN CSS was written against.
- **Verify:** `grep -n '\[\[code' candidate.txt` (two blocks, L245 and L1885) against the three /1-and-/2 references (cand L1931, L1935, L1941); read candidate L1929–1960 against original L1930–1940; `diff` against the production page for the frame's form delta.
- **Disposition:** The draft-host references are class (iii) draft form, recorded in section 11. The frame and corrections are standing JP-side supplements, not dispositions.

### 4. Fonts and assets

- **What:** The original's exhibit loads its faces three ways (orig L240–274): the particles stylesheet from its own EN files (L240), two faces from fonts.bunny.net (Berkshire Swash, Anonymous Pro; L243–244), and Atkinson Hyperlegible through four self-hosted @font-face blocks (L246–274). Its stacks (orig L293–295): header `"Berkshire Swash", cursive`, body `"Atkinson Hyperlegible", sans-serif`, mono `"Anonymous Pro", monospace` — no JP face anywhere. The candidate's exhibit (cand L246–254) carries the production lineage's arrangement as Phase 17 left it: the particles import first, repointed to the JP storage host (below), then a fonts block of four Google Fonts lines (Berkshire Swash; Kaisei Opti; Atkinson Hyperlegible; Anonymous Pro with its italic axis) — the coollabs forms the production page still carries were repointed to googleapis by commit 8dcac74, and the block sits after the particles import where the production page has it before (the phase17-diff instructs exactly this repositioning for production). The stacks (cand L272–274): header `"Berkshire Swash", "Kaisei Opti", cursive` — Kaisei Opti, a JP display face loaded at weight 700, is the production translation's supplement, documented in the body by a footnote （日本語文字はKaisei Opti, cand L230); body and mono stacks are unchanged from the original and name no JP face. Assets (ASSET-REHOST ×6): the theme's files move from EN hosts to the JP storage wiki (scp-jp-storage.wdfiles.com) under `file:8260379-*` names — hpl2.png (the image-block's picture, cand L28), particles.css (the exhibit's first import), and Canine.png (the social-sample avatar, orig on the number-27-oneiroi-station page's files) — the production lineage's hosting, since the production page's attachments live on the storage wiki. The remaining graphics are data-URI masks carried in substance (section 11, item 5).
- **Why:** P7/T5 (KB-16): the header-only JP supplement is the production translation's own answer to the JP-font question; the localize lane charged the body/mono gap and the ledger dispositioned it on the lane's severity framing (below), so this package records the stacks exactly rather than re-charging them. P5 (KB-17, patterns 9c5e907): Google Fonts is on the allowed hotlink list; the bunny.net and coollabs mirrors are outside it, which is what the Phase 17 repoint disposed of. The storage re-hosting is the production page's own arrangement (its files were never the EN wiki's to keep).
- **Verify:** `grep -n '@import\|@font-face' original.txt candidate.txt` (the candidate has no @font-face and no bunny/coollabs line); read candidate L272–274 against original L293–295; `grep -n 'scp-jp-storage' candidate.txt` for the three storage assets.
- **Disposition:** The font-host repoints are FIXED by Phase 17 (commit 8dcac74 in this repo's record). The body/mono JP gap is DISPOSITIONED (ledger (c3) via ledger line 1702: the lane's "display-unbreaking" framing).

### 5. Header, sidebar, site furniture

- **What:** This is the theme whose render row is a furniture charge sheet: page-overflow 934px at 768px and 327px at 320px, header/account clipping, a sidebar offset (x=24), and a contrast warning at 3.2 (readable, a machine warn). None of it is a candidate-side furniture edit: the theme's header, sidebar and top-bar rules are the original's, carried; the JP-side furniture interventions in the file are the two tail corrections (section 3), of which the navigation correction addresses the mobile submenu's anchoring, a different item from the charged offsets. The theme's own header text values are the production translation's, and no P8/P9 adaptation was charged against them.
- **Why:** The charged geometry is the narrow-width header clip/collision family (KB-35; the FIX3-S2EN §6.5 X1–X9 analysis), which the ledger dispositions for the population rather than repairing theme by theme; a reviewer can re-derive the family membership from the row's own wording (clip and collision at narrow widths, clean at desktop).
- **Verify:** RENDER-ROWS-1 (RENDER-A row 8) for the charge text; ledger (c2) for the family disposition; candidate L1951–1960 for the one furniture supplement the file does carry.
- **Disposition:** DISPOSITIONED (ledger (c2): the KB-35 family). The contrast item is a machine warn the row itself marks readable.

### 6. Text translation

- **What:** The body is the production translation, retained entire: 19 TRANSLATION-ANCHORED and 41 TRANS-UNANCHORED blocks cover the prose, the heading specimens, the Oneiroi social samples (the or-tweet and or-comment pairs, live and exhibit forms), and the ornament credits. Two translation facts need a reviewer's eye. (a) The fake footer specimen: the sample's "last edited" line reads 最後の編集 13:22 OWST by Some Dude (cand L150), with its exhibit twin at cand L156 — the sentence is translated and the time converted, but the editor's name stands in English, exactly as the localize lane recorded it (its row names both instances). (b) The social samples' joke timestamps are translated in form and preserved in absurdity (25/02/2016 16:32; "Jan 33, 2017 0:61" — the original's impossible date and time, carried as the specimen's joke, not corrected). The exhibit comment texts inside the CSS are the production lineage's (the correction modules' English comments are JP-side additions, section 3). No glyph-form conversions (R5) occur.
- **Why:** P10: body text is translated; a specimen's content (a fake editor name inside a fake footer, an impossible date inside a joke timestamp) is the specimen, and the localize lane's own framing — "display-unbreaking but honest" — is the ground on which (a) stands. The lane listed it so the fact is on record, not so it would be silently normalized later.
- **Verify:** Read candidate L148–158 against original L140–150; the LOCALIZE-ROWS row 9 text for the lane's own wording.
- **Disposition:** Standing (the production translation). Item (a) is DISPOSITIONED on the lane's severity framing (ledger line 1702).

### 7. Links

- **What:** The credit block's source link (cand L13) is the required back-reference, labeled ソース in the production form (section 1). The prose fork link, `[[[theme:newspaper|Newspaperテーマ]]]` (orig L10 → cand L16), names the EN theme the work forks from: on the JP wiki that fullname is not a JP page, and no JP candidate of newspaper exists in this campaign's set for it to name instead — the same kept-no-counterpart shape as the chaos package's author-page exhibit, recorded here rather than charged. The ornament credits' Wikimedia Commons links are kept, gaining `?uselang=ja` in the candidate (a reader-facing localization of the link target's UI language; the files named are unchanged). No other body links exist.
- **Why:** P11 repoints where a JP counterpart exists; where none exists, the honest form is the kept target with the fact recorded.
- **Verify:** `grep -n 'theme:newspaper\|wikimedia' candidate.txt`.
- **Disposition:** Standing; no link flag.

### 8. Structure

- **What:** The closing rule is honored across a 1,940-line file: both exhibits keep their rule order in substance, the twilight mechanism keeps its comment-gate form, and the sample body is retained entire (the social samples in live-plus-exhibit pairs, the footnoteblock in its check-copy escaped form — Per-theme record). The JP-side structural additions are three, all at the delivery layer: the frame and the two correction modules (section 3), and one in-exhibit extension a reviewer should not mistake for churn — blocks B90–B92 (orig L1694–1705 → cand L1683–1702, CSS-BODY heuristic) extend the theme's credit-modal rules to the JP credit view's selectors: `#page-content .modalbox` gains the sibling selector `#u-credit-otherwise .modalbox`, and a `.modalbox-title` rule is added in the same zone. That is the T7 credit-CSS adaptation inside the exhibit, the counterpart of the tail's credit correction module. Brace structure verified by depth scan for this package: both code exhibits and all module CSS blocks end at depth 0 with no negative excursion on both sides (the candidate has four modules to the original's two, per the additions above).
- **Why:** Residue class R3: each structural delta's ground is stated. The exhibit census is one-to-one; every addition is at the delivery or credit layer, which is where a migration's supplements belong.
- **Verify:** Read candidate L1683–1702 against original L1694–1705 for the selector extension; the depth scan is reproducible from the two package files.
- **Disposition:** Standing (no exhibit restructuring in substance).

### 9. Formatting only

- **What:** none — the classifier counts 0 whitespace-only blocks and 0 re-indentation blocks over 96 change blocks.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; here the ground for "none" is the classifier count above.
- **Verify:** classification.json (summary: reindent_blocks 0; no WS-ONLY label in the label counts).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The candidate carries the production lineage's annotations in two forms. (a) A reader-visible footnote in the font exhibit (cand L230): 日本語文字はKaisei Opti — the production translation's note that Japanese characters are set in Kaisei Opti, attached to the header-font line. (b) The two correction modules' English comments (cand L1946, L1953), which name themselves as SCP-JP corrections and state what each does; they are the JP-side editors' annotations riding on their own modules. There are no `[!-- ... --]` translator notes (`grep -c '\[!--' candidate.txt` counts only the twilight comment-gate pair, which is mechanism, not annotation — section 3).
- **Why:** R2: porter additions are listed so they are never mistaken for original content. Here the annotations are inherited from the production lineage rather than added by this campaign, and the listing keeps that straight.
- **Verify:** Read candidate L230 and L1945–1960.
- **Disposition:** Standing (inherited annotations, recorded).

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) T1 pseudo-ref ×2, DISPOSITIONED class (ii): references to pages not yet posted under those names at baseline; they resolve at posting. (2) The render findings: page-overflow at 768/320px, header/account clip, sidebar offset, the readable contrast warn — DISPOSITIONED as the narrow-width family (KB-35; FIX3-S2EN §6.5 X1–X9) in (c2); and the sample credit-modal, DISPOSITIONED as the preview form's property (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, ruling 5's ground). (3) The localize lane's two items — the untranslated name in the footer specimen (section 6) and the header-only JP font (section 4) — DISPOSITIONED on the lane's own "display-unbreaking" severity framing (ledger line 1702). (4) The credit label variants: DISPOSITIONED as the staff-normalization item (section 1). (5) The derived-presence HTTP-KEPT ×8: adjudicated NOT kept references — every `http://` occurrence in the candidate sits inside a `data:image/svg+xml` mask value as the W3C namespace string (cand L281–286, L504–505, L1895); none loads anything. (6) The draft-host delivery references (cand L1931, L1935, L1941): class (iii) draft form (P4), rewritten at posting — for this theme, to the production page's own fragments.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa; for item 5, read the lines named.
- **Disposition:** DISPOSITIONED (items 1–4, 6); item 5 recorded as a classifier false positive.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 2 errors / 0 warns / 1 info, the errors pseudo-ref ×2 (T1-ROWS row 8). Register (c1) dispositions pseudo-ref as class (ii). (b) T2/T3 render: FINDINGS — the geometry family and the preview-form credit modal, both dispositioned in (c2) (RENDER-ROWS-1, RENDER-A row 8). (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting count (LOCALIZE-ROWS row 9, LOCALIZE-A): the lane's row charges the two honest items (footer name, header-only font) under its "display-unbreaking" head, and (c3) dispositions the row's charges under the class outcomes (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves — for this theme, satisfied by the production block and the Phase 17 field addition, not by a credit wave). The follow-up currency check found nothing to follow: the upstream latest is still revision 27 (campaign record, `diff-cosmonaut-from27.txt`). (d) T5: judged jointly with T4 by the localize lane. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (96 change blocks) and the generator's (diff.md: +193/−180 in 17 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:cosmonaut-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS at the ledger determination ((b) row 8), and the stamp as built read PASS (Status table); after the FIX-SNIPPET landing 358955e the regenerated stamp reads STALE, with the record verdict standing.

## Per-theme record

### Provenance acts, one by one

This theme's class-U story is a provenance chain, not a fix wave. (1) The production translation: SCP-JP's theme:cosmonaut was translated from EN revision 23 by nebula2700 (translation year 2025 per the credit block; creation year of the EN work 2022). (2) Phase 17 re-translation: the JP text was brought to revision 27; the delta for the production page is recorded in `pages/phase17-diff-cosmonaut-jp.txt` (two hunks: the re-translation revision field added to the credit block, and the fonts block repointed from coollabs to googleapis and repositioned after the particles import). (3) The canonical import, commit d727e92: the candidate entered this repo whole (1,960 lines) as part of the display-check composition's canonical sources. (4) The pair reconciliation, commit ffad285 ("Reconcile 15 theme pages to the live pair state"): one change — the sample's `[[footnoteblock]]` became the escaped `@@[[footnoteblock]]@@` form the live check-wiki pair carries. (5) Phase 17 in-repo, commit 8dcac74: the candidate gained the 改訳時参照リビジョン： 27 field and the googleapis font repoints (the same acts the phase17-diff prescribes for production). No GOSIGN2 wave commit touches the file; the ledger's examination (LOCALIZE-A, RENDER-A, T1) is its whole sweep-era record.

### The candidate against the production page (the third source)

`diff pages-existing/existing:theme-cosmonaut.txt pages/theme:cosmonaut-jp.txt` is 73 lines, in seven groups. (a) Credit userlink forms: production carries `[[*user nebula2700]]` and `[[*user EstrellaYoshte]]`; the candidate carries the plain names. (b) The candidate adds the re-translation revision field (Phase 17). (c) Prose userlinks: production's maker/commissioner and cloud-artist links are plain names in the candidate. (d) The footnoteblock form (act 4 above): production live, candidate escaped — a check-composition form; the phase17-diff does not prescribe it for production. (e) The fonts block: production still carries the coollabs imports before the particles import; the candidate carries the Phase 17 googleapis form after it. (f) Delivery addresses: production's frame and modules name scp-jp.wdfiles.com/local--code/theme%3Acosmonaut/N; the candidate's name the draft host and the -jp fullname (class (iii) check form). (g) The two correction modules are candidate-only: the production page's file ends with the twilight module, while the candidate appends the credit and navigation corrections (section 3) — Sigma-10-environment supplements that the check composition carries and production does not. A reviewer judging the migration should read (b) and (e) as the migration's prescribed delta, (a), (c), (d) and (f) as check-copy forms, and (g) as environment supplements awaiting the same journey.

### Record conflict — the sources.tsv note for this row

sources.tsv's notes column for this theme states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-cosmonaut-from27.txt` (kind K5a-i). The artifact (in the LOCALIZE-A lane's record) records the opposite: `rev27 → rev27 変更: なし` (no changes), with an empty intervening-revision list. There is no post-reference delta to classify and no supersession; revision 27 is both the re-translation reference and the upstream latest. The note is a population-level convention in sources.tsv (the same shape recorded for the ambrose-chapter-two, caretaker-sigma, chaos and clock-tower rows); for this row it does not survive contact with its own citation, and this package follows the artifact.

## Change set outside the two diffed files

The diff covers two files; this theme's change set is the widest in the batch. (1) `pages-existing/existing:theme-cosmonaut.txt` — the production page itself, the migration's target and this package's third source. (2) `pages/phase17-diff-cosmonaut-jp.txt` — the migration's application record: the two-hunk delta a production editor applies to bring the live page to the candidate's state on the prescribed items. (3) `pages/theme-decoration-sample-cosmonaut-jp.txt` — the render sample page; it is the "sample" the T2/T3 checks rendered, and its credit-modal line is the render row's subject. (4) `pages/theme:cosmonaut.txt` — the repo's EN-side copy of the original page, the EN sample's base. (5) The storage assets on scp-jp-storage.wdfiles.com (hpl2.png, particles.css, Canine.png under `file:8260379-*`), the production lineage's file hosting that the candidate's references name. (6) The delivery itself: the candidate's own local--code /1 and /2 on the draft host, named by the frame and the two tail modules, which are the runtime form of the two exhibits; at posting they become the production page's own fragments.

## Multi-wave provenance

The candidate's current state is the product of a production translation, a Phase 17 re-translation, and the check composition's reconciliations — not of the Stage 2 pipeline: nebula2700's production translation from revision 23 (2025) is the base text; Phase 17 brought it to revision 27 and recorded the production delta; the canonical import (commit d727e92) brought the check copy into this repo; the pair reconciliation (ffad285) and the Phase 17 in-repo acts (8dcac74) settled its current bytes before the GOSIGN2 sweep began. The sweep's lanes then examined it as population #8 (LOCALIZE-A row 9, RENDER-A row 8, T1-ROWS row 8), charged only disposition-class items, and the ledger determination passed it with no OPEN items, so the FIX5 wave had nothing to re-judge so no wave in the package era touched it — which is why its stamp as built read PASS. The later FIX-SNIPPET landing (canonical commit 358955e, the production-predecessor reference audit) repaired two usage-example lines after the build; the regenerated stamp consequently reads STALE against that post-build change, with the record verdict standing. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 8, (c1) foreign-include exception set (this theme is not in it), (c2) cosmonaut entry, (c3) cosmonaut entries (lines 1395, 1408, 1702); GOSIGN2-LEDGER-SUPPLEMENT.md (no cosmonaut entries); T1-ROWS row 8; LOCALIZE-ROWS row 9; RENDER-ROWS-1 (RENDER-A row 8). The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

Three residue blocks were emitted, all in the exhibits' CSS, all resolved here. R1 = B90 (orig L1694–1696 → cand L1683–1685, CSS-BODY): the credit-modal selector extension (`#page-content .modalbox` gaining `#u-credit-otherwise .modalbox`) — the T7 credit-CSS adaptation, written up in section 8. R2 = B91 (orig L1702 → cand L1691–1695) and R3 = B92 (orig L1705 → cand L1698–1702): the added `.modalbox-title` rule and its closing brace, the same adaptation's other half, likewise section 8. (The classifier's own T7-CREDIT-CSS label fired on two other blocks in the tail zone; these three carry only the heuristic CSS-BODY label because their change is selector text, not a signature shape.) No new signature is proposed: a selector-extension census would be a population tool, and the lane report notes it as a possible classifier refinement rather than a pattern.

## License and attribution

- **Title:** Cosmonaut Theme
- **Author:** EstrellaYoshte
- **Source:** https://scp-wiki.wikidot.com/theme:cosmonaut — revision 27 (revision date 2025-12-14 11:15:02)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: nebula2700 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
