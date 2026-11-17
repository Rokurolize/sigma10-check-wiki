# Review package — theme:decom-dept-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:decom-dept-jp — origin EN, population #78 [GOSIGN2-LEDGER (b) row 78]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 78]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 0 warns / 1 info (pseudo-ref×5, foreign-include×2); standing classes dispositioned in register c1 [T1-ROWS row 78; GOSIGN2-LEDGER (b) row 78]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-header defect: theme's own gray-dept header logo/site-name collision and 検索 overprint of "財団" at ≤375 both engines (768px clean); 884px@768 sample overflow, notice clip, WebKit CC "S". [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 78, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 78]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 78]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:decom-dept-jp.txt sha256:1d47d8b0facb68ad8c53c1a6597789359f6cd6dc7f84be7e5c64a4f0892640e6; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/decom-dept-jp/candidate.txt (sha256 1d47d8b0facb68ad8c53c1a6597789359f6cd6dc7f84be7e5c64a4f0892640e6)
Original: theme:decom-dept — scp-wiki, revision 187 (sha256 36da011dd46e5fd9d6b8eac1fcf1f2846d1758c605b64a9a18a417976a9f3f98)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 78), and the generated stamp above still reads PASS: the candidate's bytes have not changed since the verdict era (its last change is the FIX2-CREDIT commit the verdict record itself rests on) |
| Wave history | Two commits touch the candidate: the Stage 2 EN7 creation (331ab7e — unusually complete: six credit fields, the font supplement with its license documented in the block, both rating specimens already replaced, and a translator's note adjudicating an original-side inconsistency) and FIX2-CREDIT (666f543 — exactly two lines, the translator and translation-year fields the localize lane found missing). Each is narrated in the Per-theme record |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×5 (class (ii)); the foreign author-label pair (the KB-54 named exception); the candidate-header collision family (KB-35) and the sample overflow family (KB-33/KB-34); P11's （英語版） link markings (sibling / batch-posting class). One item is **flagged**, not dispositioned, by this package: the original's closing `more-by:calibold` include, dropped with no disposition in any register (Per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | This theme is one of the two members of the ledger's named KB-54 exception set (section 2). The sweep's single named exception is theme:amethyst-v2, which has no candidate |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:decom-dept | theme:decom-dept-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 187 (first translation; the candidate's credit block records 初訳時参照リビジョン: 187) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-decom-dept.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:decom-dept-jp.txt`, created in commit 331ab7e (Stage 2 EN7); its last content change is commit 666f543 (FIX2-CREDIT) |
| Lines / bytes | 637 lines / 15,295 bytes (the last line carries no trailing newline, so `wc -l` reports 636) | 633 lines / 16,749 bytes |
| SHA-256 | 36da011dd46e5fd9d6b8eac1fcf1f2846d1758c605b64a9a18a417976a9f3f98 | 1d47d8b0facb68ad8c53c1a6597789359f6cd6dc7f84be7e5c64a4f0892640e6 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted. Reference-revision currency: the follow-up artifact `diff-decom-dept-from187.txt` in the campaign record records rev187 → rev187, no changes, so revision 187 is still the upstream latest; the sources.tsv note for this row says otherwise and is dealt with in the Per-theme record.

## Summary

Decom-dept is a small department theme (637 lines) whose original is unusually self-documenting: it demonstrates both rating forms (a labeled bare Rate and an info-module specimen), wraps its head in an author-label component specimen, documents a pride-logo include parameter its own code never implements, and closes with the author's more-by component. The candidate is the most finished creation in this batch: it arrived with six of the eight credit fields (plus a ninth field documenting its added font and that font's license), both rating specimens already replaced by the preview credit block, the subtitle string translated, and a translator's note that catches the pride-parameter inconsistency and preserves the original's behavior deliberately. FIX2-CREDIT's whole work in this file is two lines. The render charges are the population's narrow-width families, dispositioned. Two record items need a reviewer's care: the kept foreign component pair, which is a named staff exception with its ground restated in section 2, and the one silent drop this package flags — the closing more-by include, which no register mentions.

## Class summary

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 29 |
| TRANSLATION-ANCHORED | 9 |
| DRAFT-HOST | 6 |
| DELIVERY-HOST | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Counts: 51 blocks — 21 specific (41.2%), 27 heuristic (52.9%), 3 residue (5.9%), 0 skipped. The heuristic share is the translated body (TRANS-UNANCHORED ×29). Topology: no relocation; each side's components match by kind (two head modules, one code exhibit). Labels are sets per block; these sections were written from classification.json's label spans. Three adjudications matter. (1) The derived-presence pass reports FOREIGN-KEPT ×2 (cand L33, L43) — the author-label pair, a named exception, not an oversight (section 2). (2) The single CSS-BODY block (B49) is the translated subtitle content string, a rendered-text translation in substance (section 6). (3) The residue set includes the one block no register explains (B51, the more-by drop), resolved as a flag in the Appendix and the Per-theme record.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's frame zone stands outside and above the gate (orig L1–19): a module importing its own /1 (L1–3), a second module carrying the pride-logo header rule (L5–12), the interwiki-style frame (L14–17, `priority=1`, theme= own /1, parameters in the original's unspaced form), then the gate (L19). Inside the gate, the original's head is the rating specimens (orig L21–45). The candidate's frame zone is the same three pieces in the same positions, repointed (cand L1–17), and its in-gate head is the credit block (cand L20–30). Provenance route: derived from the original at reference revision 187 (see Provenance); no R4 adoption.
- **Why:** The frame zone is where this theme declares its delivery and its logo behavior; P1/P4/P6 rework exactly this zone, and each piece is accounted for in sections 1–3 (the pride rule's parameter story is section 10's note).
- **Verify:** Read original L1–19 against candidate L1–17; blocks B1–B5 in classification.json.
- **Disposition:** Recorded; the credit reading is section 1, the delivery reading section 3.

### 1. Credit and attribution

- **What:** The original carries no credit block; its rating furniture is two specimens inside the body — a labeled bare Rate (`**Rating Module:**` over `[[module Rate]]`, orig L21–25) and an info-module specimen (`:scp-wiki:info:start/more/end` around placeholder text, orig L37–45) — and its attribution is the prose sentence (orig L49 zone: created by Calibold) and the author-label specimen (section 2). The creation replaced both specimens with the preview credit block and arrived with six of the eight ruling-3 fields already filled (cand L21–28 zone: title Decommissioning Dept. Theme, original title, copyright holder `[[*user Calibold]]`, creation year 2021, reference revision 187, source link) plus a ninth field of the port's own — **追加フォント:** Noto Serif JP (SIL OFL 1.1, Google Fonts) — documenting the font the port adds and its license, in the block where a reviewer looks for provenance. The two missing fields were exactly the ones the localize lane charged (P3: 翻訳責任者/翻訳年 欠落）, and FIX2-CREDIT (commit 666f543) added exactly those two lines (cand L22–23: translator AI, translation year 2026), nothing else. There is no license box on either side and no per-file license entries to carry.
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing form; the original's two specimens are demonstrations of rating forms, and the JP form replaces both (the Rate's removal is the KB-09 mechanism; the info specimen's placeholder text — "Info about your page." — carries no content to lose, which is what makes its deletion a replacement rather than a drop; section 8). Ruling 3 fixes the eight fields; the ninth field is the port documenting its own addition under the same discipline (its font's license is a TASL fact a reviewer would otherwise have to leave the repo to check).
- **Verify:** Read candidate L20–30 against the eight-field list; `git show 666f543 -- pages/theme:decom-dept-jp.txt` (two added lines, nothing else); `git show 331ab7e:pages/theme:decom-dept-jp.txt` for the creation's six fields and ninth field already present.
- **Disposition:** Standing. The credit completion is FIXED by FIX2-CREDIT (ledger (c3): P3 FIXED, credit waves, checker-verified); the ledger determination then found nothing open (section 12).

### 2. Includes and components

- **What:** The candidate's complete include list (grep): the head frame (bare `component:interwiki-style`, cand L14), the credit pair (bare `credit:start-preview` / `credit:end-preview`, cand L20/L30), the author-label pair (`:scp-wiki:component:author-label-source` start/end, cand L33/L43 — KEPT on the foreign site), the usage self-include in two forms (plain and `|inc-pride= --`, cand L45/L49 zone, bare `theme:decom-dept-jp`), and `component:image-block` (bare, cand L53 zone). Three facts need a reviewer's eye. (a) The author-label pair is the file's only `:scp-wiki:` content (grep count: exactly 2) and it is deliberate: the ledger's (c1) register names this theme's two lines as the KB-54 named exception — the component renders the author's label with the page's own title via the ListPages module it wraps (the specimen between the pair, cand L34–42, is carried and its author-page link repointed, section 7) — and porting the component is a separate staff call (FIX3-S2EN §6.7), not this theme's port. The T1 baseline's foreign-include ×2 errors are these two lines, dispositioned by the same exception. (b) The file's include forms are bare (no site prefix) for the frame, credit pair and image-block — the same-wiki resolution form; the components named exist on the JP wiki under those fullnames, and the checker raises no class against the form. (c) One original include has no candidate counterpart: the closing `[[include :scp-wiki:more-by:calibold]]` (orig L635) — flagged in the Per-theme record. The iftags tag is localized (orig L19 → cand L19).
- **Why:** P1 repoints foreign includes to the JP site; the exception in (a) exists because the component's function (an author label fed by the page's own ListPages) has no JP port and the campaign's ruling was to keep the pair visibly foreign rather than silently drop or silently keep it — the exception is named in the ledger so the keeping is auditable. P2/T2 (KB-08): iftags conditions name JP tags.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare; `grep -c ':scp-wiki:' candidate.txt` (2, the pair); ledger (c1) line for the foreign-include class, decom-dept entry.
- **Disposition:** The pair is DISPOSITIONED (KB-54 named exception, ledger (c1); ledger (c3): P1 DISPOSITIONED). The more-by drop is FLAGGED in the Per-theme record, not dispositioned.

### 3. Delivery and code loading

- **What:** The stylesheet lives in one code exhibit on both sides (orig L150–631 → cand L147–629), so it is /1 on both sides, and the self-delivery addresses are correct (SELF-DELIVERY ×2): the head module @imports own /1 (orig L2 → cand L2, draft host) and the frame names own /1 (orig L16 → cand L16, draft host; DELIVERY-HOST + DRAFT-HOST spans). The frame keeps the original's parameter set and even its unspaced form (`|priority=1`, `|theme=...`): priority 1 is the theme's own layer value (it has no included base; its base furniture arrives with the Sigma-10 environment itself). The second head module (the pride-logo header rule) is carried with its asset repointed to the candidate's own files (orig L8 → cand L8, draft host). No cross-theme @import exists on either side.
- **Why:** P4/T9: a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. P6: the frame's parameter set (priority, theme) is the surviving pair the JP interwiki-style accepts; the unspaced serialization is the original's own and is accepted as-is.
- **Verify:** `grep -n '\[\[code' candidate.txt` (one block, L147) against the two /1 references (cand L2, L16); read original L14–17 against candidate L14–17.
- **Disposition:** The draft-host pair is class (iii) draft form, recorded in section 11.

### 4. Fonts and assets

- **What:** The original's exhibit imports three lines (orig L153–155): Poppins and Roboto Slab from fonts.bunny.net, and Font Awesome from grombald.github.io (the Common-Theme project's host). The candidate imports four (cand L150–153): Poppins and Roboto Slab repointed to fonts.googleapis.com with families unchanged (FONT-IMPORT span), Noto Serif JP added (JPFONT-LOAD), and Font Awesome 4.7.0 from cdnjs.cloudflare.com. The supplement's stack work (JPFONT-STACK): the exhibit's Roboto Slab stacks gain the fallback — `'Roboto Slab', 'Noto Serif JP', serif` (cand L175 and its sibling occurrence) — so Japanese text in the theme's serif contexts has a named JP face; the credit block's ninth field documents the addition and its SIL OFL 1.1 license (section 1). No stack names a face that no import loads, and no import is duplicated. Assets: the theme's two graphics are its own page's files, repointed from the EN page's attachments to the candidate's own on the draft host — DeDPride.png (the header rule, orig L8 → cand L8) and DeDLogo.svg (the image-block, cand L56 zone).
- **Why:** P7/T5 (KB-16): no JP typeface was loaded or named in the original; the supplement is the standard repair, executed at creation here. P5/KB-17 (patterns 9c5e907): Google Fonts and cdnjs are on the allowed hotlink list; fonts.bunny.net and a personal GitHub Pages host are outside it, so all three original lines moved.
- **Verify:** `grep -n '@import' original.txt candidate.txt` (3 lines against 4); read candidate L175 against the original's stack lines; the ninth credit field at cand L29.
- **Disposition:** Standing (the creation's own supplement; no register charges this theme's fonts — the localize row's display-affecting items are P1, P3 and P11, section 12).

### 5. Header, sidebar, site furniture

- **What:** This theme's header is its render charge: the theme's own gray-dept header design collides its logo and site name at ≤375px in both engines, with the 検索 control overprinting 財団 (768px is clean). The candidate's header rules are the original's, carried — including the pride-logo background rule (section 3) — so the collision is the theme's own geometry at narrow widths, not a port edit. The header's text layer: the credit title keeps the work's name (Decommissioning Dept. Theme), and the localize row's T5 item records the header "Decommissioning Dept." and the EN tab labels as kept with a staff-confirmation note; the ledger's (c3) outcomes for this theme do not line the T5 item separately (they name P1, P3, P11), so it stands here as the row recorded it. The one header-adjacent translation is the motto string, section 6.
- **Why:** The collision is the narrow-width header clip/collision family (KB-35), dispositioned for the population; ruling 2 places header language outside migration correctness (KB-57), and the T5 item's staff-confirmation note is the row's own caveat, preserved here rather than upgraded or erased.
- **Verify:** RENDER-ROWS-1 (RENDER-S2-B) decom-dept row for the charge text; ledger (c2) for the family disposition.
- **Disposition:** DISPOSITIONED (ledger (c2): KB-35 family; the sample overflow items under KB-33/KB-34). The T5 header item stands as recorded in LOCALIZE-ROWS row 78.

### 6. Text translation

- **What:** The body is retained and translated: 9 TRANSLATION-ANCHORED and 29 TRANS-UNANCHORED blocks cover the usage prose, the specimens (blockquotes B42/B43 among them: "That's a horizontal rule" → それは水平線です; the nested-blockquote labels), the tab specimens, and the closing source-code collapsible's labels. The rendered-string translation a reviewer is most likely to meet is the motto: the CSS content string `"Secured, Contained, Protected"` (orig L227) becomes `"確保、収容、保護"` (cand L225, block B49, labeled CSS-BODY heuristic) — the localize row singles this translation and its translator's-note quality out as good, and the bytes bear it out. The usage prose keeps the work's provenance (made for the Decommissioning Department hub, by Calibold) with the hub link repointed and marked （英語版） (section 7).
- **Why:** P10: body and sample text are translated, including strings the CSS renders (a content string is reader-visible text, and leaving the motto in English would have left the theme's signature line untranslated in every rendered header that uses it).
- **Verify:** Read original L47–145 against candidate L41–140; `grep -n '確保' candidate.txt` (cand L225) against original L227.
- **Disposition:** Standing (the port itself; the localize T5 pass judged this theme's text jointly with T4 and praised the item above).

### 7. Links

- **What:** Three link facts. (a) The credit block's source link (cand L28) is the required ruling-3 back-reference. (b) The author-page link inside the author-label specimen: the original links the fullname `Calibri Bold's Mega Cool Author Page` (orig L33); the candidate links the same EN page by full URL, `https://scp-wiki.wikidot.com/calibri-bold-s-mega-cool-author-page`, with the label gaining the （英語版） marking (cand L39, LINK-REPOINT span). (c) The hub link in the prose: the original's `[[[Decom. Dept. Hub|Decommissioning Department]]]` (orig L49) becomes a full EN URL with the same （英語版） marking (cand L41). Both repoints name EN pages that have no JP counterpart in the campaign set, and both say so in the label — the P11 form this population uses for kept EN links.
- **Why:** P11: links to EN hub and author pages are the sibling / batch-posting class; the （英語版） marking is the honest form (the reader is told the target is the English page), and the ledger dispositions the class rather than each link.
- **Verify:** Read candidate L39 and L41 against original L33 and L49.
- **Disposition:** DISPOSITIONED (ledger (c3): P11, sibling / batch-posting class).

### 8. Structure

- **What:** The closing rule is honored: the exhibit's rules survive in the original's order, the sample body is retained, and the tail keeps its shape (source-code collapsible, then the gate close). The structural deletions are three, each with its ground stated. (a) The bare Rate specimen (orig L21–25, BARE-RATE-DEL): replaced by the rate-bearing preview credit block (section 1). (b) The info-module specimen (orig L37–45, INFO-DEL): a demonstration of the EN rating form around placeholder text, replaced by the same credit block; the JP environment's rating form is the credit module, and the specimen's text carried no content beyond the demonstration. (c) The closing more-by include (orig L635): no ground is recorded anywhere — flagged in the Per-theme record. The single EXHIBIT-RESTRUCTURE primary is a repoint inside an exhibit line; the exhibit census is otherwise one-to-one. Brace structure verified by depth scan for this package: the code exhibit and both module CSS blocks end at depth 0 with no negative excursion on both sides.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so each block's ground is stated. Items (a) and (b) are the P3 replacement class; item (c) is what the class looks like without its ground, which is why it is flagged rather than narrated.
- **Verify:** `grep -n 'module Rate\|info:start\|more-by' original.txt candidate.txt` (all three present in the original, all absent in the candidate); sections 1 and the Per-theme record for the grounds and the flag.
- **Disposition:** Standing for (a) and (b) (the P3 replacement); (c) FLAGGED.

### 9. Formatting only

- **What:** none — the classifier counts 0 whitespace-only blocks and 0 re-indentation blocks over 51 change blocks.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; here the ground for "none" is the classifier count above.
- **Verify:** classification.json (summary: reindent_blocks 0; no WS-ONLY label in the label counts).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One reader-visible annotation, and it is the batch's best: the 訳注 at cand L50, attached to the pride-logo usage. It states that in the original's revision-187 source, no conditional comment processes the documented `inc-pride` parameter, so the pride logo is always applied; that this is a discrepancy between the original's documentation and its implementation; and that the port preserves the original's behavior as-is. The classifier's ANNOTATION signature fired on it. There are no `[!-- ... --]` translator comments (`grep -c '\[!--' candidate.txt` = 0).
- **Why:** R2: porter additions are listed so they are never mistaken for original content. This note does more: it adjudicates an original-side inconsistency in the open, at the exact point a reader would act on the false documentation, and it records the port's fidelity decision (preserve behavior, document the discrepancy) where the next editor will find it. Live-parity discipline is the same instinct: the original's behavior, however inconsistent with its own prose, is the spec.
- **Verify:** Read candidate L45–50 (the two usage forms and the note).
- **Disposition:** Standing (the port's own documentation of an original-side discrepancy).

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) T1 pseudo-ref ×5, DISPOSITIONED class (ii): references to pages not yet posted under those names at baseline (the usage self-include's forms among them); they resolve at posting. (2) The foreign-include ×2 (the author-label pair): DISPOSITIONED as the KB-54 named exception (ledger (c1); the set is this theme's pair and the cosmonaut-adjacent cases the register names — for this file, exactly cand L33/L43), with the component port reserved as a separate staff call (FIX3-S2EN §6.7). (3) The render findings: the candidate-header collision and 検索 overprint at ≤375 (DISPOSITIONED, KB-35 family) and the 884px@768 sample overflow, notice clip and WebKit item (DISPOSITIONED, KB-33/KB-34 families), both in (c2). (4) The P11 link markings: DISPOSITIONED (sibling / batch-posting class, (c3)). (5) The draft-host delivery pair (cand L2, L16): class (iii) draft form (P4), rewritten at posting; not charged. One item is NOT dispositioned here: the more-by drop (section 8, item (c)), flagged in the Per-theme record.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–5); the flagged drop stands as documentation, not as a verdict item (the theme's ledger verdict has no OPEN items).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 7 errors / 0 warns / 1 info — pseudo-ref ×5 and foreign-include ×2 (T1-ROWS row 78). Register (c1) dispositions pseudo-ref as class (ii) and the foreign pair as the KB-54 exception. (b) T2/T3 render: FINDINGS — the header collision family and the sample overflow family, both dispositioned in (c2) (RENDER-ROWS-1, RENDER-S2-B). (c) T4 localize plus follow-up: FINDINGS with 3 display-affecting items (LOCALIZE-ROWS row 78): the author-label keep (P1; DISPOSITIONED as the KB-54 exception), the missing translator/year fields (P3; FIXED by FIX2-CREDIT), and the （英語版） link markings (P11; DISPOSITIONED). The row's T5 text praises the subtitle translation and its note, and records the header/tab English with a staff-confirmation note (section 5). The follow-up currency check found nothing to follow: the upstream latest is still revision 187 (campaign record, `diff-decom-dept-from187.txt`). (d) T5: judged jointly with T4 by the localize lane. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (51 change blocks) and the generator's (diff.md: +90/−99 in 8 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:decom-dept-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS at the ledger determination ((b) row 78), with the stamp still reading PASS (Status table).

## Per-theme record

### Wave history, edit by edit

The candidate's current state is the product of two commits. (1) Creation, commit 331ab7e (Stage 2 EN7): the translation (including the motto string), the delivery repoints, the font repoints and the Noto Serif JP supplement with its license documented in the credit block's ninth field, six of the eight credit fields, both rating specimens replaced by the credit block, the author-label pair kept, the （英語版） link forms, the pride-parameter translator's note — and the more-by drop. (2) FIX2-CREDIT, commit 666f543: exactly two added lines, the translator and translation-year fields. No sweep commit touches this file: its usage self-references were already in the bare -jp form at creation.

### Record note — the register's wave names vs this file's commits

The ledger's (c3) line for this theme reads "P1 DISPOSITIONED (posting-procedure convention class); P3 credit fields FIXED (credit waves; checker-verified); P11 DISPOSITIONED (sibling / batch-posting class)". The outcomes are correct in the current bytes. Two precisions this package adds: the P3 fix's vehicle is FIX2-CREDIT and its content is exactly two lines (the creation had done the other six fields itself, a fact (c3)'s plural "credit waves" does not convey); and the P1 line's class name ("posting-procedure convention") is the register's drawer for the same keeping that (c1) names precisely as the KB-54 exception — the (c1) naming is the one a reviewer can act on, and section 2 follows it.

### Flag — the dropped more-by include, undispositioned

The original closes its body with `[[include :scp-wiki:more-by:calibold]]` (orig L635), the author's more-by component, after the source-code collapsible. The candidate has no counterpart (`grep -n 'more-by' candidate.txt`: no hits), and the classifier emits the deletion as residue block B51 with no signature. No register charges or dispositions it: not the ledger's (c1)–(c4) lines for this theme, not the localize row (whose items are P1, P3, T5, P11), not the FIX2-CREDIT report. The drop itself is defensible — the component is author-promotion furniture with no JP port, and ruling 4 ports machinery a theme needs, which a more-by box is not — but the campaign's own practice for this file's other author furniture was a named exception with grounds (the author-label pair, KB-54), and this deletion has neither a charge nor a ground. It is recorded here as a flag with the deciding grep, so a future editor can restore the include or disposition it with the evidence in hand. This package does not edit the candidate.

### Record conflict — the sources.tsv note for this row

sources.tsv's notes column for this theme states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-decom-dept-from187.txt` (kind K5a-i). The artifact records the opposite: `rev187 → rev187 変更: なし` (no changes), with an empty intervening-revision list. There is no post-reference delta to classify and no supersession. The note is a population-level convention in sources.tsv (the same shape recorded for the ambrose-chapter-two, caretaker-sigma, chaos, clock-tower and cosmonaut rows — all five themes in this batch carry it, and all five artifacts contradict it); for this row it does not survive contact with its own citation, and this package follows the artifact.

### Post-package repairs (REFRESH3-F) — NO-EDIT adjudication

**FIX-CARETAKER, landing `ba896f4` (report `R/review-scout/FIX-CARETAKER.md`,
item 4, "decom-dept-jp: dropped more-by include, adjudicated, no edit").**
That report supplies the ground the flag above lacked, and the
adjudication is NO-EDIT: the candidate is byte-unchanged by this landing,
and its canonical file has no commit after the package build (`0533657`)
— `candidate.txt` was already byte-identical to canonical at refresh
time. Census evidence from the report: exactly 2 of 287 originals carry a
`more-by` include (this theme and 512-onwards); 0 of 2 `-jp` candidates
keep one (512-onwards-jp dropped its include the same way); no
`more-by:calibold-jp` candidate exists anywhere in the repo; and the
campaign's only more-by port, `more-by:waylandlaurencepan-jp`, serves the
production page `theme:512-onwards` under a posting-name arrangement, not
any `-jp` candidate. The dropped include is Calibold author-promotion
furniture; if a `more-by:calibold` port is ever commissioned, the include
returns at the original's position in the posting-name form. The flag
above is kept as the as-built record; the file was not edited, so its
verdict and PASS stamp stand unchanged.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-decom-dept-jp.txt` — the render sample page; it is the "sample" the T2/T3 checks rendered, and its 884px overflow at 768px is the render row's subject. (2) `pages/theme:decom-dept.txt` — the repo's EN-side copy of the original page, the EN sample's base. (3) The delivery itself: the candidate's own local--code /1 on the draft host, named by the head module and the frame (cand L2, L16), which is the runtime form of the self-delivery; the original side's /1 was the same exhibit on scp-wiki.wdfiles.com. The author-label component the candidate keeps is EN-side by exception (section 2) and is not part of the JP change set.

## Multi-wave provenance

The candidate's current state is the product of the S2 port and one two-line fix wave: the EN7 creation (commit 331ab7e) did nearly everything, including two acts the other creations in this batch needed waves for (the credit block's substance and the font supplement); LOCALIZE-S2-A examined that state and charged P1, P3, T5 and P11 (its row is LOCALIZE-ROWS row 78); FIX2-CREDIT (commit 666f543) closed the P3 charge with its two lines; the render walk recorded the narrow-width families; the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge, and no later commit touches the file — which is why its stamp still reads PASS. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 78, (c1) foreign-include entry (decom-dept), (c2) decom-dept entry, (c3) decom-dept entry; GOSIGN2-LEDGER-SUPPLEMENT.md (no decom-dept entries); T1-ROWS row 78; LOCALIZE-ROWS row 78; RENDER-ROWS-1 (RENDER-S2-B) decom-dept row; REPORT-GOSIGN2-FIX2-CREDIT.md (campaign record), decom-dept in scope. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

Three residue blocks were emitted. R1 = B42 (orig L138–139 → cand L135–136, TRANS-UNANCHORED heuristic): the blockquote specimen line "That's a horizontal rule" → それは水平線です — a plain specimen translation, section 6. R2 = B43 (orig L140–141 → cand L137–138, TRANS-UNANCHORED heuristic): the nested-blockquote specimen labels, the same shape, section 6. R3 = B51 (orig L634–636 → cand L632, no signature): the deletion of `[[include :scp-wiki:more-by:calibold]]` at the body's close — not a translation item but the undispositioned drop flagged in the Per-theme record, where it is written up with its evidence. No new signature is proposed for R1/R2 (specimen lines are the TRANS-UNANCHORED class's home); for R3 the lane report proposes that a closing-include deletion with no counterpart and no register entry is exactly the shape a future classifier pass should surface as a named drop class rather than residue.
