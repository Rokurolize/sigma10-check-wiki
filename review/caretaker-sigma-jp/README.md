# Review package — theme:caretaker-sigma-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:caretaker-sigma-jp — origin EN, population #67 [GOSIGN2-LEDGER (b) row 67]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now b831587f6d54dafd9d2496f760b858b7de83af53662a30befe2d32a1bf297f1a); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 0 infos (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 72; GOSIGN2-LEDGER (b) row 67]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — port defect: `interwiki-style` rejected (missing `priority` parameter); no other candidate-specific defect. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 67, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 67]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 67]
- Computed against: canonical commit ba896f4f980ac8fdf8c288b2faab80a226eca212; candidate file pages/theme:caretaker-sigma-jp.txt sha256:b831587f6d54dafd9d2496f760b858b7de83af53662a30befe2d32a1bf297f1a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/caretaker-sigma-jp/candidate.txt (sha256 5fb18dc46cb1bd65288ba61a28b3b8fb2f4a0f78e660d8847a15024dde131b0d)
Original: theme:caretaker-sigma — scp-wiki, revision 10 (sha256 3408d5f857d95360d5dd359cbcb3490b8b175ca72a05e799b29248c8e87b0188)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 67). The generated stamp above reads STALE by design: the only post-verdict change to the candidate is the population sweep's one-line usage-name repair (Per-theme record), and the stamp does not carry a PASS onto changed bytes |
| Wave history | Four commits touch the candidate: the Stage 2 EN5 creation (7e07438), FIX-CREDIT-D's translator-field normalization (1869877), FIX4-LICENSE (c2a8bee: `priority=1` restored and the license box wrapped), and the usage-example sweep (b5cb724). Each is narrated in the Per-theme record |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 (P5, class (ii) / KB-58); T1 pseudo-ref ×1 (class (ii)); the draft-host delivery pair (class (iii)). Two items are **flagged**, not dispositioned, by this package: the dropped `[[footnoteblock]]` and the font supplement's override of the page-title face (Per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:caretaker-sigma | theme:caretaker-sigma-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (first translation; the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-caretaker-sigma.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:caretaker-sigma-jp.txt`, created in commit 7e07438 (Stage 2 EN5); its last content change is commit b5cb724 (the usage-example sweep) |
| Lines / bytes | 424 lines / 8,172 bytes (the last line carries no trailing newline, so `wc -l` reports 423) | 436 lines / 9,560 bytes |
| SHA-256 | 3408d5f857d95360d5dd359cbcb3490b8b175ca72a05e799b29248c8e87b0188 | 5fb18dc46cb1bd65288ba61a28b3b8fb2f4a0f78e660d8847a15024dde131b0d |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted. Reference-revision currency: the follow-up artifact `diff-caretaker-sigma-from10.txt` in the campaign record records rev10 → rev10, no changes, so revision 10 is still the upstream latest; the sources.tsv note for this row says otherwise and is dealt with in the Per-theme record.

## Summary

The original is a Sigma-9-era theme page that carries everything on one page: an interwiki-style frame at the head, a bare Rate and an info module, a short prose introduction, the full element sample body (collapsible, tabview, blockquote, table, footnote), its whole stylesheet as a code exhibit served as the page's own local--code /1, a license box, and a tail module that loads the exhibit. The candidate keeps that single-page shape almost intact: the sample body is retained and translated in place, the stylesheet stays in its code exhibit in the same order, and the JP changes sit where the campaign's classes put them (preview credit block at the head, info module and bare Rate removed, font imports repointed to Google Fonts with a Noto Sans JP load and an appended fallback block, license entries re-wrapped in the JP license box, delivery consolidated at the tail). The measured churn (diff.md: +144/−137 in 2 hunks; the classifier counts 52 change blocks) is mostly the sample body's line-by-line translation. The theme's one real port defect, a frame shipped without its `priority` parameter, was found by the render walk and fixed by FIX4-LICENSE; two smaller items no register charged (a dropped `[[footnoteblock]]`, and the appended font block's side effect on the page-title face) are flagged in the Per-theme record.

## Class summary

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 26 |
| TRANSLATION-ANCHORED | 19 |
| EXHIBIT-RESTRUCTURE | 4 |
| SELF-DELIVERY | 3 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| INFO-DEL | 2 |
| LICENSE-BOX | 2 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| TASL-FIELDS | 1 |

Counts: 52 blocks — 27 specific (51.9%), 24 heuristic (46.2%), 1 residue (1.9%), 0 skipped. Topology: no relocation; each side's components match by kind (the original's code exhibit orig L141–401 answers to the candidate's cand L137–412, and the tail module likewise). Labels are sets per block; the skeleton lists each block once under its primary label, so these sections were written from classification.json's label spans. Four adjudications matter. (1) B2's primary is EXHIBIT-RESTRUCTURE, but the block also carries the CREDIT-PREVIEW, TASL-FIELDS and CREDIT-PROSE spans (the credit block's insertion is paired with the head frame's removal); section 1 is written from those spans, not from the skeleton's section 1, which shows only INFO-DEL and LICENSE-BOX. (2) B47's RESTORATION label is a diff-only signal: the appended JP font block's selectors match the original's own earlier heading rule; nothing was deleted and restored by a wave, and the block has been in the file since creation (section 4). (3) B48's LICENSE-BOX pairing (orig L404 → cand L415) conceals a deletion: orig L404 is the `[[footnoteblock]]` line, which has no candidate counterpart (Per-theme record). (4) B7's EXHIBIT-RESTRUCTURE primary is an include repoint inside the image-block exhibit line, not a restructuring (section 2).

## Standing sections

### 0. Header and provenance frame

- **What:** The original's header (L1–16) is the frame, a bare Rate and an info module inside the `[[iftags +theme]]` gate: the interwiki-style include at L3–6 (`priority=1`, theme= the page's own /1 on scp-wiki.wdfiles.com), the `[[>]] [[module rate]] [[/>]]` at L8–10, and `:scp-wiki:info:start`/`end` at L12/16 around placeholder text. The candidate's header (L1–12) is the gate (L1, tag localized) and the preview credit block (L3–12); the frame itself sits at the tail with the delivery module (cand L430–436), where the original already kept its tail module (orig L422–424). Provenance route: derived from the original at reference revision 10 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery and its rating furniture; P2/P3/P6 rework exactly this zone for the JP environment, and each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–16 against candidate L1–12 and L428–436; blocks B1–B5 in classification.json.
- **Disposition:** Recorded; the credit reading is section 1, the delivery reading section 3.

### 1. Credit and attribution

- **What:** The original's rating furniture is the bare `[[module rate]]` (orig L9) plus the info module pair (orig L12/16) whose body is placeholder text ("This is a rating box with a credit module. / Testing, testing, 1-2-3."). Both are removed (INFO-DEL blocks B4/B5; the Rate's removal rides in B3, orig L8–10). The candidate adds the preview credit block at the head (cand L3–12, spans inside B2): `:scp-jp:credit:start-preview` / `end-preview` carrying all eight ruling-3 fields (cand L4–11) — title Caretaker Theme（Sigma版）, translator AI, translation year 2026, original title "Caretaker Theme (Sigma Version)", copyright holder winkwonkboi, creation year 2025, reference revision 10, and the source link to the EN page. The holder matches the original's own attribution (prose, orig L20; license box, orig L410). The license box: the original wraps its entries in `:scp-wiki:component:license-box-theme` (orig L407/419) with the entries in blockquote form (orig L409–417); the creation carried the entries as a bare list under a `+ 画像の出典` heading with no box wrapper; FIX4-LICENSE (commit c2a8bee) replaced the heading with `:scp-jp:component:license-box-backend` (cand L415) and added `:scp-jp:component:license-box-end` (cand L426), and the entries stand in the JP list form (cand L417–424): feesh.png + carebody.png by winkwonkboi, AEEDLogoWhite.png by GreenGolem, both CC BY-SA 3.0, source "SCP Foundation" — both attribution lines of the original survive, including the second author's. T7 credit CSS: the theme's own `.rate-box-with-credit-button` / `.creditButton` rules (orig L258–269) are carried verbatim inside the exhibit (cand L255–266); supplement type T7 by inheritance, not by addition.
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form, so the bare Rate beside it would double-render the widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa) and the info module is not JP furniture (ledger class C). Ruling 3 fixes the eight fields and credits campaign translations to AI; the translator field read SCP-JP at creation and was normalized to AI by FIX-CREDIT-D (commit 1869877, a one-line change to this file). T4/KB-63: a license box the port drops must be restored in its settled JP form; here the entries were never dropped, only their wrapper was, and FIX4-LICENSE restored the wrapper.
- **Verify:** Read candidate L3–12 against the eight-field list; `grep -n 'info:start\|info:end\|module rate' candidate.txt` (absent) against original L9/12/16; read candidate L415–426 against original L407–419.
- **Disposition:** Standing (the port's credit form and the restored box). The FIX4-LICENSE restoration is checker-verified per the ledger's frame-wave record (section 12).

### 2. Includes and components

- **What:** The candidate's complete include list (grep): the credit pair (L3/L12), the escaped usage include (L18), `:scp-jp:component:image-block` (L24), the license-box pair (L415/L426), and the interwiki-style frame (L433–436). Changes against the original: (a) the iftags tag is localized `+theme` → `+テーマ` (B1, orig L1 → cand L1); (b) the usage include is repointed `:scp-wiki:theme:caretaker-sigma` → `:scp-jp:theme:caretaker-sigma-jp` (INCLUDE-REPOINT; the -jp name form itself was written by the population sweep, Per-theme record); (c) the image-block include is repointed from the bare `component:image-block` to `:scp-jp:component:image-block` (COMPONENT-SWAP span inside B7, orig L28 → cand L24), its name= asset URL unchanged (section 4) and its caption translated; (d) the license-box components are swapped as a pair (section 1); (e) the info pair is deleted (section 1). No `:scp-wiki:` include remains in the candidate (grep: 0). No component port under ruling 4 was needed: image-block and the license box are JP environment components, not theme-specific ports.
- **Why:** P1: foreign-site includes are repointed to the JP site; a same-site usage include takes the candidate's own fullname. P2/T2 (KB-08): iftags conditions name JP tags in the JP environment.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists; `grep -c ':scp-wiki:' candidate.txt` = 0.
- **Disposition:** Standing; no foreign include is kept, so KB-15/KB-54 do not engage.

### 3. Delivery and code loading

- **What:** Both sides deliver the stylesheet out of the page's own code exhibit: the exhibit is each side's only `[[code]]` block, so it is local--code /1 on both sides (orig L141–401; cand L137–412). The original loads that /1 twice: the head frame's theme= URL (orig L5, scp-wiki.wdfiles.com) and the tail module's @import (orig L423, same host). The candidate loads it twice in the same two roles, consolidated at the tail: the tail module's @import (cand L431) and the frame's theme= (cand L435) both name the candidate's own /1 on the draft host (sigma10-jp-test.wdfiles.com) (DELIVERY-HOST B51, SELF-DELIVERY B52, DRAFT-HOST spans). The frame's position moved from the head (orig L3–6) to the tail in the creation commit itself; the original already kept its tail module outside the gate, and the candidate's frame and module both sit after `[[/iftags]]` (cand L428). The frame's one parameter defect: the original carries `priority=1` (orig L4), the creation shipped the frame without it, and FIX4-LICENSE restored it (cand L434). Before that fix the render walk recorded the frame rejected outright (section 12). Priority 1 is the standalone value: the theme has no base layer to order against, it matches the original's own value, and the localize row names it as what "every JP port precedent" carries.
- **Why:** P4/T9: deliveries are served from JP-side hosts in this environment, and a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. P6/KB-07: an interwiki-style frame without `priority` is rejected, which is why the missing parameter was a port defect and not a style point (ledger (c2), FIXED by FIX4-LICENSE).
- **Verify:** `grep -n '\[\[code' candidate.txt` (one block, L137) against the two /1 references (cand L431, L435); read original L3–6 against candidate L433–436 for the priority line's history, and `git show c2a8bee -- pages/theme:caretaker-sigma-jp.txt` for the restoration itself.
- **Disposition:** The draft-host pair is class (iii) draft form, recorded in section 11. The priority restoration is FIXED (ledger (c2)).

### 4. Fonts and assets

- **What:** The original imports two display faces from api.fonts.coollabs.io (orig L142–143: Fredericka the Great, Delius Swash Caps). The candidate imports three stylesheets from fonts.googleapis.com at the exhibit's head (cand L138–140, FONT-IMPORT + JPFONT-LOAD spans inside B46): Noto Sans JP (400;700) added, and the two original faces repointed to the canonical host with their families and display=swap unchanged. All three imports were already in this form at creation. The stacks: the original's rules name the two Latin faces with generic fallbacks (orig L161, L169, L293, L304) and are carried verbatim; the JP fallback arrives as an appended block at the exhibit's end (cand L399–411, the block the classifier labels RESTORATION): a porter comment (section 10) and one rule grouping h1–h6, #page-title and .meta-title under `"Delius Swash Caps", "Noto Sans JP", cursive`. That rule's side effect on the page-title face is flagged in the Per-theme record. Assets: three image URLs are byte-identical to the original, all on scp-wiki.wdfiles.com local--files of the EN theme page — feesh.png (image-block name=, cand L24), carebody.png (cand L143), AEEDLogoWhite.png (cand L147). They are the T1 checker's three hotlink errors (section 12).
- **Why:** P7/T5 (KB-16): Japanese heading text needs a JP typeface loaded and present in the stack; the theme is standalone, so no base loads one. P5/KB-17 (patterns 9c5e907): Google Fonts is on the allowed hotlink list and api.fonts.coollabs.io is not, so the two faces moved to the canonical host. The three images are the opposite case: re-hosting them is a posting-procedure act, class (ii), so the candidate keeps the original-state hosts (KB-58 deferred hosting; the campaign's owner order bars re-upload).
- **Verify:** `grep -n 'fonts.coollabs\|fonts.googleapis' candidate.txt` (coollabs absent; three googleapis imports at L138–140); `grep -n 'local--files' candidate.txt` (exactly L24, L143, L147); read candidate L399–411 against original L297–306 for the appended block's shape.
- **Disposition:** Fonts FIXED in the port itself (no ledger charge was needed; the localize row's pattern-5 item is the asset side). Assets DISPOSITIONED (ledger (c3): P5, class (ii) / KB-58).

### 5. Header, sidebar, site furniture

- **What:** No P8/P9 signature fired, and direct reading agrees there is no variable layer to adapt: the theme sets no `--header-title`/`--header-subtitle` variables on either side. Its header text lives in CSS `content:` strings, carried byte-identical (equal lines, so no change blocks): `content: 'SCP Foundation'` (orig L160 → cand L157), `content: 'Anomalous Entity Engagement Division'` (orig L167 → cand L164), and the responsive shortenings `'Engagement Division'` (orig L378 → cand L375) and `'AEED'` (orig L398 → cand L395). The sidebar, top-bar, login-status and search rules are byte-preserved inside the exhibit, including the mobile `.open-menu a` rule (orig L381–385 → cand L378–382). The one furniture-adjacent change is the font block's effect on #page-title, flagged in the Per-theme record.
- **Why:** The strings are the work's own names (the Foundation's name and the division's name, in the division's own theme); ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57, patterns 9c5e907). P8 layout adaptation is owed only where the JP furniture's structure differs; nothing in the copied rules contradicts the JP Sigma-10 layout, and the render walk's only header finding for this theme was the frame rejection (section 12).
- **Verify:** `grep -n "content: '" original.txt candidate.txt` and compare the four strings; read orig L381–385 against cand L378–382.
- **Disposition:** DISPOSITIONED in effect (header language, ruling 2); the localize row for this theme raised no P8/P9 item.

### 6. Text translation

- **What:** The sample body is retained entire and translated in place, which is where most of the 45 translation blocks sit: 19 TRANSLATION-ANCHORED blocks (one-to-one pairs: the collapsible labels and heading samples B11/B12, the tab labels B13–B16, the repeated tabview lines B31–B39, the table B43, the section headings B44/B45) and 26 TRANS-UNANCHORED blocks (the tabview's repeated "There's a fair many lines here." lines B15–B30, each rendered ここにはかなりの行数があります。, the blockquote lines B40–B42, and single prose lines). The introduction (orig L18–24) is carried nearly whole: heading (cand L14), the author sentence with its hub link (cand L16, section 7), the usage line (cand L18) and the instruction sentence (cand L20). The info module's placeholder text has no counterpart because the module itself was removed (section 1). In-CSS text: the header `content:` strings stay in English (section 5); the appended block's comment is Japanese porter text (section 10, COMMENT-TEXT span). The one residue block (B8, orig L30 → cand L26) is the section heading `+ Examples` → `+ 例`, resolved here: it is a plain P10 heading translation the classifier left open only because the heading token changed language.
- **Why:** P10: body, usage and sample text are translated; terminology follows the JP form of the work's names (Caretaker Theme（Sigma版）). Translation by one-to-one line replacement is the shape that keeps the follow-up diff applicable (localize.md's closing rule), and this theme is the clean case of it: the sample body's structure is untouched.
- **Verify:** Read original L30–137 against candidate L26–133 line by line; the tabview repetition count matches (orig L59–88 ↔ cand L55–84).
- **Disposition:** Standing (the port itself). The localize T5 pass judged this theme's text jointly with T4 and raised no text item beyond the pattern findings (section 12).

### 7. Links

- **What:** No LINK-REPOINT signature fired, but two link changes are in the bytes. (a) The hub link: the original's prose links the division hub by bare fullname, `[[[anomalous-entity-engagement-division-hub|Anomalous Entity Engagement Division.]]]` (orig L20); the candidate links the same EN hub by full URL, labeled 異常存在接触部（AEED、英語版）(cand L16). The hub has no JP counterpart page, so the link keeps its EN target with the （英語版） marking — the same form the campaign dispositions for decom-dept's P11 items (sibling / batch-posting class). (b) The visited-link exhibit `[[[theme:caretaker-sigma|Visited link.]]]` is kept with its target unchanged and its label translated (orig L35 → cand L31): it is a styling specimen whose target is the original's own page name, exactly as in the original. The credit block's source link (cand L11) is the required ruling-3 back-reference to the EN original.
- **Why:** P11 repoints links to JP counterparts where a counterpart exists; where none exists, the EN target is kept and marked, which is the failure P11 exists to prevent (a reader sent to a dead JP fullname) avoided by the marking rather than by a repoint.
- **Verify:** Read orig L20 against cand L16; `grep -n 'anomalous-entity-engagement' candidate.txt` (one hit, the marked EN link).
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** Inside the exhibit, the closing rule is honored in full: every rule of the original's stylesheet survives in the same order (the topology pass finds no relocation, and the exhibit stays a code exhibit rather than being inlined), and the one JP correction block is appended at the exhibit's end (cand L399–411), not interleaved. The four EXHIBIT-RESTRUCTURE primaries adjudicate as: B2, the head rework (head frame out, credit block in — sections 0–1), not an exhibit change; B7, the image-block include repoint inside an exhibit line (section 2); B49/B50, the license entries' reformat from the original's blockquote form to the JP list form inside the restored box (section 1) — content preserved, form changed. Exhibit decisions proper: the sample body is RETAINED and translated (section 6), the opposite choice from themes that drop it, so no R3 drop needs a ground here. Two small furniture changes ride along: the source-code collapsible gains show/hide labels (orig L140 bare `[[collapsible]]` → cand L136 with ソースコードを表示 / 閉じる）, the translation of the exhibit's own furniture; and the `[[footnoteblock]]` deletion is not an exhibit decision — it is a functional drop, flagged in the Per-theme record.
- **Why:** Residue class R3: a sanctioned exhibit replacement and a silent deletion have the same diff shape, so each block's ground is stated. The structural preservation itself is localize.md's closing rule: variable names, selectors and channel order are the original's, so a follow-up diff against a future upstream revision still applies.
- **Verify:** `grep -n '\[\[toc\]\]\|tabview\|image-block' candidate.txt` against original L28–117 (all present); read candidate L134–137 against original L138–141 for the collapsible.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** none — the classifier counts 0 whitespace-only blocks and 0 re-indentation blocks over 52 change blocks. Every changed line carries content.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; here the ground for "none" is the classifier count above.
- **Verify:** classification.json (summary: reindent_blocks 0; no WS-ONLY label in the label counts).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The skeleton prints none for this section because the ANNOTATION signature did not fire, but direct inspection finds one, riding inside B47: the appended font block opens with a two-line Japanese CSS comment (cand L399–401, `/* ===== SCP-JP ローカライズ補正（原語版への追記） ===== */` and its explanation line) announcing that the block is an SCP-JP localization correction appended to the original. It is porter-visible only (inside the CSS exhibit). The candidate contains no `[!-- ... --]` wikitext comments (`grep -c '\[!--' candidate.txt` = 0). This is also the COMMENT-TEXT label's one firing.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; the comment is in fact good practice (it marks the supplement as a supplement, which is what lets section 4's adjudication be made from the bytes), and it is recorded here so the record is complete.
- **Verify:** Read candidate L399–401.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The three EN asset URLs (cand L24, L143, L147): T1 hotlink ×3, DISPOSITIONED class (ii) — posting-time re-hosting; re-upload is barred by owner order and deferred hosting is the recorded state (GOSIGN2-LEDGER (c1) hotlink entry; (c3) P5, KB-58). (2) The T1 pseudo-ref ×1: the usage example's self-reference in its baseline form (`:scp-jp:theme:caretaker-sigma`, a page that does not exist under that name), class (ii) at baseline; the population sweep has since written the reference in the candidate's -jp posting form (cand L18), so the item is closed by edit as well as by class. (3) The draft-host delivery pair (cand L431, L435): class (iii) draft form (P4), rewritten at posting; not charged. (4) The header `content:` strings in English: ruling 2 scope (section 5); not charged. (5) The visited-link exhibit's EN target (cand L31): the original's own self-exhibit form, kept (section 7); not charged. Two further items are NOT dispositioned here because no register decides them: the dropped `[[footnoteblock]]` and the appended font block's page-title side effect, both flagged in the Per-theme record for a future editor.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–4); item 5 recorded; the two flagged items stand open as documentation, not as verdict items (the theme's ledger verdict has no OPEN items).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 4 errors / 1 warn / 0 infos; the errors are hotlink ×3 and pseudo-ref ×1 (T1-ROWS row 72; the warn's code is not itemized in the extracted row). Register (c1) dispositions hotlink and pseudo-ref as class (ii). (b) T2/T3 render: FINDINGS — the one candidate-specific defect was the frame's rejection for the missing `priority` parameter, since FIXED by FIX4-LICENSE (commit c2a8bee) and recorded as such in register (c2); the row's closing assessment records no other candidate-specific defect (RENDER-ROWS-1, RENDER-S2-A (EN5)). (c) T4 localize plus follow-up: FINDINGS with 3 display-affecting items (LOCALIZE-ROWS row 67): pattern 6 (the missing priority; FIXED, ledger (c2)/(c3) P6 FIXED, frame waves, checker-verified), pattern 5 (the EN-site hotlinks; DISPOSITIONED (c3) P5), and the frame's presence itself. The follow-up currency check found nothing to follow: the upstream latest is still revision 10, so the follow-up artifact records rev10 → rev10 with no changes (campaign record, `diff-caretaker-sigma-from10.txt`). (d) T5: judged jointly with T4 by the localize lane; no separate text item stands for this theme. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (52 change blocks) and the generator's (diff.md: +144/−137 in 2 hunks); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:caretaker-sigma-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS at the ledger determination ((b) row 67), with the stamp STALE for the sweep reason stated in the Status table.

## Per-theme record

### Wave history, edit by edit

The candidate's current state is the product of four commits, and the wave story is narrower than the register language suggests. (1) Creation, commit 7e07438 (Stage 2 EN5): the whole port as it now stands in structure — credit block (translator field reading SCP-JP), sample body translated in place, font imports already on Google Fonts with the Noto Sans JP load and the appended fallback block, license entries as a bare list under a `+ 画像の出典` heading, the frame at the tail — but without its `priority` parameter. (2) FIX-CREDIT-D, commit 1869877: one line, 翻訳責任者 SCP-JP → AI, the population-wide ruling-3 normalization. (3) FIX4-LICENSE, commit c2a8bee: the theme's substantive wave edit — `| priority=1` added to the frame, and the license entries wrapped in the JP box (the `+ 画像の出典` heading replaced by the backend include, the end include added). The commit's subject names both halves (caretaker-sigma priority restored, KB-07; license-box furniture restored in 7 themes, KB-63). (4) The usage-example sweep, commit b5cb724: one line, the usage include's name written in the -jp posting form (cand L18).

### Record notes — where the registers understate or misstate this file

Two record-vs-bytes points, both stated so a reviewer is not misled. (a) The ledger's (c3) line for this theme names only two outcomes (P5 DISPOSITIONED; P6 FIXED) and never mentions the license box; a reader of (c3) alone would conclude the box was always in its JP form. It was not: the box wrapper is a FIX4-LICENSE restoration, visible in the commit and in register (c2)'s FIXED entry's commit hash. The (c3) register records pattern outcomes, not commit contents; the git record decides. (b) Register (c4)'s KB-06 entry says caretaker-sigma's triage was "closed by their KB-07b priority fixes (FIX4-IWB, FIX4-LICENSE)" — two wave names for the closure family across the triage set (bloodraven, caretaker-sigma, skipos). This file's own history contains no FIX4-IWB commit; its priority fix is FIX4-LICENSE only. The outcome (FIXED) is correct; only the wave attribution is collective.

### Record conflict — the sources.tsv note for this row

sources.tsv's notes column for this theme states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-caretaker-sigma-from10.txt` (kind K5a-i). The artifact records the opposite: `rev10 → rev10 変更: なし` (no changes), with an empty intervening-revision list. There is no post-reference delta to classify and no supersession. The note is a population-level convention in sources.tsv (the same shape the ambrose-chapter-two package records for its own row); for this row it does not survive contact with its own citation, and this package follows the artifact.

### Flag 1 — the dropped [[footnoteblock]]

The original places `[[footnoteblock]]` at orig L404, between the code exhibit and the license box; the sample body's footnote (`[[footnote]]This is a footnote.[[/footnote]]`, orig L127) renders there. The candidate keeps the footnote (cand L123) and drops the block: `grep -n 'footnoteblock' candidate.txt` finds nothing. The classifier does not surface the drop as its own block — the differ pairs orig L404 with the license-box-backend line (B48) — and no register charges it: the render row records "no other candidate-specific defect" and the ledger passed the theme with no OPEN items. It is recorded here as a flag, not a disposition: the footnote's text has no render position in the candidate, and a future editor should decide whether the omission was a deliberate exhibit trim (the block sat outside the sample body proper, in the page's furniture zone) or an accident of the head/tail rework. This package does not edit the candidate.

### Flag 2 — the font supplement overrides the page-title face

The appended P7 block (cand L402–411) groups its selectors as `h1, h2, h3, h4, h5, h6, #page-title, .meta-title` under one stack, `"Delius Swash Caps", "Noto Sans JP", cursive`. The original gives #page-title/.meta-title their own face — `"Fredericka the Great", serif` (orig L290–295), which the candidate's exhibit still declares (cand L287–292) — but the appended rule comes later in the same stylesheet at equal specificity for those two selectors, so the title's effective font-family is the Delius stack, not Fredericka with a JP fallback added. The JP fallback the supplement exists to provide is thus bought, for the title, by changing the title's Latin face. No register charges this (the localize row's pattern items are 5 and 6; the render walk records no title-face finding), and the theme's headings proper (h1–h6) are unaffected in kind (their stack gains exactly the intended fallback). Recorded with the cascade evidence so the judgment is visible; the minimal alternative, a separate appended rule for #page-title/.meta-title naming Fredericka first, is noted for a future editor.

### Post-package repairs (REFRESH3-F)

**FIX-CARETAKER, landing `ba896f4` (report `R/review-scout/FIX-CARETAKER.md`,
items 1–2, "caretaker-sigma-jp").** This landing postdates the package
build (`0533657`, the U-4 batch commit) and repairs Flags 1 and 2. Two
candidate changes: (a) `[[footnoteblock]]` restored after
`[[/collapsible]]` and before
`[[include :scp-jp:component:license-box-backend]]`, with the original's
blank lines around it (+2 lines, plain form, license apparatus
untouched) — the live `[[footnote]]` at candidate L123 now has a render
position; (b) `#page-title` and `.meta-title` removed from the appended
P7 block's selector group, which now reads `h1, h2, h3, h4, h5, h6 {`
with its declaration unchanged (3 lines in the one rule header) — the
theme's own rule at candidate L287–292 again decides the title face
(`"Fredericka the Great", serif`), as in the original, whose cascade
never put those two selectors in the Delius stack. Checker per the
report: error 4 / warn 1 / info 0 before and after, findings identical
line for line, class (i) errors 0. This package documents the corrected
candidate; its stamp reads STALE against the pre-repair verdict, by
design.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-caretaker-sigma-jp.txt` — the render sample page (an include of the candidate and of the shared `theme-decoration-sample`); it is the "sample" the T2/T3 checks rendered alongside the candidate page. (2) `pages/theme:caretaker-sigma.txt` — the repo's EN-side copy of the original page, the EN sample's base. (3) The delivery itself: the candidate's own local--code /1 on the draft host, named by the tail module and the frame (cand L431, L435), which is the runtime form of the self-delivery; the original side's /1 was the same exhibit on scp-wiki.wdfiles.com.

## Multi-wave provenance

The candidate's current state is the product of the S2 port and three later touches, not a single pass: the EN5 creation (commit 7e07438) did the translation, the credit furniture swap, the font repoint and supplement, and the tail consolidation, and shipped the frame without its priority; LOCALIZE-S2-A then examined that state and charged patterns 5 and 6 (its row is LOCALIZE-ROWS row 67); the render walk (RENDER-S2-A, EN5) caught the frame rejection the source checks had only warned about; FIX4-LICENSE (commit c2a8bee) repaired the priority and restored the license-box wrapper in one commit; FIX-CREDIT-D (commit 1869877) had already normalized the translator field; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. The only later change is the documentation-pass era's own: the usage-example sweep (commit b5cb724) wrote the usage include in its -jp posting form, which is why the generated stamp reads STALE. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 67, (c2) caretaker-sigma entry, (c3) caretaker-sigma entry, (c4) KB-06 entry; GOSIGN2-LEDGER-SUPPLEMENT.md (no caretaker-sigma entries); T1-ROWS row 72; LOCALIZE-ROWS row 67; RENDER-ROWS-1 (RENDER-S2-A) caretaker-sigma row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted one residue block; it is resolved, and no new signature is required.

- **R1 — B8 (residue; orig L30 → cand L26, body → body).** The sample body's section heading, `+ Examples` → `+ 例`. Resolved in section 6 as a plain P10 heading translation; the classifier left it open only because a one-word heading offers no anchor token in either language.

## License and attribution

- **Title:** Caretaker Theme (Sigma Version)
- **Author:** winkwonkboi
- **Source:** https://scp-wiki.wikidot.com/theme:caretaker-sigma — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
