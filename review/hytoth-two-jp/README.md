# Review package — theme:hytoth-two-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:hytoth-two-jp — origin EN, population #98 [GOSIGN2-LEDGER (b) row 98]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 563ecdb78f79efa877608ee901b627700ffbe971fcdf4c16fc5061204242824e); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 15 errors / 0 warns / 1 info (hotlink×13, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 108; GOSIGN2-LEDGER (b) row 98]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-rate contradicted by eye; massive page-overflow 533/548px@320/375 and desktop 1433–1438px@1366 + 972px@768; header tagline/財団 clipped ≤375; WebKit-only IMMRAMA header clip ≤375; cdn.scpwiki.com carried over (Basalt exception). [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 98, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 98]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 98]
- Computed against: canonical commit 45976a8f2cf8f9266e96fa5399f3a3bbeb254f7b; candidate file pages/theme:hytoth-two-jp.txt sha256:563ecdb78f79efa877608ee901b627700ffbe971fcdf4c16fc5061204242824e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/hytoth-two-jp/candidate.txt (sha256 7e3d8b5d44b2a09e4051b564ce6c368c2d729639f7a9f19821f5a8d109b83364)
Original: theme:hytoth-two — scp-wiki, revision 30 (sha256 1d4375c285d6d5fd197b7e85d08ff185ed81d30880459225204802477f06bbcd)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 98); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no hytoth-two entries |
| Fixed after the localize check | P7 (Japanese font supplement), landed inside commit f931619 (FIX2-COLON) together with the basalt delivery repoint from the EN Basalt CDN to theme:basalt-jp; duplicate @imports removed in commit a497307 (FIX4-MECH) |
| Standing items | **DISPOSITIONED** — T1 hotlink×13 and pseudo-ref×2 (ledger (c1) classes); localize P4 EN-CDN Basalt delivery, class (ii) original-state delivery, and P5 EN-storage logos, class (ii) / KB-58 (ledger (c3)); render findings: the hidden-rate machine values (KB-50), the large page-overflow measurements and the ≤375 header clips (ledger (c2)) |
| Carried flag (this package) | The candidate inlines the Basalt base body (declared in its own prose, cand L1913) and the inlined copy diverges from the live theme:basalt-jp on eight logo URLs, whose EN-host values override the imported base's JP-host values in the cascade (section 3; Per-theme record, item 1) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:hytoth-two | theme:hytoth-two-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 30, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 30 | — |
| Source of this copy | Campaign mirror store `orig-hytoth-two-rev30.txt` (class COPY, byte-identical; review/sources.tsv) | Canonical file `pages/theme:hytoth-two-jp.txt`, created in commit a869415 (Stage 2 EN11); later commits f931619 (FIX2-COLON) and a497307 (FIX4-MECH, last content change) |
| Lines / bytes | 840 lines / 26,671 bytes | 2,434 lines / 71,579 bytes |
| SHA-256 | 1d4375c285d6d5fd197b7e85d08ff185ed81d30880459225204802477f06bbcd | 7e3d8b5d44b2a09e4051b564ce6c368c2d729639f7a9f19821f5a8d109b83364 |

Provenance route: derived from the original at the reference revision, layered over theme:basalt-jp (sources.tsv kind: K5b-3, with the note "candidate layers over theme:basalt-jp (this package's diff covers the theme's own layer only)"). The note scopes this package's diff: the Basalt-derived region of the candidate's module is the base's body, and its provenance is theme:basalt-jp's own package; section 3 measures the copy against that base directly, because the copy is part of this candidate's delivered bytes. The theme's own layer is the original's code exhibit (orig L322–821).

## Summary

The original is a Basalt-based theme ("Second Second Hytoth") with a three-part delivery: a parameterized page include of theme:basalt (orig L11, carrying hidetitle / centertitle / acs-itemnum / disable-acs-anim), its own stylesheet served as its own /1 (frame priority=4 and a module @import), and a license box. The candidate rebuilds that delivery as one large inline module (cand L6–1576): the Basalt-derived body first (cand L7–1074, measured 0.975-similar to theme:basalt-jp's fragment 1, 42 differing lines), then the theme's own layer (cand L1075–1575), with the basalt parameter mechanism reproduced as gated modules at cand L1579–1595, two frames naming basalt-jp /1, and the module also @importing basalt-jp /1 (cand L31). The candidate declares this form in its own documentation prose (cand L1913: the theme's CSS and the base Basalt 2.1.0 including Bedrock are inlined in this page; the exhibit that follows is the theme-specific part), and the bytes match the declaration — the contrast with the alcur-theme-jp case in this campaign, where the prose declared layering and the bytes inlined. What remains as a flag is narrower and measured: the copy freezes Basalt 2.1.0, and where it differs from the live base, its values win the cascade — concretely the eight logo URLs (--logo and seven --memo-logo values) keep EN-host forms while basalt-jp's own carry JP-host forms (section 3). The classifier counts 68 blocks (39 specific, 23 heuristic, 6 residue, all resolved in the Appendix); diff.md measures +1689/−95 in 11 sections, the small removal count reflecting that almost everything in the original survives somewhere in the candidate. The theme passed with no open items.

## Classification

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 27 |
| TRANS-UNANCHORED | 27 |
| EXHIBIT-RESTRUCTURE | 4 |
| INCLUDE-REPOINT | 4 |
| IFTAGS | 3 |
| COMPONENT-SWAP | 3 |
| DELIVERY-HOST | 2 |
| DELIVERY-MOVE | 2 |
| DRAFT-HOST | 2 |
| INFO-DEL | 2 |
| LICENSE-BOX | 2 |
| LINK-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| COMMENT-TEXT | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Counts: 68 blocks — 39 specific (57.4%), 23 heuristic (33.8%), 6 residue (8.8%), 0 skipped. The heuristic and residue mass is this theme's shape, not neglect: a 500-line translated body produces single-line translation blocks with no anchors, and every one is resolved in the Appendix. Topology: the original's code exhibit (orig L321–821) matched into the candidate's module-css (cand L5–1576) at 0.99 similarity; the candidate-side own-delivery companion body was unavailable to the classifier (its recorded caveat). Labels are sets per block; this README's sections were written from classification.json's label spans, not from the skeleton's per-section lists (the skeleton runs to 471 lines for this theme because block B2, the delivery restructure, carries fourteen labels at once).

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with the `[[iftags +theme]]` gate holding a hidden logo image (orig L1–3), the interwiki-style include (L5–9, priority=4, theme= its own /1), and the parameterized basalt include inside a display:none div (L10–12). The candidate opens with the same hidden-logo gate (cand L1–3), a second iftags (L5), and the inline module (L6–1576). Provenance route: derived from the original at reference revision 30, layered over theme:basalt-jp (sources.tsv kind K5b-3; see Provenance).
- **Why:** The header frame is where the original declares its delivery; P4 reworks exactly this frame, and the whole of section 3 is its reading.
- **Verify:** Read original L1–17 against candidate L1–6.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original's info module (orig L20–24) contains exactly one line of content, the author-page link `[[[badooga-author-page|More By Badooga]]]`; the intro prose credits the theme to badooga, records that it modernizes theme:hytoth by macro_au_micro and NatVoltaic, and borrows CSS from theme:foxtrot (Liryn) and SCP-9628 (sprawlingstar). The candidate replaces the info module with the preview credit block (cand L1610–1619): `:scp-jp:credit:start-preview` / `end-preview` with all eight ruling-3 fields — title Second Second Hytothテーマ, translator AI, translation year 2026, original title, copyright holder badooga, creation year 2026, reference revision 30, and the source link to the EN page. The author field agrees with the original's own credit (the info link, the intro prose, and the license box's logo attribution all name badooga). The lineage credits (macro_au_micro, NatVoltaic, Liryn, sprawlingstar) survive in the translated intro prose (CREDIT-PROSE). The license box is retained whole (section 8). The credit-module CSS the classifier fires on (T7-CREDIT-CSS span cand L1245–1250) sits inside the inlined Basalt copy: it is basalt's own credit CSS, inherited through the copy; the original's own layer contains no creditRate rules (grep: 0 hits), because in the original they arrive with the basalt include. No bare `[[module Rate]]` exists on either side.
- **Why:** P3/T1: the preview credit module is the JP environment's credit form (patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields and credits campaign translations to AI.
- **Verify:** Read candidate L1610–1619 against the eight-field list, original L20–24 and the license entries at candidate L2420–2432.
- **Disposition:** Standing (the port's credit form); the localize lane verified the credit form and charged no credit item.

### 2. Includes and components

- **What:** The candidate's include list (grep): the two interwiki-style frames naming basalt-jp /1 (cand L1600–1610 region, section 3), the credit pair (L1610/L1619), the escaped usage includes (cand L1628, L1642, L1644), the theme-squares component (cand L1661, repointed), the acs-animation include inside the parameter block (cand L1595 area), and the license-box pair (cand L2420, L2432, repointed `:scp-jp:`). Changes against the original: (a) the parameterized basalt page include (orig L11) is replaced by the delivery composition in section 3 — a page include of theme:basalt-jp would inline the base page's whole body (its prose, exhibits and credit block) into every page using this theme, which is not a viable delivery, so the port reproduces the mechanism instead of the include; (b) the original's usage exhibits, written as nested @@/span constructions that assemble `:scp-wiki:theme:hytoth-two` at render (orig L33, L53, L55), are simplified to plain @@[[include theme:hytoth-two-jp]]@@ lines (COMPONENT-SWAP spans B8/B13/B14: orig L32–33, L52–53, L54–55 → cand L1627–1628, L1641–1642, L1643–1644); (c) every surviving component include is repointed `:scp-wiki:` → `:scp-jp:` (INCLUDE-REPOINT ×4). No `:scp-wiki:` include remains live in the candidate.
- **Why:** P1: foreign-site includes are repointed to the JP site, and a same-site include takes the bare fullname form. Ruling 4 and the 2026-11-16 cross-theme ruling: a based theme layers over the base's JP candidate (theme:basalt-jp), never over the raw upstream delivery — the candidate's frames and import name basalt-jp, satisfying the ruling's target, while the inline copy is section 3's separate question.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing, with the delivery composition carried in section 3.

### 3. Delivery and code loading

- **What:** The original delivers in three parts: the basalt layer by parameterized page include (orig L11: hidetitle={$hidetitle}, centertitle=a, acs-itemnum={$acs-itemnum}, disable-acs-anim={$disable-acs-anim}); its own layer as its own /1, loaded by the frame (orig L5–9, priority=4) and by a module @import (orig L14–16); and a small theme-squares companion module (orig L65–70). The candidate delivers as follows. (1) One inline module (cand L6–1576) whose first 1,068 lines (cand L7–1074) are the Basalt-derived body and whose remainder is the theme's own layer: measured against theme:basalt-jp's fragment 1 (its code block at basalt-jp L85–1143), the Basalt region is 0.975-similar with 42 differing lines, and 72.0% of the whole module's lines match basalt-jp's file in sequence. The 42 differences are enumerable: the theme's own Charm and Noto Sans JP imports at the head; basalt's bedrock @imports replaced by an @import of basalt-jp /1 itself (cand L31); --UI-font-primary carrying the P7 'Noto Sans JP' insertion; two small rule blocks near the region's end; and the eight logo URLs below. (2) The module also @imports basalt-jp /1 (cand L31), and two interwiki frames name basalt-jp /1 (cand L1600 priority=1 on the draft host, cand L1605 priority=2 on scp-jp.wdfiles.com) — the audit classes basalt-jp /1 as a MATCH delivery, one of its /1–/6 multi-part set. (3) The basalt parameter mechanism is reproduced in JP form as blockquoted gated modules (cand L1579–1595): `[ift{$hidetitle}gs -basalt-override]` wrapping the #page-title display:none module, and the acs-itemnum / disable-acs-anim gates wrapping their modules and the acs-animation include — the same `[ift{$param}gs` idiom basalt-jp itself uses for its include parameters, so the theme's documented settings (hidetitle, acs-itemnum, disable-acs-anim) still function. (4) The theme-squares companion module survives (cand L1654–1659). (5) The candidate's own /1 is the retained code exhibit (cand L1915–2414), which now holds the theme's own layer only and is documentation: nothing loads it, and the candidate says so (cand L1913). The cascade consequence of (1)+(2): the module's own rules follow its @import, so where the copy and the live basalt-jp differ, the copy wins. For --logo the theme's own layer then overrides both (cand L1087: --logo: var(--hytoth-logo-1), an EN-host file of the theme's own, part of the P5 set). For the seven --memo-logo values nothing overrides the copy, so the copy's EN-host URLs (scp-wiki.wikidot.com/local--files/theme%3Abasalt/...) are the live values, where basalt-jp's own fragment carries the JP-host forms (sigma10-jp-test.wdfiles.com/local--files/theme%3Abasalt-jp/...). The files are the same artwork on the EN host, so the visible effect today is nil; the structural effect is that this theme does not receive basalt-jp's host repoint or any future basalt-jp correction to those values, and the same freezing applies to the whole copied region as basalt-jp evolves.
- **Why:** P4/T9: deliveries are served from JP hosts, and based themes layer over the JP base candidate. The population's form for basalt-based themes is @import layering (theme:admo-jp in this campaign imports basalt-jp /1 and carries no basalt body). This candidate instead carries the body, and declares that it does (cand L1913) — a declared, deliberate delivery decision by the porter, which is why this package records it as a measured divergence for the coordinator rather than as a false record: the alcur-theme-jp defect was that the prose claimed layering while the bytes inlined a stale copy; here the prose and the bytes agree, the copy measures 0.975-current against the live base, and its differences are enumerated above. The remaining substance is the freezing and the eight cascade-live EN-host values.
- **Verify:** The measurements are reproducible from this repo alone: extract candidate L7–1074 and pages/theme:basalt-jp.txt L86–1142 and diff (42 differing lines); `grep -n 'memo-logo' candidate.txt pages/theme:basalt-jp.txt` and compare hosts; read cand L1913 for the declaration and cand L1579–1595 for the parameter mechanism.
- **Disposition:** The parameter mechanism, the frames and the companion module are standing. The inline copy itself is flagged, not dispositioned: no register adjudicated this theme's delivery composition (the sources note pre-scopes the package diff to the theme's own layer; it does not rule on the copy), and the theme's ledger PASS was determined on the P4/P5/P7 items, where P4 was dispositioned as original-state CDN delivery — a description of the creation state, before FIX2 repointed the frames to basalt-jp (Per-theme record, item 1).

### 4. Fonts and assets

- **What:** The live module's @import census is exactly four lines: Charm (cand L7, the theme's display face), Noto Sans JP (cand L8), basalt-jp /1 (cand L31) and Sofia Sans (cand L33, basalt's face, inside the copy). Wave history: at creation the module carried the basalt import twice and the Charm import twice; f931619 (FIX2-COLON) repointed the delivery imports from the EN Basalt CDN (cdn.scpwiki.com/theme/en/basalt/normalize-min.css and basalt-bedrock-min.css) to basalt-jp /1, colon-encoded the copy's logo URLs (`theme:basalt` → `theme%3Abasalt`) without repointing their host (section 3), and added the Noto Sans JP import with the 'Noto Sans JP' insertion into --UI-font-primary (the P7 supplement, label JPFONT-LOAD, riding inside the colon commit — Per-theme record, item 2); a497307 (FIX4-MECH) removed one duplicate basalt-jp /1 @import and one duplicate Charm @import (KB-65). Assets: the T1 checker's 13 hotlink errors are the EN-storage lines — the copy's eight logo URLs (section 3), the theme's own logo files on scp-wiki.wdfiles.com (--hytoth-logo-1/-2, cand L1082–1083), the hidden gate image, and the basalt artwork in the body exhibits. The original's --logo in its own layer pointed at an EN theme:admo asset (orig L31: basalt-theme-logo.svg in theme:admo's file area); the candidate's corresponding image references were repointed in the port.
- **Why:** P7/T5: the stacks had no Japanese-capable font (the localize lane's item (c)). KB-65: duplicated @imports inside one file are removed. P5/KB-58: re-hosting EN-storage artwork is a posting-procedure act, class (ii). P4: the basalt delivery repoint from the EN CDN to the JP base candidate is the cross-theme ruling's requirement, and FIX2 performed it for the frames and the import — the copy's internal values are the residue section 3 measures.
- **Verify:** `grep -n '@import' candidate.txt` (four lines, as above); `git show f931619 -- pages/theme:hytoth-two-jp.txt` (31 changed lines) and `git show a497307 -- pages/theme:hytoth-two-jp.txt` (the two duplicate removals).
- **Disposition:** P7 FIXED (ledger (c3), recorded there as "font wave"; the bytes sit in FIX2-COLON). P4 and P5 DISPOSITIONED (ledger (c3): P4 delivery class (ii); P5 class (ii) / KB-58), with the copy's internal logo values carried as the section 3 flag rather than under the P5 disposition, because the disposition was written for asset hosts the theme does not control, while the copy's values shadow a base the campaign does control.

### 5. Header, sidebar, site furniture

- **What:** The header furniture is basalt's, arriving through the copy and the import (section 3); the theme's own layer redefines --logo (cand L1087) and the header artwork variables (HEADERVAR spans cand L43–45 and L100–102 in the copy, cand L1114–1116 in the own layer). The render row's furniture findings are the ≤375 clips of the header tagline and letterhead in both engines and the WebKit-only IMMRAMA header clip, all recorded with the row's large overflow measurements (section 11). No P9 item was charged; the header title text is basalt's furniture, not this theme's strings.
- **Why:** P8/P9 items are charged per theme where the theme's own furniture diverges; here the furniture is the base's, and its JP form is basalt-jp's own package's subject.
- **Verify:** RENDER-ROWS-1 row for this theme; the HEADERVAR spans in classification.json (block B2).
- **Disposition:** Standing; the render items are dispositioned in section 11.

### 6. Text translation

- **What:** The body is translated throughout: the intro prose (with the lineage credits, section 1), the usage text, and the settings documentation (the hidetitle / acs-itemnum / disable-acs-anim explanations in the cand L1648+ region). The classifier's translation mass is 27 TRANSLATION-ANCHORED and 27 TRANS-UNANCHORED blocks, most of them single lines of the documentation body. One in-fiction sample in the settings documentation stands bilingual by design: the English line followed by its Japanese rendering in parentheses, the form a documentation sample takes when the quoted text is itself the subject. The localize lane's item (d) charged two untranslated display-visible in-fiction samples and mixed EN control labels in this region; in the current bytes the region (body cand L1620–1914) contains no untranslated display paragraph (a scan for long Latin-script lines returns none), the samples stand translated or bilingual as above, and the surviving English labels are the parameter names themselves, which are syntax, not prose. No commit after creation touches the region, and ledger (c3) carries no outcome for item (d) by name (Per-theme record, item 3). In-CSS text: the basalt banner comment and the theme's exhibit comment header stay in English (COMMENT-TEXT 1 block; residue class R1, porter-visible only); the CONTENT-STRING firing (B2 spans cand L260–261, L659–660, L764–765, L1339–1340) is basalt's own string content inside the copy.
- **Why:** P10: body and usage text are translated; a quoted in-fiction sample is data the documentation is about, and the bilingual form keeps both the datum and its rendering visible.
- **Verify:** Read orig L26–320 against cand L1620–1914; `awk 'NR>=1620 && NR<=1914' candidate.txt | grep -P '[A-Za-z]{40,}'` (no hits).
- **Disposition:** Standing (the port itself); item (d)'s record state is carried in the Per-theme record.

### 7. Links

- **What:** The intro's wikilinks became explicit EN URLs in translation (LINK-REPOINT ×2): theme:basalt, the second-hytoth hub, theme:foxtrot, SCP-9628 and theme:hytoth are all named as full scp-wiki.wikidot.com URLs in the candidate's prose, because the link targets are EN pages with no JP counterparts in this environment, and the prose's purpose is to credit and point at the originals. The credit block's source link (cand L1619 area) is the required ruling-3 back-reference. The license box's Source line likewise names the EN theme page, verbatim from the original (section 8).
- **Why:** P11 repoints links to JP counterparts where they exist; for attribution links to the original works, the EN target is the correct one.
- **Verify:** `grep -n 'scp-wiki.wikidot.com' candidate.txt` and sort the hits by role (links here, assets in section 4).
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** The structural facts are the delivery composition (section 3) and the exhibit decision: the retained code exhibit holds the theme's own layer only (cand L1915–2414, 500 lines, the same size as the original's exhibit), prefaced by the porter's declaration prose (cand L1913) stating that the theme's CSS and the base are inlined in the page and that what follows is the theme-specific part. That prose is the porter's documentation, and it is accurate. The license box is retained whole: the includes repointed to `:scp-jp:component:license-box-theme` / `license-box-end` (cand L2420, L2432; blocks B67/B68) and the box's contents byte-identical to the original's (the logo_sh.svg / logo_sh_2.svg entry by badooga, the logo_sh.png entry by Taoka, both CC BY-SA 3.0, with the EN Source line). The classifier's "restoration (KB-63)" note on B67/B68 does not apply: the box was never dropped, so nothing was restored; it is a kept box with repointed includes, and its contents stay in English because they are the box's data, carried verbatim as license entries are. The content census otherwise maps one-to-one: gate, frames, modules, credit, prose, settings documentation, theme-squares, exhibit, license box — every original region has a named fate in these sections.
- **Why:** Residue class R3: structural decisions are stated with their grounds so a reviewer can tell a declared composition from a silent one; the declaration at cand L1913 is what makes this theme's inline the former.
- **Verify:** Read cand L1913–1915 and L2416–2434 against orig L822–840.
- **Disposition:** Standing (the composition is flagged in section 3 on its measured divergence, not on its existence).

### 9. Formatting only

- **What:** The classifier counts 0 re-indentation blocks; whitespace-only churn is inside the translation and copy mass and is not separately blocked. Brace balance, checked by depth with comment- and string-awareness: every channel on both sides ends at depth 0 (the original's two modules and exhibit; the candidate's module, the two parameter modules, the theme-squares module and the exhibit). The candidate's two `http://` strings (cand L2178, L2393) are W3C namespace identifiers inside data-URI SVGs in the exhibit, the known HTTP-KEPT false-positive shape.
- **Why:** The depth check exists because a displaced closing brace keeps the counts equal while swallowing every later rule, and only a depth scan sees it — a live risk in a 1,571-line hand-assembled module, and the scan clears it.
- **Verify:** The depth figures are reproducible by scanning each [[module CSS]] / [[code]] channel of the two files; read cand L2178 in place.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter addition is prose: the declaration at cand L1913 (section 8), which documents the delivery composition in the page itself. It is documentation, not a translator note, and it is accurate against the bytes. No `[!-- ... --]` translator notes exist. The frame, the credit block and the font supplement are accounted for in their own sections.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; this theme's one prose addition is listed here and relied on in section 3.
- **Verify:** Read cand L1913; `grep -n '\[!--' candidate.txt` (no translator-note lines).
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The 13 EN-storage asset lines: T1 hotlink×13, DISPOSITIONED class (ii) (GOSIGN2-LEDGER (c1); (c3) P5, KB-58) — with the section 3 caveat for the eight values inside the basalt copy. (2) The two pseudo-ref errors in the T1 row: recorded by class in the row (T1-ROWS row 108); the vendored row does not itemize their loci. (3) The basalt delivery as it stood at localize time (EN CDN): DISPOSITIONED as original-state delivery, class (ii) (ledger (c3) P4) — superseded in fact by FIX2's repoint to basalt-jp, which the ledger text predates. (4) The hidden-rate machine values in the render row: DISPOSITIONED (ledger (c2), KB-50: the eye check contradicted the machine reading; hidden-rate values are recorded only). (5) The render measurements: page-overflow 533/548px at 320/375 and 1433–1438px at 1366 plus 972px at 768, the ≤375 header tagline and letterhead clips, and the WebKit-only IMMRAMA header clip: DISPOSITIONED with the render row as the cross-cutting overflow and clip families (ledger (c2)); the row also records the cdn.scpwiki.com carry-over under the Basalt exception as it stood at render time. (6) Localize item (d): no outcome recorded by name in (c3); the current bytes are as section 6 states, and the theme passed with no OPEN items. No item is left as an unexplained exception; the inline copy (section 3) is a flag, not a disposition, and is therefore not in this list.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place, and so an item no register decided is visibly absent from it.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–5); item 6 recorded.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 15 errors / 0 warns / 1 info; the errors are hotlink×13 and pseudo-ref×2 (T1-ROWS row 108). (b) T2/T3 render: FINDINGS, all items dispositioned in (c2) (section 11, items 4–5); engine coverage is the lane's full matrix as run (RENDER-ROWS-1, RENDER-S2-B). (c) T4 localize plus follow-up: FINDINGS with 4 items (LOCALIZE-ROWS row 98); outcomes P4 DISPOSITIONED / P5 DISPOSITIONED / P7 FIXED (ledger (c3)), item (d) as section 6 states. (d) T5: judged jointly with T4. (e) The delivery measurements in section 3 were made for this package from the repo's own files (the candidate against pages/theme:basalt-jp.txt), and the audit's basalt-jp /1 MATCH classification is in R/review-scout/FIX-CODEADDR.md. (f) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (68 change blocks) and the generator's (diff.md: +1689/−95 in 11 sections); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:hytoth-two-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 98).

## Per-theme record

### Item 1 — the inlined basalt copy and its eight cascade-live EN-host values (flag)

Measured in section 3: the candidate's module carries a 1,068-line Basalt-derived region, 0.975-similar to theme:basalt-jp's fragment 1 with 42 differing lines, and the module also @imports that same fragment (cand L31), so the copy's differing values win. Eight of the differences are host forms of the same artwork: --logo (cand L42) and seven --memo-logo values name scp-wiki.wikidot.com/local--files/theme%3Abasalt/... where basalt-jp names sigma10-jp-test.wdfiles.com/local--files/theme%3Abasalt-jp/.... The own layer redefines --logo (cand L1087), so that one is not live; the seven memo logos are live. FIX2-COLON colon-encoded these URLs in place (theme:basalt → theme%3Abasalt) and repointed the frames and the import to basalt-jp, but did not repoint the copy's internal values. The flag is referred to the coordinator with the distinguishing facts stated in section 3 (declared inline, current copy, enumerated differences): whether this theme should be rebuilt onto pure @import layering, as alcur-theme-jp was, is a coordinator decision; this package does not edit the candidate.

### Item 2 — wave attribution: the "font wave" for this file is inside FIX2-COLON

Ledger (c3) records P7 as "FIXED (font wave)". No font-wave commit touches this file: the history is a869415 (creation), f931619 (FIX2-COLON), a497307 (FIX4-MECH), and the Noto Sans JP import and the --UI-font-primary insertion are in f931619's diff, in the same commit that repointed the basalt delivery from the EN CDN to basalt-jp /1. The bytes are right; the record's wave name is wrong for this theme. The same pattern recurs across this batch and in the ambrose package's FIX-CREDIT-D.

### Item 3 — localize item (d) has no traceable outcome

LOCALIZE-ROWS row 98 charges, as item (d), two untranslated display-visible in-fiction samples and mixed EN control labels in the settings-documentation region. Ledger (c3)'s outcome line for this theme names P4, P5 and P7 only. No commit after creation touches the region, and the current bytes show the samples translated or bilingual (section 6). Either the lane examined a pre-integration draft of the EN11 delivery, or the bilingual form is the answer it accepted without a (c3) line; the integrated file's history cannot decide between the two. Recorded as a record gap, with the current byte state stated in section 6 so a reviewer need not take the gap on trust.

### Post-package repairs (REFRESH3-I) — hytoth-two rebuilt on its original's import form (landing 45976a8)

The flag in Item 1 above described this package as built; the coordinator has since ruled on it and landed the repair. `FIX-HYTOTH.md` (campaign scout folder) is the item record and `GOSIGN2-SUPERVISOR-STATE.md` §"Main-chat rulings landed 2026-11-17" carries the ruling's grounds (brief level: **main-chat ruling 8** / hytoth branch 2a). The landing is canonical commit `45976a8f2cf8f9266e96fa5399f3a3bbeb254f7b` ("pages: hytoth-two rebuilt on its original's import form", 2026-11-17), which postdates this package's build at `7c640f1` (U-6 batch). `candidate.txt` has been recopied from the current canonical `pages/theme:hytoth-two-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`; the regenerated stamp reads **STALE** by design — no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

The ruling's topology test held branch 2a: the original includes the Basalt theme page (orig L11) and never copies it; its single code block (orig L322–821) is the theme's own layer with `--basalt-*` overrides that presuppose an imported base; the "Version 2.1.0 / Built on Bedrock" Basalt banner and body existed only in the port. "Alcur with better manners": the full rebuild follows the alcur terms (precedent `FIX-ALCUR.md`, 5506feb), with the candidate's existing `theme%3Abasalt-jp/1` @import as the sole base channel. What changed in the candidate, 2,434 → 1,400 lines (+9/−1,043):

- The 1,068-line inlined Basalt copy (old module L35–1066, 159 rules) was deleted. Its four head @imports stay in their old relative order — Charm (L7), Noto Sans JP (L8), `theme%3Abasalt-jp/1` (L9, the sole base channel), Sofia Sans (L10) — followed by a short delivery-note comment (L12–19) in place of the departed Basalt banner.
- Three rules with no counterpart in current basalt-jp/1 were preserved verbatim at the head of the override layer (L21–31): the `#revision-list` history-column rule, the `div.anom-bar > div.top-box` grid rule, and the `table` margin rule — the same three selectors alcur preserved.
- The theme's own layer (83 rules + 2 keyframes, including its banner) is byte-verbatim, relocated from old L1067–1575 to L33–541.
- The source-code prose line (old L1913) was corrected from the false declaration that the CSS and Basalt base were inlined to the delivered form: the theme's CSS is served from the head module and Basalt 2.1.0 is @imported from theme:basalt-jp.
- Cascade gate (FIX-HYTOTH §4): identical expanded import multisets and 667 winner keys in both forms, 0 keys unique to either side, and exactly 8 winner differences — D1–D7 the memo-logo `--memo-logo` stops being shadowed by the copy's stale EN-host URL and takes basalt-jp's JP-host URL, D8 the porter-era `--UI-font-primary` `'Sofia Sans', 'Noto Sans JP'` → `'Sofia Sans'` (JP glyphs remain delivered via basalt-jp's separate fallback variables). No `theme%3Abasalt/` EN-host path survives.
- Checker (FIX-HYTOTH §7): 14 → 6 errors (the 8 inlined-copy hotlinks removed), no new finding of any class, 0 class (i) before and after. The remaining 5 hotlinks + 1 pseudo-ref are the theme's own standing asset/delivery classes.

## Change set outside the two diffed files

The theme layers over theme:basalt-jp, whose own package (review/basalt-jp/) carries the base's provenance; section 3's measurements read that canonical file but do not change it. Otherwise none: no other canonical file carries part of this port. The two wave commits are shared vehicles — f931619 (FIX2-COLON) touched 18 theme files and a497307 (FIX4-MECH) touched 29; this file's hunks in each are narrated in sections 3–4 and in Multi-wave provenance.

## Multi-wave provenance

| Commit | Wave | What it changed in this file |
|---|---|---|
| a869415 | Stage 2 EN11 creation | The whole port in its K5b composition: the basalt body and the theme's own layer inlined into one module, the parameter mechanism reproduced as gated modules, two frames naming the EN Basalt CDN files, the credit block added, the info module removed, the body and documentation translated (one sample bilingual), the usage exhibits simplified, the license box retained with repointed includes, the exhibit retained as the theme's own layer with the declaration prose |
| f931619 | FIX2-COLON | The basalt delivery repointed from cdn.scpwiki.com (EN Basalt CDN) to theme:basalt-jp /1 in both frames and the module import; the copy's logo URLs colon-encoded in place (KB-01) without host repoint; riding in the same commit, the P7 supplement: Noto Sans JP @import added and 'Noto Sans JP' inserted into --UI-font-primary. 31 changed lines |
| a497307 | FIX4-MECH | Two duplicate @imports removed (KB-65): one basalt-jp /1 import and one Charm import; the live module's census is now exactly four @imports (section 4) |

## Appendix — heuristic and residue blocks

The 23 heuristic and 6 residue blocks resolve by shape:

- **B2** (orig L5–7 → cand L5–1602, the delivery restructure): the differ anchors the original's frame-and-include head against the candidate's whole delivery composition. Its fourteen labels are the composition's parts, each decided in its section: IFTAGS, SELF-DELIVERY and DRAFT-HOST (the frames), DELIVERY-HOST and DELIVERY-MOVE (the repoint and the inline), FONT-IMPORT and JPFONT-LOAD (section 4), HEADERVAR and CONTENT-STRING and T7-CREDIT-CSS (spans inside the copy: cand L43–45, L100–102, L1114–1116; cand L260–261, L659–660, L764–765, L1339–1340; cand L1245–1250), COMMENT-TEXT (the basalt banner), TRANS-UNANCHORED (the copy's unanchored mass) and EXHIBIT-RESTRUCTURE. The block's "script delta without the anchor majority" note is the expected shape for a 1,571-line composition anchored on a 3-line original region.
- **The single-line translation blocks** (B6, B10, B12, B18, B20, B21, B23, B25, B27, B43, B45–B49, B56–B60 and their kin, TRANS-UNANCHORED with the same note): one-line prose and documentation translations in the body (orig L22–307 → cand L1623–1898). Resolved by the section 6 reading: the body is translated throughout, and the localize T5 pass is the check that covers unanchored translation.
- **B62** (orig L318 → cand L1909): the "Source Code" section's in-fiction line (Rakmou-leusan's hope), translated. **B63** (orig L320 → cand L1911–1913): the collapsible labels translated, with the declaration prose (cand L1913) entering in the same block. **B64** (orig at L323 → cand L1916, body → code-css, no signature): the exhibit's opening boundary — the original's exhibit comment header against the candidate's exhibit opening, displaced by the added declaration prose; the exhibit body itself is the retained own layer (section 8). **B66** (orig at L822 → cand L2415, no signature): blank-line placement at the exhibit's close, formatting only.
- **B17** (orig L72 → cand L1661, EXHIBIT-RESTRUCTURE): the theme-squares exhibit line, repointed with the component; the label's "no translated counterpart" note is the differ's, and the counterpart is the repointed include itself (section 2).
- **B52** (orig L299 → cand L1890, LINK-REPOINT): one of the intro's EN-URL link conversions (section 7).

## License and attribution

- **Title:** Second Second Hytoth Theme
- **Author:** badooga
- **Source:** https://scp-wiki.wikidot.com/theme:hytoth-two — revision 30
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
