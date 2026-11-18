# Review package — theme:helix-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:helix-jp — origin EN, population #96 [GOSIGN2-LEDGER (b) row 96]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 96]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 1 warn / 0 infos (hotlink×11); standing classes dispositioned in register c1 [T1-ROWS row 106; GOSIGN2-LEDGER (b) row 96]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — header gear logo clipped at left ≤768 both engines; credit-modal heading white-on-yellow ≈1.4; WebKit CC "S"; i57logo 503 = EN11 deferred host. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 96, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 96]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 96]
- Computed against: canonical commit f931619f42a4bfbf6f0962b6c0756217e6991c58; candidate file pages/theme:helix-jp.txt sha256:35f12589947c563bc91fb929f462499dd26e77c705bb76ebcb6e1f2e2ae696b4; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/helix-jp/candidate.txt (sha256 35f12589947c563bc91fb929f462499dd26e77c705bb76ebcb6e1f2e2ae696b4)
Original: theme:helix — scp-wiki, revision 11 (sha256 778cdc2ff3bb1b8c111645fa9119f1a150fde67f2d7cc3dbdbfe6415af6f68e4)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 96); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no helix entries |
| Fixed after the localize check | P6 (interwiki-style frame), landed inside commit f931619 (FIX2-COLON) together with the KB-01 colon encoding and the ruling-3 translator normalization |
| Standing items | **DISPOSITIONED** — T1 hotlink×11, class (ii) (ledger (c1)); localize P5 EN-storage header/HUD/logo assets, class (ii) / KB-58 (ledger (c3)); render findings: header gear logo clipped at left ≤768 in both engines (KB-35 family), WebKit CC "S" (KB-36), the credit-modal heading contrast on the preview form (KB-32), and the i57logo 503 on the EN11 deferred host (KB-58) (ledger (c2)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:helix | theme:helix-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 11, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 11 | — |
| Source of this copy | Campaign mirror store `orig-helix-rev11.txt` (class COPY, byte-identical; review/sources.tsv) | Canonical file `pages/theme:helix-jp.txt`, created in commit a869415 (Stage 2 EN11); its only later commit is f931619 (FIX2-COLON, last content change) |
| Lines / bytes | 482 lines / 13,614 bytes | 794 lines / 22,601 bytes |
| SHA-256 | 778cdc2ff3bb1b8c111645fa9119f1a150fde67f2d7cc3dbdbfe6415af6f68e4 | 35f12589947c563bc91fb929f462499dd26e77c705bb76ebcb6e1f2e2ae696b4 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; standalone base). No production counterpart was adopted: the candidate's CSS body measures 0.98-similar to the original's own code exhibit (classifier topology pass). The localize follow-up records no unincorporated upstream updates for this theme.

## Summary

The original is a small BHL-era theme whose live delivery address is defective in the original itself: its module CSS @imports `https://scp-wiki.wdfiles.com/local--code/theme:helix` with no fragment number (orig L1–3), while the real stylesheet sits in the page's code exhibit (orig L157–473). The candidate inlines the exhibit into its module CSS (cand L7–323), and the module copy and the retained exhibit copy are byte-identical (315 content lines each, measured similarity 1.0), so the page's own /1 — which the population audit (FIX-CODEADDR) probes as MATCH, serving 7,699 B of this CSS — and the inline carry the same body. The candidate's one later commit, FIX2-COLON, did three things beyond its named scope: it added the interwiki frame the creation commit lacked (the P6 fix), colon-encoded the two logo URLs in both copies, and normalized the translator field to AI. The rate/info exhibit block at the original's head (orig L7–18) was dropped as furniture for modules the JP environment replaces. The theme passed with no open items; its 11 T1 hotlink errors are the 11 EN-storage asset lines, dispositioned class (ii).

## Classification

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 3 |
| WS-ONLY | 3 |
| COLON-ENC | 2 |
| DELIVERY-MOVE | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| INFO-DEL | 1 |
| RESTORATION | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Counts: 9 blocks — 8 specific (88.9%), 1 heuristic (11.1%, B9, resolved in the Appendix), 0 residue, 0 skipped. Topology: the original's code exhibit (orig L157–473) moved to the candidate's module-css (cand L7–323) at 0.98 similarity; the candidate-side own-delivery companion body was unavailable to the classifier (its recorded caveat), and this package supplies the missing comparison directly: the candidate's module copy and exhibit copy are byte-identical. Labels are sets per block; this README's sections were written from classification.json's label spans, not from the skeleton's per-section lists (the skeleton's sections 1, 2 and 4 print "none" although credit, include and delivery labels fired inside blocks whose primaries sit elsewhere).

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with its delivery module (L1–3, the fragment-less @import), the `[[iftags +theme]]` gate (L5) and the rate/info exhibit block (L7–18, section 8). The candidate opens with the interwiki frame (cand L1–4), the localized gate (L6) and the inlined module (L7–323). The frame was not part of the creation commit; it arrived in f931619 (section 3, Per-theme record item 1). Provenance route: derived from the original at reference revision 11 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P4/P6 rework exactly this frame for the JP environment.
- **Verify:** Read original L1–6 against candidate L1–7; `git show a869415:pages/theme:helix-jp.txt | head -6` (no frame) against the current head.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original carries no credit block; its attribution is prose: the intro credits the theme's coding to tiredsn0w and the logos to tiredsn0w plus an anonymous non-Wiki personnel, and the head exhibit block (orig L7–18) samples the info module rather than instantiating it. The candidate adds the preview credit block (cand L325–334): `:scp-jp:credit:start-preview` / `end-preview` with all eight ruling-3 fields — title HELiXテーマ, translator AI, translation year 2026, original title "HELiX", copyright holder tiredsn0w, creation year 2026, reference revision 11, and the source link to the EN page. The author field agrees with the original's prose credit; the anonymous logo co-credit cannot be named in a field and is carried in the translated prose, which preserves it. The theme's own credit-module CSS is inherited from the original's stylesheet (T7-CREDIT-CSS by inheritance, one set in the single CSS body the candidate carries twice). No license box exists on either side, and none was charged (KB-63 covers dropped boxes; this original never had one). No live bare `[[module Rate]]` exists in the candidate; the original's only Rate is inside the dropped exhibit block (section 8).
- **Why:** P3/T1: the preview credit module is the JP environment's credit form and it is rate-bearing (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields and credits campaign translations to AI; f931619 normalized this file's translator field from SCP-JP to AI under that ruling.
- **Verify:** Read candidate L325–334 against the eight-field list and the original's intro prose (orig L20–40 region); `grep -n 'module Rate' candidate.txt` (absent).
- **Disposition:** Standing (the port's credit form); the localize lane verified the credit form and charged no credit item.

### 2. Includes and components

- **What:** The candidate's include list (grep): the interwiki-style frame (L1–4), the credit pair (L325/L334), the escaped usage include (cand L353: @@[[include theme:helix-jp]]@@, the bare same-site form; the original's exhibit read @@[[include:scp-wiki:theme:helix]]@@ at orig L40), and `component:image-block` repointed to `:scp-jp:` (cand L429; INCLUDE-REPOINT). The image-block's `name=` parameter still carries the full EN wdfiles URL of DR_logo.png: the parameter names the image file the exhibit displays, the file lives in EN storage, and re-hosting it is the same class (ii) act as the other EN assets (section 4). No `:scp-wiki:` include remains live in the candidate.
- **Why:** P1: foreign-site includes are repointed to the JP site, and a same-site include takes the bare fullname form. Ruling 4 does not engage: image-block exists on the JP site.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; the DR_logo.png parameter is part of the P5 dispositioned asset set (section 11).

### 3. Delivery and code loading

- **What:** The original's delivery is a single module CSS (orig L1–3) @importing `https://scp-wiki.wdfiles.com/local--code/theme:helix` — an address with no fragment number, so as written it names the page's code-delivery root rather than any block; the stylesheet's actual text is the code exhibit (orig L157–473). The candidate delivers the same body two consistent ways: inlined in the module CSS (cand L7–323; topology code-css → module-css at 0.98), and as the page's own /1 named by the interwiki frame (cand L1–4: `:scp-jp:component:interwiki-style`, priority=1, theme= the candidate's own /1 on the draft host sigma10-jp-test.wdfiles.com; labels SELF-DELIVERY + DRAFT-HOST). The two candidate copies are byte-identical (module L7–323 and exhibit L469–785, 315 content lines each), so the channels cannot diverge. The population audit (R/review-scout/FIX-CODEADDR.md) classes helix-jp /1 as MATCH: the probe served 7,699 B of this theme's CSS, i.e. the named block is the block that holds the CSS. The frame itself is a FIX2-COLON addition: the creation commit had no frame at all, which is what the localize lane charged as P6 ("translation module absent", display-affecting).
- **Why:** P4/T9: deliveries are served from JP hosts, and the draft-host form of a candidate's own local--code is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. P6: a theme page in the JP environment carries the interwiki-style frame so its code delivery resolves under the JP site's theme machinery; its absence at creation was a real gap, fixed in f931619.
- **Verify:** Read orig L1–3 against cand L1–4 and L7; `diff <(sed -n '8,322p' candidate.txt) <(sed -n '470,784p' candidate.txt)` (the two copies, empty diff); FIX-CODEADDR.md's helix-jp row (MATCH).
- **Disposition:** The draft-host URL at cand L3 is class (iii) draft form, not charged. P6 FIXED (ledger (c3), recorded there under "frame waves"; the bytes sit in FIX2-COLON, see Multi-wave provenance).

### 4. Fonts and assets

- **What:** No font @import exists on either side and no font supplement was needed or added: the theme's stacks are BHL's, and no P7 item was charged for this theme. Assets: the candidate's EN-storage lines are the header, HUD and logo images (HELiXthemeHeader.png and HELiX.png among them) on scp-wiki.wdfiles.com in both CSS copies, plus the DR_logo.png exhibit parameter (section 2) — 11 lines in total, which are the T1 checker's 11 hotlink errors. FIX2-COLON colon-encoded the two logo URLs in both copies (`theme:helix` → `theme%3Ahelix`, 4 lines, label COLON-ENC, KB-01).
- **Why:** P5/KB-58: the assets are the theme's own artwork in EN storage; re-hosting them is a posting-procedure act, class (ii), so the candidate keeps the original-state hosts. KB-01: unencoded colons in local--files URLs break under the JP host's URL handling.
- **Verify:** `grep -n 'scp-wiki.wdfiles.com' candidate.txt` (11 lines); `git show f931619 -- pages/theme:helix-jp.txt` for the four colon-encoded lines.
- **Disposition:** DISPOSITIONED (ledger (c3): P5, class (ii) / KB-58; ledger (c1): the hotlink class is (ii)).

### 5. Header, sidebar, site furniture

- **What:** The theme's header and HUD rules are byte-preserved inside the moved body; its furniture is BHL's with the theme's own header artwork (section 4). No header-variable strings are redefined by this theme, and P9 was not charged. The render row's furniture findings are the ≤768 left clip of the header gear logo (both engines) and the WebKit CC "S" item, both cross-cutting families (section 11).
- **Why:** P8 layout adaptation is owed only where the JP furniture's structure differs; the localize lane raised no P8 item for this theme, and ruling 2 places header language outside migration correctness in any case.
- **Verify:** The moved body comparison in section 3; RENDER-ROWS-1 row for this theme.
- **Disposition:** Standing; no furniture item was charged in any register.

### 6. Text translation

- **What:** The intro prose, the usage text and the exhibit headings are translated in full, including the credit prose (the tiredsn0w and anonymous-personnel credits survive in Japanese). The classifier's TRANS-UNANCHORED blocks (3) are this prose mass. In-CSS text: the stylesheet's comments stay in English (residue class R1, porter-visible only); the CONTENT-STRING firing is the theme's own CSS string content, carried as defined. The localize T5 pass found no untranslated body paragraph; the one prose loss is the Sigma-10 reference: the original's sentence links the Sigma-10 theme page, and the translation carries the words as plain text (section 7).
- **Why:** P10: body and usage text are translated. The classifier's TRANS-UNANCHORED label is the honest one for translation without line anchors, and the localize pass is the check that covers it.
- **Verify:** Read orig L20–155 against cand L336–467; LOCALIZE-ROWS row 96 (no T5 item charged).
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The footer wikiwalk (orig L479 → cand L791, the heuristic block B9, resolved in the Appendix) holds the theme's link decisions: the "Altitudes Hub" wikilink became an explicit EN URL (no JP counterpart page exists); the middle link's title text is translated while its target likewise stays the EN page; the "State of Kepler" theme wikilink became plain text, "State of Keplerテーマ" (no JP page exists, so a wikilink would be a dead target). In the body, [[[SCP-6118]]] likewise became a full EN URL, and the original's Sigma-10 theme link became plain text in translation. The credit block's source link (cand L333 area) is the required ruling-3 back-reference to the EN original.
- **Why:** P11 repoints links to JP counterparts where they exist; where none exists, an explicit EN URL keeps the link working and plain text avoids a dead wikilink. Both forms appear here, chosen per target.
- **Verify:** Read orig L477–482 against cand L789–794; `grep -n 'scp-wiki.wikidot.com' candidate.txt` and sort the hits by role (assets in section 4, links here).
- **Disposition:** Standing; no link item was charged for this theme in any register. The Sigma-10 plain-texting is recorded above as an observation, not a flag: the sentence's information survives, only the link is gone.

### 8. Structure

- **What:** Two structural decisions. (a) The stylesheet's relocation (section 3) preserves rule order (0.98-similarity move), and the exhibit is retained whole (cand L469–785). (b) The head exhibit block is dropped (orig L7–18, INFO-DEL/EXHIBIT-RESTRUCTURE mass at the file head): a `[[>]]` block sampling `[[module rate]]`, `info:start`/`info:end` and `info:start-standalone`/`info:end-standalone` — documentation samples of the EN furniture modules, not live furniture (the Rate inside it never rendered as the page's own rating device; it sits inside an exhibit div). The candidate's live credit form is the preview credit block (section 1). The localize lane, which itemized this theme's defects, charged only P5 and P6; the exhibit block's drop was visible to it and uncharged.
- **Why:** Residue class R3: a sanctioned exhibit replacement and a silent deletion have the same diff shape, so the ground is stated. The samples document modules the JP environment replaces with the credit module; keeping EN info-module samples as the page's head furniture would misdocument the JP form.
- **Verify:** Read orig L7–18; confirm no counterpart exists in the candidate (`grep -n 'info:start' candidate.txt`, absent).
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** 3 of the 9 blocks are WS-ONLY; the classifier counts 0 re-indentation blocks. Brace balance, checked by depth with comment- and string-awareness: every channel (the original's module and exhibit; the candidate's module and exhibit) ends at depth 0 on both sides.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; the depth check exists because a displaced closing brace keeps the counts equal while swallowing every later rule.
- **Verify:** classification.json (3 WS-ONLY blocks, reindent_blocks 0); the depth figures are reproducible by scanning each [[module CSS]] / [[code]] channel of the two files.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none — no signature fired, and direct inspection agrees: the candidate contains no `[!-- ... --]` translator notes (`grep -c '\[!--' candidate.txt` = 0). The only added text with no original counterpart is the frame, the credit block and the translated prose, each accounted for in its own section.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here the ground for "none" is the grep above.
- **Verify:** The grep in What.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The 11 EN-storage asset lines: T1 hotlink×11, DISPOSITIONED class (ii) (GOSIGN2-LEDGER (c1) hotlink entry; (c3) P5, KB-58). (2) The header gear logo clipped at the left at ≤768 in both engines: DISPOSITIONED as the narrow-width header clip family (ledger (c2), KB-35 family). (3) The credit-modal heading contrast (white on yellow, ≈1.4) on the sample: DISPOSITIONED as a property of the preview credit form, not of this theme (ledger (c2); KB-32; the 2026-11-16 ruling that credit-modal behaviour on preview-module pages belongs to the preview form). (4) WebKit CC "S": DISPOSITIONED, cross-cutting (KB-36). (5) The i57logo 503 in the render capture: DISPOSITIONED as the EN11 deferred-host state (KB-58). No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–5).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 11 errors / 1 warn / 0 infos; all 11 errors are hotlink, the section 4 asset lines (T1-ROWS row 106). Register (c1) dispositions the hotlink class as (ii). (b) T2/T3 render: FINDINGS, all items dispositioned in (c2) (section 11, items 2–5); engine coverage is the lane's full matrix as run (RENDER-ROWS-1, RENDER-S2-B). (c) T4 localize plus follow-up: FINDINGS with 2 display-affecting items (LOCALIZE-ROWS row 96); outcomes P5 DISPOSITIONED / P6 FIXED (ledger (c3)). (d) T5: judged jointly with T4; no mistranslation or untranslated-body finding. (e) Delivery probe: FIX-CODEADDR classes this theme's /1 as MATCH (7,699 B served). (f) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (9 change blocks) and the generator's (diff.md: +476/−164 in 7 sections); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:helix-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 96).

## Per-theme record

### Item 1 — wave attribution: the frame fix rode inside FIX2-COLON

Ledger (c3) records this theme's P6 outcome under the frame waves. The file's history is two commits (a869415 creation, f931619 FIX2-COLON), and the frame's addition is in f931619's diff, alongside its named colon-encoding scope and the ruling-3 translator normalization. The creation commit's lack of a frame is exactly what the localize lane charged (P6, "translation module absent"), so the fix's location is decidable from the bytes: it is in FIX2-COLON. The bytes are right; the record's wave name is wrong for this theme. The same pattern (a FIX2-COLON commit carrying a fix its subject does not name) recurs across this batch and in the ambrose package's FIX-CREDIT-D.

### Item 2 — the original's own delivery address is incomplete

The original's module @imports the local--code root with no fragment number (orig L1–3). Whatever that address served on the EN wiki, it is not a well-formed delivery of the exhibit block; the port's answer (inline the body, name /1 in the frame) is the population's standard form and the audit's probe confirms /1 serves this CSS (section 3). Recorded as an original-side defect the port silently corrected, as EN-author report material; no JP-side action follows from it.

## Change set outside the two diffed files

None for this theme: no other canonical file carries part of this port. The one wave commit is a shared vehicle — f931619 (FIX2-COLON) touched 18 theme files; this file's hunks in it are narrated in sections 3–4 and in Multi-wave provenance.

## Multi-wave provenance

| Commit | Wave | What it changed in this file |
|---|---|---|
| a869415 | Stage 2 EN11 creation | The whole port: the exhibit inlined into the module CSS, the credit block added, the rate/info exhibit block dropped, the body translated, the usage include rewritten to the bare -jp form, image-block repointed. No interwiki frame (the P6 gap the localize lane then charged) |
| f931619 | FIX2-COLON | The interwiki frame added at the head (the P6 fix, item 1); colon encoding `theme:helix` → `theme%3Ahelix` in the HELiXthemeHeader.png and HELiX.png URLs in both copies (KB-01); the credit block's translator field normalized SCP-JP → AI (ruling 3) |

## Appendix — heuristic and residue blocks

There are no residue blocks. The one heuristic block:

- **B9** (orig L479 → cand L791, body → body, TRANS-UNANCHORED by shape): the footer wikiwalk. Resolved by reading both sides: the three-link navigation line was translated link by link — the Altitudes Hub target kept as an explicit EN URL, the middle title translated as text, and the State of Kepler target reduced to plain text because no JP page exists for it. The block is the link adjudication recorded in section 7, not untranslated residue. The RESTORATION label on the head blocks is a diff-only signal (added lines matching the original's own regions across the two copies); nothing for this theme was deleted and later restored by a wave.

## License and attribution

- **Title:** HELiX Technologies Theme
- **Author:** tiredsn0w
- **Source:** https://scp-wiki.wikidot.com/theme:helix — revision 11
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
