# Review package — theme:clock-tower-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:clock-tower-jp — origin EN, population #72 [GOSIGN2-LEDGER (b) row 72]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 6fffd492f4a4fdb1bd4760e98f9a126e838ec8a317f24bfc6c46e3d40645394e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 2 infos (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 62; GOSIGN2-LEDGER (b) row 72]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` (minor) — BHL min-width overflow 337–419px@≤375 on sample; mangled `url-https//…` stylesheet is a runtime artifact (recorded verbatim). [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 72, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 72]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 72]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:clock-tower-jp.txt sha256:6fffd492f4a4fdb1bd4760e98f9a126e838ec8a317f24bfc6c46e3d40645394e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/clock-tower-jp/candidate.txt (sha256 6fffd492f4a4fdb1bd4760e98f9a126e838ec8a317f24bfc6c46e3d40645394e)
Original: theme:clock-tower — scp-wiki, revision 20 (sha256 c2d64e9f40db989bbccfb24883daaecabeae00c3aa6ab1c4828ce28e15e7c709)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 72). The generated stamp above reads STALE by design: the only post-verdict change to the candidate is the population sweep's one-line usage-name repair (Per-theme record), and the stamp does not carry a PASS onto changed bytes |
| Wave history | Three commits touch the candidate: the Stage 2 EN6 creation (240c3d2), FIX2-CREDIT (666f543 — the six missing credit fields, the duplicate Rate's removal, and the JP font supplement), and the usage-example sweep (b5cb724). Each is narrated in the Per-theme record |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×5 (class (ii)); the BHL base's min-width overflow at ≤375px (base-inherent, KB-33/KB-34 families); the mangled stylesheet URL (a runtime artifact of draft addressing); P4 delivery, including the dropped `stylesheet-ct.css` import, whose payload this package verified (Per-theme record). No item is flagged |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:clock-tower | theme:clock-tower-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20 (first translation; the candidate's credit block records 初訳時参照リビジョン: 20) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-clock-tower.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:clock-tower-jp.txt`, created in commit 240c3d2 (Stage 2 EN6); its last content change is commit b5cb724 (the usage-example sweep) |
| Lines / bytes | 652 lines / 18,362 bytes (the last line carries no trailing newline, so `wc -l` reports 651) | 661 lines / 20,192 bytes |
| SHA-256 | c2d64e9f40db989bbccfb24883daaecabeae00c3aa6ab1c4828ce28e15e7c709 | 6fffd492f4a4fdb1bd4760e98f9a126e838ec8a317f24bfc6c46e3d40645394e |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted. Reference-revision currency: the follow-up artifact `diff-clock-tower-from20.txt` in the campaign record records rev20 → rev20, no changes, so revision 20 is still the upstream latest; the sources.tsv note for this row says otherwise and is dealt with in the Per-theme record. The original page's own metadata, fetched by the FIX2-CREDIT lane on 2026-11-16: title 'Timepiece Theme', created by JackalRelated, created 2021-08-13 (the credit block's title and 作成年 rest on it).

## Summary

Clock-tower (the Timepiece Theme) is a Black Highlighter theme whose original delivers its base twice over (a head module importing both BHL stylesheets from the EN project's GitHub Pages, and two interwiki-style frames naming the same files at priorities 1 and 2), then carries its own layer as a code exhibit delivered at priority 3. The candidate keeps that topology exactly, repointing the base to the JP project's GitHub Pages mirror of the same two files, and its diff is moderate (diff.md: +111/−109 in 6 hunks; the classifier counts 65 change blocks, most of them the sample body's translation). Two findings give the theme its class-U shape. The creation shipped the by-now familiar pair (a two-field credit block and the bare Rate standing beside it), which FIX2-CREDIT closed together with the JP font supplement. And the creation dropped one @import the localize lane flagged as unverified — the original's own `stylesheet-ct.css` attachment — which this package has now verified: the file carries the @font-face for Colus, the commercial display face the original's header stack names, and the candidate replaces that face with Cinzel (import, stack, and a reader-facing translator's footnote), so the import's payload is substituted, not lost. The verification and the record's wording gap are set out in the Per-theme record.

## Class summary

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 23 |
| TRANSLATION-ANCHORED | 22 |
| DRAFT-HOST | 6 |
| EXHIBIT-RESTRUCTURE | 6 |
| INCLUDE-REPOINT | 6 |
| DELIVERY-HOST | 5 |
| CSS-BODY | 3 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Counts: 65 blocks — 39 specific (60.0%), 25 heuristic (38.5%), 1 residue (1.5%), 0 skipped. Topology: the differ also reports relocation candidates between the two files' components; the component census is one-to-one by kind on both sides (head module, code exhibit, tail module), and no content moved between components — the candidates are the alignment of the two delivery channels (module vs frame) that name the same files. Labels are sets per block; these sections were written from classification.json's label spans. Three adjudications matter. (1) The six EXHIBIT-RESTRUCTURE primaries sit on exhibit lines whose includes were repointed; the exhibit census is one-to-one (section 8). (2) The single HEADERVAR block is the Colus → Cinzel header-stack substitution (section 4), a deliberate replacement with its ground stated in the file itself, not a variable drift. (3) The dropped `stylesheet-ct.css` @import line sits inside a font-import block; it is adjudicated in sections 4 and 11 from the fetched file, not from the label.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's frame zone (orig L1–28): the gate (L1), the head module (L2–14) importing the two BHL stylesheets and carrying two `.scp-image-block` rules, the priority-1 frame (L16–19, normalize), the priority-2 frame (L21–24, black-highlighter), and the bare Rate (L26–28). The candidate's frame zone (cand L1–35) is the same pieces in the same order with the Rate replaced by the credit block (cand L26–35). Provenance route: derived from the original at reference revision 20 (see Provenance); no R4 adoption.
- **Why:** This zone is where a BHL theme declares its base delivery; P4/P6 rework exactly this zone, and each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–28 against candidate L1–35; blocks B1–B8 in classification.json.
- **Disposition:** Recorded; the credit reading is section 1, the base and delivery readings sections 2–3.

### 1. Credit and attribution

- **What:** The original has no credit block and no license box; its attribution is the stylesheet's own comment header (orig L211–216 zone: "Timepiece Theme / [2021 Wikidot Theme] / by JackalRelated", with the Phenomena and Clock Tower inspiration line) and its only rating device is the bare `[[module Rate]]` (orig L26–28). The creation added the preview credit block with two fields and left the Rate standing beside it (creation L32). FIX2-CREDIT (commit 666f543) completed the block to all eight ruling-3 fields (cand L27–34: title Timepiece Theme, translator AI, translation year 2026, original title, copyright holder `[[*user JackalRelated]]`, creation year 2021, reference revision 20, source link) and removed the Rate in the same commit (BARE-RATE-DEL span). The field values are evidenced by the wave's fetched metadata (title 'Timepiece Theme', created_by JackalRelated, created_at 2021-08-13; the wave's report notes the body carries no attribution line, so created_by is the evidence for the holder). The comment header survives in the candidate's exhibit, translated, still naming JackalRelated (cand L219–224 zone). There are no per-file license entries on either side to carry (the `#license-area` CSS variables at orig L599–604 → cand L608–613 are BHL furniture styling, carried unchanged, not a license record).
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing form, so the creation's bare Rate beside it was the KB-09 duplicate (ledger class B's mechanism). Ruling 3 fixes the eight fields; the checker's `credit-missing-fields` class (i) rule is "add only the missing fields of the eight, values evidenced", which is the wave's stated method.
- **Verify:** Read candidate L26–35 against the eight-field list; `grep -n 'module Rate' candidate.txt` (absent) against original L27; `git show 666f543 -- pages/theme:clock-tower-jp.txt` (10 insertions, 6 deletions: six fields, the Rate's three lines, the font supplement).
- **Disposition:** Standing. The credit completion and Rate removal are FIXED by FIX2-CREDIT; the ledger determination then found nothing open (section 12).

### 2. Includes and components

- **What:** The candidate's complete include list (grep, 10): the three interwiki-style frames (priorities 1, 2, 3), the credit pair, `:scp-jp:component:theme-squares` (the color exhibit), `:scp-jp:component:toggle-sidebar-bhl` twice (once in the body tail, once inside the usage exhibit in `@@` form), and the two usage-exhibit includes (`:scp-jp:theme:black-highlighter-theme`, `:scp-jp:theme:clock-tower-jp`). Every include is repointed from `:scp-wiki:` to `:scp-jp:` (candidate `:scp-wiki:` count 0). Two naming decisions need a reviewer's eye. (a) The usage exhibit's base include names `:scp-jp:theme:black-highlighter-theme` — the production BHL page's fullname, not the campaign candidate's -jp name. That is this family's settled convention, not an oversight: the BHL-family candidates themselves take their base from the production page (the ashes-to-ashes and doap-bhl candidates include `:scp-jp:theme:black-highlighter-theme` at their heads), because the production page is what a JP reader's article actually composes with. (b) The usage self-include names the -jp form (the sweep's repair). The toggle-sidebar-bhl pair is not a duplication defect: the original carries the same two instances in the same positions (a live include in the tail and an escaped specimen in the usage exhibit). The iftags tag is localized (orig L1 → cand L1).
- **Why:** P1: foreign-site includes are repointed to the JP site. P2/T2 (KB-08): iftags conditions name JP tags. The base-name choice in (a) follows the population's own BHL practice; the alternative (naming the unposted candidate in user-facing instructions) would tell readers to include a page that does not exist for them.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists; for (a), `grep -n 'black-highlighter-theme' pages/theme:doap-bhl-jp.txt` (the family head form).
- **Disposition:** Standing. No foreign include is kept, so KB-15/KB-54 do not engage.

### 3. Delivery and code loading

- **What:** The base is delivered twice on both sides, in the original's own redundancy: a head module @importing normalize.min.css and black-highlighter.min.css (orig L3–4, from nu-scptheme.github.io, the EN BHL project's GitHub Pages) and two frames naming the same files at priorities 1 and 2 (orig L17/L23). The candidate repoints all four references to the same two paths on scp-jp.github.io (cand L3–4, L17, L23), the JP BHL project's mirror host, and the frame includes to `:scp-jp:component:interwiki-style`, parameters unchanged (priority, theme — the surviving P6 pair). The theme's own layer is the code exhibit (each side's only `[[code]]` block: orig L209, cand L217), delivered by the tail module's @import of own /1 (orig L647 → cand L656, draft host) and the priority-3 frame naming own /1 (orig L651 → cand L659 zone, draft host); /1 is the correct fragment on both sides (SELF-DELIVERY ×2, DRAFT-HOST ×6 across the head and tail references). One original @import has no candidate counterpart: `stylesheet-ct.css` at orig L219, adjudicated in section 4.
- **Why:** P4/T9: base deliveries are served from the JP project's hosts in this environment (the scp-jp.github.io mirror of the same BHL build), and a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. Keeping the original's double delivery is fidelity to the original's topology, not a port defect: both channels name the same two files in the same order on both sides.
- **Verify:** `grep -n '@import\|interwiki-style' original.txt candidate.txt` and compare channel by channel; `grep -n '\[\[code' candidate.txt` (one block, L217) against the two /1 references (cand L656 and the priority-3 frame).
- **Disposition:** The draft-host pair is class (iii) draft form; the base repoint is recorded (ledger (c3): P4 DISPOSITIONED, delivery class (ii) — see the Per-theme record for what that label does and does not say about `stylesheet-ct.css`).

### 4. Fonts and assets

- **What:** Fonts are this theme's densest section. The original's exhibit imports two lines (orig L218–219): a Google Fonts line carrying Courier Prime, Gowun Batang, Jost and Nothing You Could Do, and the theme's own attachment `stylesheet-ct.css`. Its stacks (orig L231–235 zone): `--body-font 'Jost'`, `--header-font 'Colus'`, `--title-font 'Gowun Batang'`, `--mono-font 'Courier Prime'`, none with a JP fallback. The candidate's exhibit imports three lines (cand L226–228): Cinzel (new), Noto Sans JP (new), and the original's four-family line carried unchanged. Its stacks (cand L240–244): body `'Jost', 'Noto Sans JP'`; header `'Cinzel', 'Noto Sans JP'` (the HEADERVAR block); title `'Gowun Batang', 'Noto Sans JP'`; mono `'Courier Prime', monospace` (no JP fallback inserted — the supplement's scope was the three text stacks, recorded here as in the chaos package). The `stylesheet-ct.css` import is gone, and the substitution it fed is documented inside the file itself: the font exhibit's header span now reads ヘッダーフォントはCinzelです with a translator's footnote (cand L209) stating that the original used Colus, a commercial face of unclear license distribution that the special distribution source cannot supply, replaced by the similar Google Fonts face Cinzel. This package verified the premise: the fetched `stylesheet-ct.css` (EN attachment, fetched 2026-11-17) opens with the `@font-face` for 'Colus' with the font embedded as a base64 data URI — the import's payload was the Colus face, and nothing in the candidate needs it once the stack names Cinzel. Provenance of the changes: the Cinzel substitution and the import drop are creation acts (commit 240c3d2 already carries the Cinzel import and no stylesheet-ct line); the Noto Sans JP import and the three stack insertions are FIX2-CREDIT acts (commit 666f543). Assets: the theme's three graphics are attachments of its own page, all repointed from the EN page's files to the candidate's own files on the draft host — ctlogo.png (the body image, orig L91 → cand L99; and `--logo-image`, orig L227 → cand L236), color-bg.png (orig L380 → cand L389), ctfog.gif (orig L386 → cand L395). No asset was dropped.
- **Why:** P7/T5 (KB-16): no JP typeface was loaded or named at creation; FIX2-CREDIT's supplement is the standard repair. The Colus → Cinzel substitution is a different class: a font that cannot be lawfully redistributed through the campaign's channels cannot be the port's header face, and the port documents the replacement where a reader meets it (the exhibit footnote), which is the R2 annotation discipline applied in the body rather than in a comment. P5: the kept Google Fonts line was already on the allowed host in the original; the two added lines use the same host.
- **Verify:** `grep -n '@import' candidate.txt` (three lines, L226–228) against original L218–219; read candidate L240–244 against original L231–235; read the footnote at candidate L209; the fetched stylesheet's first line (the @font-face) is reproducible from the URL in original L219.
- **Disposition:** Fonts FIXED (ledger (c3): P7 FIXED; the vehicle was FIX2-CREDIT, see the Per-theme record). The stylesheet-ct.css drop is DISPOSITIONED under P4 (ledger (c3)) and is verified in substance here.

### 5. Header, sidebar, site furniture

- **What:** The theme's `:root` names `--header-title: "SCP FOUNDATION"` and `--header-subtitle: "TICK. TOCK. TICK. TOCK."` (orig L228–229), and the candidate keeps both byte-identical (cand L237–238). The localize row noted the subtitle's English without a numbered charge, and the ledger carries no P9 line for this theme; the keeping is recorded here so the fact is visible rather than buried in an unchanged line. The sidebar furniture is BHL's, reached through the base delivery and the toggle-sidebar-bhl include (section 2); the theme's own furniture rules (the head module's `.scp-image-block` pair) are carried unchanged.
- **Why:** Ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57, patterns 9c5e907): these two values are the work's own furniture text, and the subtitle is a sound effect, not prose awaiting translation.
- **Verify:** Read orig L228–229 against cand L237–238.
- **Disposition:** Kept under ruling 2's scope; no register charges it.

### 6. Text translation

- **What:** The body is retained entire and translated: 22 TRANSLATION-ANCHORED and 23 TRANS-UNANCHORED blocks cover the prose introduction (B9 in the skeleton's appendix: the Phenomena/Clock Tower sentence, translated whole), the theme-squares color names (kept in English as exhibit data — Large Scissor Blades and its siblings are the palette's names, with their hex values unchanged), the usage prose, the heading specimens （第1見出し through 第6見出し）, the tab texts, and the collapsible labels. The exhibit comment header is translated with its attribution intact (section 1). The translator's footnote at cand L209 is the port's one reader-visible addition and is counted in section 10. No glyph-form conversions (R5) occur; this port has no CN text.
- **Why:** P10: body and sample text are translated; exhibit data values (color names bound to CSS variables, hex codes) are carried, since renaming them would falsify the specimen. The headings specimen is translated because its content is the specimen (what a heading looks like), not data.
- **Verify:** Read original L30–205 against candidate L38–213; the theme-squares parameters are unchanged apart from the include's site prefix.
- **Disposition:** Standing (the port itself). The localize T5 pass judged this theme's text jointly with T4; its display-affecting items are the font and the delivery flag (sections 3–4), not the body text.

### 7. Links

- **What:** The credit block's source link (cand L34) is the required ruling-3 back-reference. The prose note under the logo — "これはBlack Highlighterベースのテーマです… [[[theme:black-highlighter-theme|詳しくはこちら]]]" (orig L103 zone → cand L111 zone) — keeps its target in the plain fullname form, which on the JP wiki resolves to the production BHL page: the same production-page naming the usage exhibit uses with an explicit `:scp-jp:` prefix (section 2), and consistent with it. No other body links exist; the sample's link specimens are code-form exhibits.
- **Why:** P11 repoints links to JP counterparts where a counterpart exists; here the counterpart is the production page the link already names in same-wiki form, so there is nothing to repoint.
- **Verify:** `grep -n 'black-highlighter-theme' candidate.txt` (the prose link and the usage include, both naming the production page).
- **Disposition:** Standing; no link flag.

### 8. Structure

- **What:** The closing rule is honored: the exhibit's rules survive in the original's order, the two delivery channels keep their original redundancy, and the tail keeps its shape (toggle include, delivery module, priority-3 frame). The six EXHIBIT-RESTRUCTURE primaries sit on repointed exhibit lines (the theme-squares include, the image line, the usage includes); the exhibit census is one-to-one — theme-squares, logo image with its caption (including the caption's own malformed `width:width:300px;;` style, carried byte-identical: a specimen of the original's state, not a port error), usage exhibits, heading specimens, tabs, and the font spans all survive. The one structural deletion is the bare Rate's (section 1). Brace structure verified by depth scan for this package: the code exhibit and both module CSS blocks end at depth 0 with no negative excursion on both sides.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so each block's ground is stated. The exhibit census is the deciding check, and here it is one-to-one.
- **Verify:** `grep -n 'theme-squares\|ctlogo\|tabview\|collapsible' candidate.txt` against the original's body; the depth scan is reproducible from the two package files.
- **Disposition:** Standing (no exhibit restructuring in substance, despite the label's six firings).

### 9. Formatting only

- **What:** none — the classifier counts 0 whitespace-only blocks and 0 re-indentation blocks over 65 change blocks.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; here the ground for "none" is the classifier count above.
- **Verify:** classification.json (summary: reindent_blocks 0; no WS-ONLY label in the label counts).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One reader-visible annotation exists, although no ANNOTATION signature fired: the translator's footnote at cand L209, attached to the font exhibit's header span, explaining the Colus → Cinzel replacement (quoted in substance in section 4). It rides inside the translation block for that span, which is why the skeleton's per-section text cannot show it. There are no `[!-- ... --]` comments (`grep -c '\[!--' candidate.txt` = 0); the exhibit's comment header is the original's own, translated.
- **Why:** R2: porter additions are listed so they are never mistaken for original content. A footnote in the body is the strongest form of the discipline — the reader meets the explanation at the exact point of divergence — and it is recorded here so the package's accounting matches the file.
- **Verify:** Read candidate L209.
- **Disposition:** Standing (the port's own documentation of its one substitution).

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) T1 pseudo-ref ×5, DISPOSITIONED class (ii): references to pages not yet posted under those names at baseline; they resolve at posting. (2) The render findings, both DISPOSITIONED in (c2): the BHL min-width overflow of 337–419px at ≤375px on the sample (the base's own geometry, KB-33/KB-34 families — a BHL-based theme inherits it, and the port's own layer adds nothing to it), and the mangled `url-https//…` stylesheet reference, which is a runtime artifact of draft-host addressing recorded verbatim, not a file content. (3) The `stylesheet-ct.css` @import drop: DISPOSITIONED under P4 in (c3); its substance is verified in section 4 (the file carries the Colus @font-face; the port substitutes Cinzel). (4) The draft-host delivery pair (cand L656 and the priority-3 frame's theme=): class (iii) draft form (P4), rewritten at posting; not charged. (5) The header/subtitle strings kept in English: ruling 2 scope (section 5); no register charges them.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–4); item 5 recorded under ruling 2.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 5 errors / 1 warn / 2 infos, the errors pseudo-ref ×5 (T1-ROWS row 62). Register (c1) dispositions pseudo-ref as class (ii). The FIX2-CREDIT wave's own post-fix checker run for this file reports error 5 / warn 1 / info 2 (its report's table), unchanged, consistent with the remaining items being the class (ii) set. (b) T2/T3 render: FINDINGS (minor) — the base-inherent overflow and the runtime-artifact stylesheet URL, both dispositioned in (c2) (RENDER-ROWS-1, RENDER-S2-A (EN6)). (c) T4 localize plus follow-up: FINDINGS with 2 display-affecting items (LOCALIZE-ROWS row 72): no Japanese-capable font (P7; FIXED) and the `stylesheet-ct.css` drop flagged for verification (P4; DISPOSITIONED, and verified in this package). The row's other charges (six missing credit fields; the duplicate Rate at draft L32) were closed by FIX2-CREDIT before the ledger determination. The follow-up currency check found nothing to follow: the upstream latest is still revision 20 (campaign record, `diff-clock-tower-from20.txt`). (d) T5: judged jointly with T4 by the localize lane. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (65 change blocks) and the generator's (diff.md: +111/−109 in 6 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:clock-tower-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS at the ledger determination ((b) row 72), with the stamp STALE for the sweep reason stated in the Status table.

## Per-theme record

### Wave history, edit by edit

The candidate's current state is the product of three commits. (1) Creation, commit 240c3d2 (Stage 2 EN6): the translation, the BHL repoint to scp-jp.github.io on all four base references, the delivery repoints, the Colus → Cinzel substitution with its footnote, the `stylesheet-ct.css` drop — and the two-field credit block with the bare Rate still standing beside it (creation L32). (2) FIX2-CREDIT, commit 666f543 (10 insertions, 6 deletions): six credit fields added with values evidenced from the original page's fetched metadata (title 'Timepiece Theme', created_by JackalRelated, created_at 2021-08-13); the bare Rate deleted; the Noto Sans JP import added and the fallback inserted into the body, header and title stacks. (3) The usage-example sweep, commit b5cb724: one line, the usage self-include's name in the -jp posting form.

### Record note — the register's wave names vs this file's commits

The ledger's (c3) line for this theme reads "P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery); P7 FIXED (font wave)". As with the other themes in this batch, "font wave" is a class-level name: the file's history contains no font-wave commit, the fix rode in FIX2-CREDIT, and (c3) likewise does not name that commit's credit completion or Rate removal. This package follows the git record.

### Record note — what the P4 disposition does and does not say

The localize lane's P4 flag was specific: "`stylesheet-ct.css` @import dropped without verification". The ledger's disposition answers with a class label ("delivery class (ii): original-state CDN delivery") that fits the theme's BHL CDN repoint better than it fits the flagged item, and nowhere in the vendored record is the dropped file's content examined. This package performed the missing verification: the file (fetched from the EN page's attachments on 2026-11-17) opens with the `@font-face` definition for 'Colus' with the font embedded as a base64 data URI — it is the delivery vehicle for the one face the candidate deliberately replaces with Cinzel, a substitution the candidate documents in its own footnote (cand L209). The disposition's outcome is therefore consistent with the bytes, but its stated ground does not establish that; the ground is established here. The distinction matters for the next theme with an unverified drop: a class label is not a verification.

### Record conflict — the sources.tsv note for this row

sources.tsv's notes column for this theme states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-clock-tower-from20.txt` (kind K5a-i). The artifact records the opposite: `rev20 → rev20 変更: なし` (no changes), with an empty intervening-revision list. There is no post-reference delta to classify and no supersession. The note is a population-level convention in sources.tsv (the same shape recorded for the ambrose-chapter-two, caretaker-sigma and chaos rows); for this row it does not survive contact with its own citation, and this package follows the artifact.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-clock-tower-jp.txt` — the render sample page; it is the "sample" the T2/T3 checks rendered, and its ≤375px overflow is the render row's subject. (2) `pages/theme:clock-tower.txt` — the repo's EN-side copy of the original page, the EN sample's base. (3) The base delivery itself: the two BHL stylesheets on scp-jp.github.io (the JP project's mirror of the Black Highlighter build), named by four references in the candidate (cand L3–4, L17, L23); the port's rendering is meaningless without them, and their JP hosting is the P4 act. (4) The delivery itself: the candidate's own local--code /1 on the draft host, named by the tail module and the priority-3 frame, which is the runtime form of the self-delivery; the original side's /1 was the same exhibit on scp-wiki.wdfiles.com.

## Multi-wave provenance

The candidate's current state is the product of the S2 port, one fix wave, and the documentation era's sweep: the EN6 creation (commit 240c3d2) translated, repointed the base to the JP mirror, and made the font substitution, but shipped the credit and duplicate-Rate defects named above; LOCALIZE-S2-A examined that state and charged the credit fields, the Rate, P7 and the P4 flag (its row is LOCALIZE-ROWS row 72); FIX2-CREDIT (commit 666f543) closed the credit, Rate and font charges in one commit, with the credit values evidenced from a fresh fetch of the original page's metadata; the render walk recorded only the base-inherent overflow and the runtime artifact; the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge; and this package's build supplied the one verification the record had skipped (the dropped import's payload). The only later change is the usage-example sweep (commit b5cb724), which is why the generated stamp reads STALE. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 72, (c2) clock-tower entry, (c3) clock-tower entry; GOSIGN2-LEDGER-SUPPLEMENT.md (no clock-tower entries); T1-ROWS row 62; LOCALIZE-ROWS row 72; RENDER-ROWS-1 (RENDER-S2-A) clock-tower row; REPORT-GOSIGN2-FIX2-CREDIT.md (campaign record), clock-tower row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

One residue block was emitted. R1 = B17 (orig L112 → cand L120): the section heading `+ Examples` → `+ 例`. No signature in the table matches a bare heading line whose only change is its text. It is a plain heading translation of the P10 class, of the same shape as the examples heading in the caretaker-sigma package; it belongs to section 6 and is counted there. No new signature is proposed for a single generic heading line.

## License and attribution

- **Title:** Timepiece Theme
- **Author:** JackalRelated
- **Source:** https://scp-wiki.wikidot.com/theme:clock-tower — revision 20
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
