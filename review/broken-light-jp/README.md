# Review package — theme:broken-light-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:broken-light-jp — origin CN, population #171 [GOSIGN2-LEDGER (b) row 171]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now c3eb642845b1d8c46c3df64c196c47d7ec924e5d046e69905bf4928ef7fd1f9e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 13 errors / 1 warn / 1 info (pseudo-ref×10, hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 149; GOSIGN2-LEDGER (b) row 171]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 337–419px@320/375. [RENDER-ROWS-2 (RENDER-S2-E (CN2))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN2))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 170, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 170]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 171]
- Computed against: canonical commit fb435643733dfd93d8dfa698861e4a59921d8f0f; candidate file pages/theme:broken-light-jp.txt sha256:c3eb642845b1d8c46c3df64c196c47d7ec924e5d046e69905bf4928ef7fd1f9e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 171) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×10 and hotlink ×3 (class (ii), section 11); the render row's items (runtime-hotlink chain on the page; credit-modal preview form and page overflow on the sample, section 11); T4's one display-affecting item (the header fallback text, still Chinese in the bytes), with its ledger disposition in section 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:broken-light | theme:broken-light-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 28 (first translation; the candidate's credit block records 初訳時参照リビジョン: 28) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs2-cn2/CACHE/orig/broken-light.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:broken-light-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 599 lines / 16,869 bytes | 610 lines / 19,317 bytes |
| SHA-256 | 1b58aea48e2f1b32ee0b3b3aee1a2b01ce04a8dcd08b7b02c8ee04fae15e9e1ca | 9037555b5449151b062fa00b6ad721d4dc904194ffa64ad38a7bffff3a5097f9 |

Wave history: the candidate was created by the Stage 2 CN2 integration (commit cf1224e, the LOCALIZE-S2-D wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the translator-attribution normalization that swept all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Black Highlighter-based CN theme （如影随光， "the shadow follows the light") whose port is the fullest form of the campaign's BHL frame in this batch: the JP BHL include at the head, the theme's own layer served from its own local--code with the interwiki-style supplement at priorities 1–3, the base taken from the JP distribution instead of the CN one (bhl.scpwikicn.com), and the original's head module (base imports plus a block of the theme's own rules) dissolved into that frame. The port also does the asset work its siblings deferred: the theme's two images are re-hosted as attachments of the candidate page itself, a license box records each image's license (one CC0 from the original's own header note, two unstated in the original), and two in-page translator's notes explain the font substitution (the original's UI font is the commercial PT Root UI, replaced by the base's UI font plus Noto Sans JP) and the attachment re-hosting. One recorded item stands in the bytes exactly as T4 found it: the applied CSS's header fallback values are still the CN site's ("Site-CN-12" and the Chinese motto), even though the customization example in the same file was localized — dispositioned under ruling 2, and stated in section 5 because a page that does not set the text variables will show them. Measured churn (diff.md: +130/−127 in 51 change blocks; a GNU-diff count of the same pair gives 235 changed lines, and the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 51 change blocks — 32 specific (62.7%), 19 heuristic (37.3%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 16 |
| DRAFT-HOST | 10 |
| COMMENT-TEXT | 5 |
| EXHIBIT-RESTRUCTURE | 3 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| GLYPH-FORM | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 19 heuristic blocks are prose translations and the font-prose work (sections 4 and 6), verified line by line; there is no residue. The 10 DRAFT-HOST blocks are the candidate's references to its own draft-host delivery, which recur because both code exhibits reproduce the delivery form (section 3). The 3 EXHIBIT-RESTRUCTURE primaries adjudicate in section 8: the exhibits correspond two-for-two, and the primaries are their frames and the head module's dissolution. The 5 COMMENT-TEXT blocks and the ANNOTATION block are the porter's own comment text, adjudicated in section 10 (they are not one phenomenon: the annotation is a reader-visible note, the comment blocks are CSS and prose comments). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:broken-light-jp; original theme:broken-light on scp-wiki-cn at reference revision 28; candidate `pages/theme:broken-light-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind K5b-2; the composition is the JP Black Highlighter base candidate the frame includes). The original wraps everything in one gate, `[[iftags +版式]]` (L1–595), with a head module inside it and a tail module outside it (L597–599). The candidate inverts the emphasis: the frame comes first, outside any gate (BHL include, head module, interwiki-style includes, candidate L1–18), and the localized gate `[[iftags +テーマ]]` wraps only the body (candidate L20–608). The tail module disappears; its job is done by the head frame.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for broken-light-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module Rate]]` (original L33). The candidate deletes it (BARE-RATE-DEL block) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L22–31) carrying the eight ruling-3 fields (title 如影随光（影は光に随う）テーマ — the Chinese title kept with a Japanese gloss in parentheses; 翻訳責任者 AI; 翻訳年 2026; 原題 如影随光 主题版式； 著作権者 [[*user AI_Mayca]], a user link in the field as the porter wrote it; 作成年 2022; 初訳時参照リビジョン 28; the source link, naming scp-wiki-cn.wikidot.com/theme:broken-light, the recorded host, which serves the original). T7 credit-module CSS: none added. License box: the candidate **adds** one (candidate L590–606, the LICENSE-BOX block): a `component:license-box-backend`/`license-box-end` frame with an entry per image — the background image recorded as CC0 (the original's own exhibit header says "Background image licensed under CC0", original L195), and two images recorded as "not stated in the original (confirm with the author before posting)". The original has no license box; the addition is the port's own record-keeping, and its unstated entries are honest gaps, not claims.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields. The license box is the campaign's per-image license record for a theme whose images the port re-hosted (section 4).
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L22–31 against the eight fields and L590–606 for the box.
- **Disposition:** Applied (the swap and the box are in the bytes; the ledger's credit outcome for this theme rides on the same credit-wave record as its siblings).

### 2. Includes and components

- **What:** The candidate's includes: the JP BHL theme include at the head (candidate L1, outside the gate — the frame form this theme shares with jiha); the credit pair (section 1); three interwiki-style includes (candidate L7–18, section 3); the image-block for the Site-JP-12 logo example (candidate L104, repointed to `:scp-jp:` with its asset argument re-hosted, section 4); and the license-box pair (section 1). The escaped usage example (candidate L44–45) as built taught the JP branch form with the plain slug: `:scp-jp:theme:black-highlighter-theme` (candidate L44, the production JP page, correct as built and not a sweep line) plus `:scp-jp:theme:broken-light` (candidate L45), which named a page that does not exist on scp-jp, not the posting form. The usage-example population sweep has since completed the second name to the posting form, `:scp-jp:theme:broken-light-jp` (candidate L45; SWEEP-USAGE.md; canonical commit b5cb724). Every live include names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. The usage example's self-repoint as built satisfied the branch half of that rule only; the sweep's completion is what brings it under it. Ruling 4 is not engaged: no new component had to be ported for this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers in three places: a head module importing the base from the CN BHL distribution (`bhl.scpwikicn.com/css/min/normalize.min.css` and `.../black-highlighter.min.css`, original L3–4) followed by a block of the theme's own rules in the same module (original L6–23); a first code exhibit containing a further module (original L87–105, the customization example); and a tail module importing the theme's own layer from its CN page (`scp-wiki-cn.wikidot.com/theme:broken-light/code/2`, original L598). The candidate consolidates all of it into the standard frame: the head module imports only the candidate's own `local--code/theme%3Abroken-light-jp/1` from the draft host (candidate L3–5), and the interwiki-style includes layer the delivery as normalize (priority 1) and base (priority 2) from the JP BHL distribution (scp-jp.github.io) plus the theme's own layer at priority 3 naming the same /1 (candidate L7–18). The head module's own-rules block travels into the own layer, whose body is the second code exhibit (candidate L176–587); the first exhibit keeps its customization-example role (candidate L81–99). The 10 DRAFT-HOST blocks are the own-delivery references across the frame and the two exhibits, which reproduce the delivery form as example text as well as live lines.
- **Why:** P4/T9: delivery is served from JP hosts — the JP BHL distribution for the base, the theme's own code for its layer — never from the original's wiki or its regional distribution. P6/T3 supplies the interwiki-style supplement frame and its priority order (1 normalize, 2 base, 3 own). The draft-host form of the own delivery is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n '@import\|local--code' candidate.txt` — the frame lines and the exhibits' reproductions; no bhl.scpwikicn.com or scp-wiki-cn delivery URL remains live.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: the prose font section (candidate L164–166) names the theme's faces with their sources (Inter for titles, PT Root UI for the UI, Recursive / Noto Serif JP for mono), and the applied CSS adds the JP supplements at the exhibit's head (Noto Sans JP and Noto Serif JP from Google Fonts, candidate L181–182; the JPFONT-LOAD block). The substitution itself is announced in the page (candidate L173, section 10): the original's UI font is PT Root UI, a commercial Paratype face the CN original linked directly; the JP version replaces it with the base's UI font plus Noto Sans JP, because the commercial direct link does not fit the campaign's direct-link exception. The ledger dispositions this theme's P7 item as having no display-affecting mark (section 11). Assets: unlike its deferred-asset siblings, this port re-hosted the theme's images onto the candidate page's own attachments on the draft host — the theme banner `blbhl.png` (candidate L36) and the logo example `logo-a.svg` (candidate L104), both under `local--files/theme%3Abroken-light-jp/` — and the second translator's note (candidate L604) states the reason: the original direct-linked attachments on a sandbox wiki, and the JP version holds them as the candidate's own attachments so the page depends on no external wiki. The customization exhibit's placeholder URLs (`https://url.com` at candidate L87, L90, L93) are the original's example values, kept as examples.
- **Why:** P7 (JP font supplement, and no dependence on a commercial font's direct link) and P5 (assets served from JP hosts — here satisfied in full by re-hosting rather than dispositioned).
- **Verify:** `grep -n 'local--files' candidate.txt` — the two re-hosted assets, both naming the candidate's own page; `grep -n '@import' candidate.txt` for the font loads.
- **Disposition:** Applied (assets and supplement in the bytes); P7 DISPOSITIONED at the ledger for the substitution's display side (no display-affecting mark).

### 5. Header, sidebar, and site furniture

- **What:** The header variables sit in the applied CSS (candidate L202–203), and they are this theme's standing item, verified in the current bytes exactly as T4 recorded it: `--header-title: var(--header-title-text, "Site-CN-12")` and `--header-subtitle: var(--header-subtitle-text, "常隐于影，行必有光")` — the fallback defaults are the CN site's name and motto, unchanged from the original (L208–209). The inconsistency T4 noted is also in the bytes: the customization example in the same file was localized (the example's text variables at candidate L84–85 read タイトル / サブタイトル, and the logo example's caption at candidate L104 reads Site-JP-12), so a reader following the example gets JP text, while a page that applies the theme without setting the text variables falls back to the CN defaults. The HEADERVAR block is this region. The ledger dispositions the item under ruling 2 (section 11). No sidebar or topbar rule was adapted beyond what the moved CSS body already carried.
- **Why:** P9's JP-header expectation is what T4 measured; ruling 2 (header text language is translation taste) is the ground the ledger dispositioned it on — recorded here in full because the fallback is what an unset page displays, and the T4 row judged the item display-affecting on exactly that ground.
- **Verify:** `sed -n '202,203p' candidate.txt` against `sed -n '208,209p' original.txt` — identical fallback strings.
- **Disposition:** DISPOSITIONED (P9, ruling 2, GOSIGN2-LEDGER §(c3) line for this theme).

### 6. Text translation

- **What:** The prose is translated throughout (the 22 TRANS-UNANCHORED heuristic primaries and 16 TRANSLATION-ANCHORED blocks, verified line by line): the usage section, the font section (section 4), the examples, the collapsible labels, and the customization prose around the first exhibit; the GLYPH-FORM block is the simplified-to-Japanese glyph conversion inside the translated strings, and the CONTENT-STRING block is a reader-visible string changed as content (the font section's face names), counted here. Chinese survives only as quotation: the credit fields (candidate L23, L26, L30), the header fallbacks (section 5), and the exhibit CSS's own comments where they are the original's code comments.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings).
- **Verify:** The pairs are diff.md's body sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The prose links are the font sources (candidate L164–166: rsms.me, paratype.com, recursive.design, fonts.google.com — the faces' home pages, kept from the original's font section and serving), and the credit source link (candidate L30, recorded host scp-wiki-cn, serves). No prose link names a foreign wiki page as content, and no bare link names a page missing on scp-jp. The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no divergence: the only wikidot host named is the recorded one, in the source link.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; this theme's links satisfy it as they stand.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link only (plus delivery text inside exhibits, section 3).
- **Disposition:** Standing; no P11 item was recorded for this theme.

### 8. Structure

- **What:** The skeleton corresponds, with the frame inversion of section 0 as the one structural decision: the original's gate wraps the head module, the candidate's frame stands outside the gate. Exhibit census: two code exhibits on each side with corresponding roles — the customization example containing a module (original L87–105 → candidate L81–99, its example variables localized and its placeholder URLs kept) and the theme's own CSS body (original L189–593 → candidate L176–587). The 3 EXHIBIT-RESTRUCTURE primaries are the frames around these exhibits (the source-code section's heading and collapsible, and the first exhibit's module-in-code form), not content restructuring: no exhibit was added, dropped, split, or merged, and the applied body corresponds rule for rule apart from the font loads at its head (section 4) and the header fallbacks it shares with the original (section 5).
- **Why:** R3 requires the census before a restructure is narrated; here the census shows correspondence.
- **Verify:** `grep -n '\[\[code' original.txt candidate.txt` — two exhibits each, at the positions above.
- **Disposition:** Standing (correspondence established).

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two reader-visible translator's notes, both load-bearing. (1) Candidate L173 (an italic note closing the font section): the original specifies PT Root UI, a commercial Paratype face, for the UI; the JP version substitutes the base's UI font and Noto Sans JP because the commercial direct link does not fit the direct-link exception. (2) Candidate L604 (a blockquote note inside the license box): the original direct-linked attachments hosted on a sandbox wiki; the JP version holds them as the candidate page's own attachments, removing the external-wiki dependency. The ANNOTATION block is one of these; the COMMENT-TEXT blocks are the porter's remaining comment text (CSS comments and prose comments that changed with the translation). Unlike its batch siblings, this port announces its two real judgments in the page itself.
- **Why:** R2: porter-added text is part of the change record, and an annotation that explains a substitution is what lets a later maintainer re-derive the decision instead of re-litigating it.
- **Verify:** `grep -n '訳注' candidate.txt` — L173 and L604.
- **Disposition:** Standing (in the record, in the page).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's thirteen errors: pseudo-ref ×10 — the candidate's own draft-host delivery references (section 3), class (ii); hotlink ×3 — class (ii) standing lines (register c1); there is no class (i) error. The 1 warn / 1 info are recorded verbatim in T1-ROWS row 149 and are not classified. (2) The render row's items: on the theme page, only the runtime-hotlink site-theme chain (KB-44: the delivery chain's runtime hosts, an environment-layer reading); on the sample, the credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5) and a page overflow of 337–419px at the 320/375 viewports. (3) T4's one display-affecting item and the font item, with their ledger dispositions (§(c3) line for this theme): the header fallback text — P9 DISPOSITIONED (ruling 2); the font substitution — P7 DISPOSITIONED (no display-affecting mark; the T4 bar). The theme's determination is PASS and this package does not re-open it; item (3)'s first half is stated in section 5 in full because it is visible in the bytes today.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 149): exit 1, 13 errors / 1 warn / 1 info; the errors are pseudo-ref ×10 and hotlink ×3, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN2)): FINDINGS — the page's runtime-hotlink chain only, and the sample's credit-modal (preview-form) and overflow items of section 11(2); engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 170): FINDINGS jointly, display-affecting findings 1; the ledger §(c3) line records the theme's P7/P9 outcomes as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +130/−127 in 51 change blocks; the GNU-diff count of the same pair is 235 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:broken-light-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 171; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The usage example at candidate L45 as built read `@@[[include :scp-jp:theme:broken-light]]@@`: the porting wave's repoint changed the branch prefix but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:broken-light-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. The companion line above it (candidate L44) names `:scp-jp:theme:black-highlighter-theme`, the production JP page, which is correct as built and was not a sweep line. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

### A second, later repair — FIX-NAVLA2, canonical commit fb43564

A repair landed after this package was built that the usage-sweep record above does not cover. FIX-NAVLA2 (report `R/review-scout/FIX-NAVLA2.md`, section 1; flagged first by FIX-NAVLA.md item 2) was landed in canonical commit `fb435643733dfd93d8dfa698861e4a59921d8f0f` ("pages: stylesheet-address repairs in four themes", 2026-11-17). The candidate had two `[[code]]` blocks — a 499 B customization sample at /1 (L81–99) and the 17,602 B stylesheet at /2 (L176–587) — while both delivery lines named /1; the original (rev 28) delivered block 2 by name, and the JP Black Highlighter base include masked the defect in render checks. The repair changed two addresses only: the head module's `@import` (candidate L4) and the interwiki-style frame's `theme=` (candidate L17) now read `local--code/theme%3Abroken-light-jp/2`. The draft-host probe served /2 at 17,602 B (the stylesheet, opening with the BHL normalize @imports) against /1's 499 B, and the T1 checker's 13/1/1 finding set was unchanged apart from the L4 pseudo-ref's block number; class (i) errors 0 before and after. This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:broken-light-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-broken-light-jp.txt` is the decoration sample the render checks ran against (its credit-modal and overflow readings are section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The original-side sample `pages/theme-decoration-sample-broken-light.txt` is the campaign's mirror-side fixture, likewise outside the port. The two re-hosted images (section 4) are attachments of the candidate page itself, recorded in the license box, not separate repo files. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 如影随光 主题版式
- **Author:** AI_Mayca
- **Source:** https://scp-wiki-cn.wikidot.com/theme:broken-light — revision 28
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
