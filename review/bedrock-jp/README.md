# Review package — theme:bedrock-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:bedrock-jp — origin EN, population #4 [GOSIGN2-LEDGER (b) row 4]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 692df2a06030f22508215e6d5b185c8eabbeb9139afc2ca20a22b1116f818702); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 0 warns / 2 infos (hotlink×2, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 4; GOSIGN2-LEDGER (b) row 4]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — mobile header/page overflow 440/445px both engines (logo + menu clipped), sample credit-modal, contrast 1.66 undetermined visually; cdn.scpwiki.com Basalt-logo reference. [RENDER-ROWS-1 (RENDER-A row 4)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 4)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 6 [LOCALIZE-ROWS row 5, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 5]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 4]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:bedrock-jp.txt sha256:692df2a06030f22508215e6d5b185c8eabbeb9139afc2ca20a22b1116f818702; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/bedrock-jp/candidate.txt (sha256 356fef9dc42eff46012ae93c801f361334f23dd9b52e70c5238247e4ab7f3bbd)
Original: theme:bedrock — scp-wiki, revision 21 (sha256 7f62a64c055d179d4b51746812fc8f288fd479661219bc3e607036c69dc86da5)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 4); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no bedrock entries |
| Fixed after the localize check | The pattern-4 delivery repoint (FIX-P4, commit f1138e4: the EN CDN Basalt delivery replaced by theme:basalt-jp) and its duplicate-@import cleanup (FIX4-MOPUP, commit 379eb44); the credit furniture was assembled across three earlier waves (see Multi-wave provenance) |
| Standing items | **DISPOSITIONED** — T1 hotlink×2 (the basaltlogo.svg pair, KB-58) and pseudo-ref×2 (draft-host delivery, classes (ii)/(iii)); the render row's mobile overflow and credit-modal lines (cross-cutting families; credit modal in preview form); pattern 5 (KB-58) |
| Flagged by this package | The usage exhibit's self-reference named the plain slug (candidate L79), since completed to the `-jp` posting name by the usage sweep (b5cb724; per-theme record); and a record conflict: the ledger's (c3) outcome for pattern 4 says DISPOSITIONED (original-state CDN delivery) where the bytes show a repoint to the JP candidate — see the Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:bedrock | theme:bedrock-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 21 (created 2024-01-08 13:14:12 UTC), as recorded in the candidate's credit block: **初訳時参照リビジョン:** 21 | — |
| Source of this copy | Fetched 2026-11-17 at the recorded revision (mirror-store class FETCH-REGEN; whitespace-only against its cache) | Canonical file `pages/theme:bedrock-jp.txt`; its content history runs from the canonical-sources commit d727e92 through 379eb44 (see Multi-wave provenance) |
| Lines / bytes | 285 lines / 9,879 bytes | 350 lines / 13,200 bytes |
| SHA-256 | 7f62a64c055d179d4b51746812fc8f288fd479661219bc3e607036c69dc86da5 | 356fef9dc42eff46012ae93c801f361334f23dd9b52e70c5238247e4ab7f3bbd |

Provenance route: derived from the original at the reference revision (sources.tsv kind: K5b-3). No production counterpart was adopted (no R4). The K5b-3 note in sources.tsv records the layering this package's diff must be read with: the candidate layers over theme:basalt-jp, so the original's head delivery (the compiled Basalt stylesheets on the EN CDN) corresponds to basalt-jp's /1 as a whole, and the line-level diff below covers the theme's own layer — its prose, its three variable exhibits, its tail module, and the credit supplement appended to it.

## Summary

Bedrock is the foundational layer of Basalt 2.0: the original page delivers the compiled Basalt bedrock stylesheets live from the EN CDN (cdn.scpwiki.com) and spends its own text on documentation — a theme-squares palette exhibit, three code exhibits defining the color, font and header variable layers, usage prose and a tail module with the nametag artwork. The candidate keeps that documentation entire and translated, and changes where the foundation comes from: FIX-P4 repointed all four CDN delivery lines to theme:basalt-jp's local--code /1 on the draft host, and FIX4-MOPUP removed the duplicate @import that repoint had written twice. The credit block was assembled in three passes (fields, translator pair, frame) before FIX-P4 normalized its translator value in passing. A 58-line credit-module CSS supplement in the in-place correction form (R6) closes the candidate. Measured churn (diff.md, the generator's count: +186/−127 in 4 hunks; the classifier counts 72 change blocks) is mostly the documentation translation. Two flags ride in the Per-theme record: the usage exhibit's plain-slug self-reference, since repaired by the usage sweep (b5cb724), and the ledger's pattern-4 outcome word, which the bytes contradict.

## Classification

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 35 |
| TRANSLATION-ANCHORED | 20 |
| INCLUDE-REPOINT | 5 |
| EXHIBIT-RESTRUCTURE | 4 |
| DELIVERY-HOST | 3 |
| DRAFT-HOST | 3 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| ESCAPED-INCLUDE | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Counts: 72 blocks — 31 specific (43.1%), 34 heuristic (47.2%), 7 residue (9.7%), 0 skipped. Topology: no relocation; the original's three code-css exhibits (orig L176–199, L202–210, L213–226) are the candidate's at the same relative positions (cand L184–207, L210–218, L221–234), and the tail module-css matches (orig L239–284 → cand L247–292). Labels are sets per block; the skeleton lists each block once under its primary label, so these sections were written from classification.json's label spans: the skeleton's section 4 prints no JPFONT-STACK although the font-exhibit stack rewrites sit inside B65 (labeled CSS-BODY), and its residue appendix holds seven theme-squares name translations the skeleton's section 6 does not list.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–14) is pure delivery: a module CSS @importing the two compiled Basalt files from cdn.scpwiki.com (normalize-min.css, basalt-bedrock-min.css; L1–4) and a `[[div_]]` pair of `:scp-wiki:` interwiki-style includes at priority=1 and priority=2 naming the same two files (L5–14). The candidate's head (L1–13) names one source instead: theme:basalt-jp's /1 on the draft host, by module-CSS @import (L2) and by two `:scp-jp:` interwiki-style includes at priority=1 and priority=2 (L5–12) — the layering shape is the original's, the source is the JP port candidate. The gate follows (cand L15, `[[iftags +テーマ]]`). Provenance route: derived from the original at reference revision 21, layered over basalt-jp (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P1/P2/P4/P6 rework exactly this frame, and each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–16 against candidate L1–15; blocks B1–B6 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside the nametag div (orig L17–20) and its prose attribution (orig L22: created by EstrellaYoshte, Liryn and Placeholder McD, with thanks to aismallard and Woedenaz). The candidate deletes the bare Rate (B7, orig L19) — the nametag div survives without it (cand L27–29) — and installs the preview credit block (cand L17–26, B6): all eight ruling-3 fields, with 著作権者 naming all three creators (EstrellaYoshte、Liryn、Placeholder McD), matching the original's prose exactly; the thanks to aismallard and Woedenaz survive in the translated prose (cand L31). The block was assembled in three passes (Multi-wave provenance): the T1-fix wave added the title/holder/year fields (b816e10), FIX-CREDIT-C added the translator pair (5c32672), and the Phase 17 pass added the frame includes with the revision and source-link fields (8dcac74); FIX-P4 later normalized the translator value to AI. The T7 supplement is the candidate's tail module (cand L295–350, B72): not the basalt 8-selector set but the in-place correction form (R6) — two scoped rulesets (`.creditButton > a` under the two current credit-module containers, with their ::before/::after companions) preceded by an English porter comment explaining the mechanism (the frozen JP markup emits `.creditButton > a`; the source Bedrock rules cover `.creditButton > p > a`). No license box exists on either side, and none was charged (KB-63 covers dropped boxes; this original never had one).
- **Why:** P3/T1: the preview credit module is rate-bearing, so the bare Rate beside it would duplicate the widget (KB-09). Ruling 3 fixes the eight fields. T7/R6: the credit module's JP markup differs from the markup Bedrock's inherited rules were written for, so the correction is scoped to the two containers that occur, rather than importing a foreign selector set.
- **Verify:** Read candidate L17–26 against the eight-field list and original L22; `grep -n 'module Rate' candidate.txt` (absent) against original L19; read candidate L295–350; `git show b816e10 5c32672 8dcac74 -- pages/theme:bedrock-jp.txt` for the three assembly passes.
- **Disposition:** Standing (the port's credit form). The render row's sample credit-modal line is dispositioned preview-form (the stamp's credit-modal line: credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ruling 5).

### 2. Includes and components

- **What:** The candidate's include list (grep): the two interwiki-style frame includes (L5–12), the credit pair (L17/L26), the theme-squares component repointed to `:scp-jp:` (cand L35, B10), the image-block component repointed to `:scp-jp:` (cand L87, B24), and the escaped usage include (cand L79, B21). Changes: (a) both frame includes repointed in site and target (section 3); (b) theme-squares and image-block repointed `:scp-wiki:` → `:scp-jp:` with their parameters carried (the squares' color names translated, section 6); (c) the usage exhibit repointed to `:scp-jp:`; its plain slug was completed to the `-jp` posting name by the sweep (b5cb724), closing the flag recorded in the Per-theme record. No `:scp-wiki:` include remains (grep: none). No T8 component swap was needed; ruling 4 does not engage.
- **Why:** P1: foreign-site includes are repointed to the JP counterpart that actually exists on scp-jp (KB-15); both components have JP ports.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the lists.
- **Disposition:** Standing; the cand L79 self-reference flag is closed by the sweep repair (b5cb724; Per-theme record, item 1).

### 3. Delivery and code loading

- **What:** The original delivers its entire foundation live from the EN CDN: the two compiled files at the head (section 0), whose chain runs on through the CDN's own references (the LOCALIZE-ROWS row 5 charge names the cdn.scpwiki.com + rsms.me chain). That was the pattern-4 charge: original-site code delivery, display/integrity — the theme's rendering depended on the EN branch's CDN staying put. FIX-P4 (commit f1138e4, "pattern-4 repoint of base-theme CSS imports to JP port candidates, 39 files") repointed all four delivery lines in this file to theme:basalt-jp's /1 on the draft host (cand L2, L7, L11): the module @import and both interwiki theme= URLs. The same commit also normalized the translator field and removed the bare Rate (its subject names only the repoint; the bytes show three acts — Per-theme record, item 2). The repoint wrote the module @import twice (a KB-65 duplicated @import); FIX4-MOPUP (commit 379eb44, this package's computed-against commit) removed exactly one of the two identical lines, and the current bytes carry one (cand L2). The theme's own layer needs no delivery of its own beyond the exhibits: its code blocks are documentation exhibits, and its tail module (orig L239–284 → cand L247–292) is gated body content, as in the original. The two interwiki priorities (1 and 2) both naming /1 preserve the original's two-layer registration shape over a single JP source (the K5b-3 layering, see Provenance).
- **Why:** P4/T9 and ruling 1: a dependent theme imports the JP port candidate of its base, never the raw upstream delivery; the failure prevented is the port's rendering depending on the original branch's CDN (and, for the duplicate, KB-65's double-load of the same stylesheet).
- **Verify:** `git show f1138e4 -- pages/theme:bedrock-jp.txt` (four delivery lines repointed, the @import written twice); `git show 379eb44 -- pages/theme:bedrock-jp.txt` (one @import removed); `grep -n 'cdn.scpwiki.com' candidate.txt` (only the basaltlogo.svg references of section 4 remain).
- **Disposition:** The delivery is FIXED by repoint in the bytes. The ledger's (c3) outcome line for this theme reads "P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery)" — that is the pre-fix adjudication class, and it does not describe the current bytes; the conflict is recorded in the Per-theme record (item 2) and this package follows the bytes. The draft-host form of the /1 URLs is class (iii), recorded in section 11.

### 4. Fonts and assets

- **What:** Fonts live in this theme's documentation, not its delivery: the font exhibit (orig L202–210 → cand L210–218) defines the four Basalt font variables. B65 (labeled CSS-BODY; orig L204–208 → cand L212–216) appends a JP fallback to each of the four stacks: 'Noto Sans JP' to the Lexend, Jost and Inter stacks, 'Noto Sans Mono CJK JP' to the JetBrains Mono stack. No JPFONT-LOAD fired and none was needed for the three Noto Sans JP stacks: the resolved base loads the face (theme:basalt-jp's delivery imports Noto Sans JP from Google Fonts — `pages/theme:basalt-jp.txt` L113), so the KB-16 base-subtraction check passes. The mono fallback names a system CJK face that no import in either file loads; it sits in an exhibit (the live stacks are the base's), and if the face is absent the stack falls through to the generic monospace — recorded here as an observation, not charged. Assets: the basaltlogo.svg reference survives twice on the EN CDN — the image-block exhibit's name= (cand L87) and the header exhibit's --header-logo (cand L224) — the T1 hotlink×2 and the render row's "cdn.scpwiki.com Basalt-logo reference". Everything else visual is data-URI or variable content carried verbatim (the nametag SVG, cand L248–, byte-identical; its embedded W3C namespace string is not an HTTP reference).
- **Why:** P7/T5: Latin-only stacks need a JP fallback so Japanese text does not fall back to an OS-dependent generic. P5/KB-58: the logo asset's re-hosting is a posting-procedure act and re-upload is barred by owner order, so the original-state host stands as a recorded disposition (the FIX3-A1 §4 record leaves the basaltlogo references as re-upload-barred leftovers).
- **Verify:** Read orig L202–210 against cand L210–218; `grep -n 'basaltlogo' candidate.txt` (L87 and L224); `grep -n 'Noto Sans JP' pages/theme:basalt-jp.txt` for the base load.
- **Disposition:** Fonts standing (the port's supplement, inside an exhibit). Assets DISPOSITIONED (GOSIGN2-LEDGER (c3): P5, class (ii) / KB-58; (c2): the Basalt-logo reference).

### 5. Header, sidebar, site furniture

- **What:** HEADERVAR fired once (B67, orig L216–218 → cand L224–226): the header exhibit's variable block, where the candidate translates the exhibit's own strings — --header-title 'SCP Foundation' → 'SCP財団', --header-subtitle 'SECURE - CONTAIN - PROTECT' → '確保 - 収容 - 保護' — while --header-logo keeps the CDN URL (section 4). These are documentation copies of the variables (the live values are the base delivery's), exhibited so users can override them; the translation makes the exhibit usable in Japanese. No sidebar or topbar adaptation was made (P8 does not engage; the furniture is Basalt's). The render row's mobile overflow (440/445px, logo + menu clipped) is a sample-render family item, in section 11.
- **Why:** P9/T6 concerns the live variable overrides; an exhibit's strings are body text (P10) and translate with it. Ruling 2 (header language out of scope) is not needed here and was not charged: the LOCALIZE row's six display-affecting findings are the pattern-4/5 delivery items, not the header strings.
- **Verify:** Read orig L213–226 against cand L221–234.
- **Disposition:** Standing (exhibit translation). No header-language disposition is claimed for this theme.

### 6. Text translation

- **What:** The candidate's prose is the original's documentation translated in place, entire: the intro (B8–B9), the theme-squares palette exhibit with its twelve color/subcolor names translated (Quartz → 石英， Calcite → 方解石， Lapis Lazuli → ラピスラズリ, Amethyst → アメジスト, Granite → 花崗岩， Andesite → 安山岩， Sunstone → 日長石， Slate → 粘板岩； blocks B11–B17 and the heuristic B12–B13), the usage prose (B21's zone), the examples body (B26–B61: specimens, the calc() usage notes at orig L228–230 → cand L236–238, the "Other" section), and the exhibit captions ("The four font types used by Bedrock." → 「Bedrockで使用される4種類のフォントです。」). 20 blocks are anchor-paired; the 35 TRANS-UNANCHORED blocks and the 7 residue blocks are the same work in shapes the anchors miss (include-parameter values, one-line headings, script-delta prose) — each was read against its original line, and all are translations. One sentence keeps an EN link target by form change (B9, section 7). In-CSS text (R1): the tail module's rules are carried verbatim, including the data-URI artwork; the only in-CSS additions are the T7 module's comments (section 10).
- **Why:** P10: body, usage and exhibit text are translated, including the theme-squares' display names (they are reader-visible labels in the rendered palette). Parameter values that are identifiers (the --basalt-* variable names, the RGB infos) are carried unchanged, which is why the name lines pair as residue: only the display name on each line changed.
- **Verify:** Read orig L22–237 against cand L31–245; `grep -n 'color1-name\|subcolor1-name' candidate.txt` for the palette names.
- **Disposition:** Standing (the port itself). The localize T5 pass recorded no mistranslation finding for this theme; its findings are the delivery items (sections 3–4).

### 7. Links

- **What:** Three link shapes. (a) B9 (orig L24 → cand L33): the intro's Basalt 2.0 link — the original's same-site `[[[theme:basalt|Basalt 2.0]]]` becomes a full-URL link to the EN page, `[https://scp-wiki.wikidot.com/theme:basalt Basalt 2.0]`: the sentence is about the original work, and the link names it on its home wiki. (b) The "Other" section's GitHub link (orig L234 → cand L242): the Basalt team's page, kept byte-identical as an external reference. (c) The credit block's source link (cand L25) names the recorded host scp-wiki.wikidot.com, matching sources.tsv; no probe was needed. No prose link in the candidate points at a JP page that does not exist; the usage exhibit's include form is section 2's flag, not a prose link.
- **Why:** P11 repoints links to JP counterparts where the link's referent is the JP-side page; where the referent is the original work itself (its theme page, its team page), the original target stands.
- **Verify:** Read cand L33 and L242 against orig L24 and L234.
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** The localize.md closing rule is honored for the theme's own layer: the three exhibits keep their order and contents (the color exhibit is byte-identical, cand L186–207 = orig L178–199), the tail module's rules are verbatim, and the JP corrections sit at the head delivery, the font exhibit's stacks, and the appended T7 module after the gate (cand L295–350) — the closing position for supplements. The four EXHIBIT-RESTRUCTURE labels adjudicate as follows: B2 and B4 (orig L5–13 → cand L4–12) are the head delivery zone (the interwiki includes), decided in section 3; B10 (orig L26 → cand L35) is the theme-squares include line — the exhibit survives with its include repointed and its parameters translated; B24 (orig L77–78 → cand L86–87) is the image-block include line inside the examples — the exhibit survives with its include repointed and its caption translated. The exhibit census (theme-squares, three code exhibits, image-block, footnote specimen, toc) is identical on both sides; nothing was dropped.
- **Why:** Residue class R3: the ground is stated per block; here the census decides — every exhibit the original carries is present in the candidate.
- **Verify:** `grep -n 'theme-squares\|code type\|image-block\|footnote' original.txt candidate.txt` and compare the lists; blocks B2/B4/B10/B24 in classification.json.
- **Disposition:** Standing (no structural deletion).

### 9. Formatting only

- **What:** none — no WS-ONLY label fired over 72 blocks and the classifier counts 0 re-indentation pairs. The candidate's exhibits keep the original's indentation (the color exhibit is byte-identical, section 8).
- **Why:** Formatting-only churn is disclosed as its own class; here the ground for "none" is the classifier's count over the pair.
- **Verify:** classification.json (label counts; reindent_blocks 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two porter additions, both inside the T7 module (B72): the comment header "SCP-JP Wikidot Bedrock credit controls: support the native direct-child anchor shape." (cand L296) and the mechanism comment "The frozen JP component markup emits .creditButton > a, while the source Bedrock rules cover .creditButton > p > a. Keep this correction scoped to those two current credit-module containers." (cand L297). Both are in English and both are porter-visible only (CSS comments in an appended module). No `[!-- ... --]` notes and no body 訳注 exist (`grep -c '\[!--' candidate.txt` = 0).
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here they double as the supplement's own documentation (section 1).
- **Verify:** Read cand L295–298.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The two basaltlogo.svg references (cand L87, L224): T1 hotlink×2 — DISPOSITIONED, class (ii) / KB-58 (original-state asset reference; re-upload barred; GOSIGN2-LEDGER (c2) and (c3)). (2) The draft-host delivery URLs (cand L2, L7, L11): T1 pseudo-ref×2 as extracted in T1-ROWS row 4, over the candidate's draft-host delivery lines (cand L2, L7, L11) — DISPOSITIONED, class (iii) draft form (register (c1)). (3) The render row's mobile header/page overflow 440/445px on both engines (logo + menu clipped): DISPOSITIONED in the cross-cutting page-overflow families (KB-33/KB-34; GOSIGN2-LEDGER (c2)). (4) The sample credit-modal line: DISPOSITIONED preview-form (credit:start-preview has no modal mechanism; ruling 5). (5) The contrast 1.66 pair in the render row: recorded by the lane as undetermined visually; no register raises it to an item for this theme. (6) FLAGGED by this package and since repaired: the usage exhibit's plain-slug self-reference (cand L79) — Per-theme record, item 1; the sweep (b5cb724) completed the `-jp` posting name. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–5); item 6 was flagged with evidence and has since been repaired by the sweep (b5cb724), closing the flag; the frozen ledger verdict stands and the stamp reads STALE against it by design.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 4 errors / 0 warns / 2 infos; the errors are hotlink×2 and pseudo-ref×2 (section 11, items 1–2); the info codes are not itemized in the extracted row (T1-ROWS row 4). The T1-fix wave's credit work on this file is checker-verified in its wave record (b816e10). (b) T2/T3 render: FINDINGS — the overflow, credit-modal and contrast lines, all dispositioned in (c2) (section 11); engine coverage is the lane's full matrix as run (RENDER-ROWS-1, RENDER-A row 4). (c) T4 localize: FINDINGS with 6 display-affecting items (LOCALIZE-ROWS row 5), all of them the pattern-4/pattern-5 delivery charges — pattern 4 answered by the FIX-P4 repoint (section 3), pattern 5 dispositioned KB-58 (section 4). The follow-up (T4) currency question does not arise in the same form: the mirror was re-fetched at the reference revision for this package (FETCH-REGEN, whitespace-only against the cache). (d) T5: judged jointly with T4 by the source lane; no mistranslation finding stands. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (72 change blocks) and the generator's (diff.md: +186/−127 in 4 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:bedrock-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 4).

## Per-theme record

### Item 1 — the usage exhibit names a page that will not exist (repaired)

As built, the usage exhibit read `> {{@@[[include :scp-jp:theme:bedrock]]@@}}` (cand L79). The original's line names `:scp-wiki:theme:bedrock` (orig L69) — correct on its own wiki. The port repointed the site prefix but kept the plain slug; the candidate posts as theme:bedrock-jp, so the exhibit instructed readers to include a page that will not exist under that name on scp-jp. No register charged the line. The usage-example population sweep completed the reference to `> {{@@[[include :scp-jp:theme:bedrock-jp]]@@}}` (sweep report SWEEP-USAGE.md in R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates, and U-3's batch report (BATCH-U3.md, flag F1) independently recorded the same line. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design. The U-3 repair landing (FIX-U3.md, canonical commit 49cfb90) touched only bloodraven and black-serpent — this theme's U-3 involvement was the sweep line, not that landing.

### Item 2 — two record conflicts, resolved for the bytes

(a) Pattern 4's outcome word. The ledger's (c3) line for this theme reads "P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery)". The bytes show a fix, not a disposition: FIX-P4 (f1138e4) repointed all four delivery lines from cdn.scpwiki.com to theme:basalt-jp, and FIX4-MOPUP (379eb44) cleaned the duplicate the repoint introduced. The (c3) wording preserves the adjudication class the charge was filed under before the fix wave ran; the theme's PASS does not depend on the wording, but a reviewer reading only the register would believe the candidate still loads the EN CDN. It does not (`grep -n 'cdn.scpwiki.com' candidate.txt` returns only the two basaltlogo.svg asset references). This package follows the bytes. (b) FIX-P4's subject understates its diff: the commit named for the delivery repoint also normalized the translator field (SCP-JP → AI) and removed the bare Rate in this file. The register attributes the Rate deletion to the credit waves generally; the git diff assigns it to f1138e4. Outcomes match; commit-level attribution differs, and this package follows the git record.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-bedrock-jp.txt` — the render sample page the T2/T3 checks rendered. (2) `pages/theme-decoration-sample-bedrock.txt` — the EN sample's page. (3) The base itself: theme:basalt-jp, whose /1 the candidate's frame loads (cand L2, L7, L11) and whose own review package carries the base-side story; this package's diff deliberately covers bedrock's own layer only (the K5b-3 reading, see Provenance).

## Multi-wave provenance

The candidate's current state is the product of seven commits and three check waves: the file entered the canonical repo with the display-check composition sources (d727e92) and was reconciled to the live pair state (ffad285); the Phase 17 pass recorded the reference revision and completed the credit frame (8dcac74); the T1-fix wave added the credit block's title, holder and year fields (b816e10); FIX-CREDIT-C completed the translator pair (5c32672); LOCALIZE-A then charged the pattern-4/pattern-5 delivery items (LOCALIZE-ROWS row 5, 6 display-affecting findings) and the render lane recorded its row (RENDER-A row 4); FIX-P4 repointed the delivery to basalt-jp (f1138e4, also carrying the translator normalization and the Rate removal); FIX4-MOPUP removed the repoint's duplicate @import (379eb44, the file's last content change and this package's computed-against commit); and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 4, (c1) hotlink and pseudo-ref entries, (c2) bedrock entry, (c3) bedrock entry; GOSIGN2-LEDGER-SUPPLEMENT.md (no bedrock entries); T1-ROWS row 4; LOCALIZE-ROWS row 5; RENDER-ROWS-1 (RENDER-A row 4). The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted 17 open blocks (7 residue, 10 heuristic). All are resolved; none required a new signature. The mass is one shape — reader-visible name and heading translations whose lines pair without anchors.

- **R1 — B11, B14–B17 (residue; orig L30–52 → cand L39–61).** Four theme-squares parameter lines (Calcite, Slate, Granite, Andesite, Sunstone names). Resolved in section 6: display-name translations inside the include's parameters; the variable and info values on the same lines are unchanged.
- **R2 — B22, B62 (residue; orig L74, L173 → cand L83, L181).** The "+ Examples" and "+ CSS Variables" headings → 「+ 使用例」「+ CSS変数」. Resolved in section 6 as P10 heading translations.
- **R3 — B9 (heuristic; orig L24 → cand L33).** The Basalt 2.0 intro sentence; carries the link-form change of section 7. Resolved there and in section 6.
- **R4 — B12, B13 (heuristic; orig L33, L37 → cand L42, L46).** Two more theme-squares name lines (Lapis Lazuli, Amethyst). Resolved in section 6, same shape as R1.
- **R5 — B18–B20, B23, B25, B34, B36–B46, B53–B56 (heuristic).** One-line prose and specimen translations across the examples body. Resolved in section 6 by shape; each was read against its original line.
- **R6 — B68, B71 (heuristic; orig L228, L237 → cand L236, L245).** The calc() usage note and the "Other" section's source line, translated. Resolved in section 6.
- **R7 — B65 (heuristic-tier CSS-BODY; orig L204–208 → cand L212–216).** The font exhibit's four stack lines gaining JP fallbacks. The classifier's CSS-BODY label stands as its mechanical reading; the mechanism is the P7 stack rewrite, resolved in section 4.

## License and attribution

- **Title:** Bedrock Theme
- **Author:** EstrellaYoshte、Liryn、Placeholder McD
- **Source:** https://scp-wiki.wikidot.com/theme:bedrock — revision 21 (revision date 2024-01-08 13:14:12)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
