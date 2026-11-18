# Review package — theme:bedbugs-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:bedbugs-theme-jp — origin EN, population #60 [GOSIGN2-LEDGER (b) row 60]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 308c4c7d94d0186579ffc2bd18362761c5b217c4b01fb15f8029895f012d0bc4); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 0 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 65; GOSIGN2-LEDGER (b) row 60]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — port defect: duplicate `interwiki-style` priority=1 (console error every combo; fix to 3) + BHL min-width overflow 337–419px@≤375 on sample. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 60, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 60]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 60]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:bedbugs-theme-jp.txt sha256:308c4c7d94d0186579ffc2bd18362761c5b217c4b01fb15f8029895f012d0bc4; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/bedbugs-theme-jp/candidate.txt (sha256 b10c9bccc87a94e3ba50de41c366a6e0fb986c0f96f6cd39016298fa66466940)
Original: theme:bedbugs-theme — scp-wiki, revision 11 (sha256 b068f980bbfdf2e647e66792719b8d0cf930f8a906f628df59ea5d8d5a51548b)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 60); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no bedbugs entries |
| Fixed after the localize check | The duplicate `interwiki-style` priority (FIX4-IWB, commit 5559209: priority=1 → 3, one line) and the translator-attribution normalization (FIX-CREDIT-D, commit 1869877) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref×3 (draft-host lines, classes (ii)/(iii)); the BHL min-width overflow 337–419px@≤375 on the sample (cross-cutting families KB-33/KB-34); header language under ruling 2; the #6 interwiki registration form as a staff-confirmation item; two images' re-hosting and license confirmation at posting |
| Flagged by this package | The usage exhibit's self-reference named the plain slug (candidate L31), since completed to the `-jp` posting name by the usage sweep (b5cb724) — see the Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:bedbugs-theme | theme:bedbugs-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 11, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 11 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-bedbugs-theme.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:bedbugs-theme-jp.txt`, created in commit 053fd41 (Stage 2 EN4); later content changes in 1869877 and 5559209 |
| Lines / bytes | 314 lines / 8,028 bytes | 349 lines / 10,677 bytes |
| SHA-256 | b068f980bbfdf2e647e66792719b8d0cf930f8a906f628df59ea5d8d5a51548b | b10c9bccc87a94e3ba50de41c366a6e0fb986c0f96f6cd39016298fa66466940 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted (no R4): the candidate's stylesheet is the original's own code exhibit carried in place, and its sample body is the original's, translated. Reference-revision currency: the upstream original has moved past revision 11 since the port; the follow-up artifact `diff-bedbugs-theme-from11.txt` in the campaign record carries that later delta (sources.tsv kind K5a-i). This package judges the port against the revision it was made from.

## Summary

The original is a Black Highlighter (BHL) child theme that loads its base twice over (module-CSS @imports from cdn.scpwiki.com and two EN interwiki-style includes at priorities 1 and 2 from nu-scptheme.github.io), gates a bare Rate module and a full translated-later sample body, and serves its own small stylesheet out of a code exhibit as its local--code /1. The candidate loads the base once, through the JP BHL theme page include, repoints the base's @imports inside the exhibit to the JP BHL distribution (scp-jp.github.io), and delivers its own layer at priority 3 on the draft host. The sample body survives entire and translated; the credit block and an added license box supply the attribution the original never had. Measured churn (diff.md, the generator's count: +188/−154 in 6 hunks; the classifier counts 57 change blocks) is mostly that translation. Two later waves touched the file: FIX-CREDIT-D normalized the translator field, and FIX4-IWB repaired the one real port defect the render check found, the duplicate interwiki-style priority. One exhibit line escaped both waves: the usage example still names the theme by its plain slug (Per-theme record, item 1).

## Classification

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 27 |
| TRANSLATION-ANCHORED | 22 |
| DRAFT-HOST | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| SELF-DELIVERY | 3 |
| DELIVERY-HOST | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| LINK-REPOINT | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Counts: 57 blocks — 32 specific (56.1%), 24 heuristic (42.1%), 1 residue (1.8%), 0 skipped. Topology: no relocation; each side's components match by kind (the original's code-css exhibit at orig L194–305 is the candidate's at cand L200–329, the /1 source on both sides). Labels are sets per block; the skeleton lists each block once under its primary label, so these sections were written from classification.json's label spans: the skeleton's section 5 prints "none" although HEADERVAR fired inside B55, and its section 10 prints "none" although the porter annotations ride inside B50 and B53.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–16) declares base delivery twice (module-CSS @imports of the BHL normalize and BHL stylesheets from cdn.scpwiki.com, L3–6; two `:scp-wiki:` interwiki-style includes at priority=1 and priority=2 naming the same files on nu-scptheme.github.io, L8–16) over the `[[iftags +theme]]` gate (L1). The candidate's head (L1–12) is the JP frame: the `:scp-jp:theme:black-highlighter-theme` include first (L1), a module CSS importing the candidate's own /1 from the draft host (L3–5), one `:scp-jp:` interwiki-style include at priority=3 naming the same /1 (L7–10), and the localized gate `[[iftags +テーマ]]` (L12). Blocks B1–B4 carry the whole rework. Provenance route: derived from the original at reference revision 11 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P1/P2/P4/P6 rework exactly this frame for the JP environment, and each piece of it is accounted for in sections 1–3.
- **Verify:** Read original L1–16 against candidate L1–12; blocks B1–B4 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module rate]]` inside a right-aligned div (orig L18–20); it has no credit block, no info module and no license box. The candidate deletes the bare Rate (inside B5, orig L18–20 → cand L14–23) and installs the preview credit block (cand L14–23): `:scp-jp:credit:start-preview` / `end-preview` carrying all eight ruling-3 fields (title Bedbugsテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Bedbugs Theme; 著作権者 [[*user winkwonkboi]]; 作成年 2024; 初訳時参照リビジョン 11; the source link to the EN page). The holder matches the original's own attribution (its prose names winkwonkboi as creator, orig L24); nobody the original names is dropped. A license box is added at the tail (cand L334–348, block B56): `:scp-jp:component:license-box-backend` (author=winkwonkboi) with entries for the theme's two images (entlogo.png, Site-95.png), each stating that the original records no license and that the author must be asked before posting — the honest form for unlicensed assets, not an invented license. No T7 credit-module CSS was added (no T7-CREDIT-CSS label fired; `grep -c 'creditRate' candidate.txt` = 0): the credit module's styling comes from the base.
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form, so a separate bare Rate beside it would duplicate the rating widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields and credits campaign translations to AI. T4: a license box is a supplement where the original had none, and KB-60's form judgment accepts the author-confirmation wording where the original is silent.
- **Verify:** Read candidate L14–23 against the eight-field list; `grep -n 'module rate' candidate.txt` (absent, case-insensitive) against original L19; read candidate L334–348.
- **Disposition:** Standing (the port's credit form). The localize check verified the eight fields present (LOCALIZE-ROWS row 60 charges no pattern-3 item for this theme); the ledger closes the credit fields FIXED (register (c3)).

### 2. Includes and components

- **What:** The candidate's complete include list (grep): the JP BHL theme page (L1, live), the interwiki-style frame (L7–10), the credit pair (L14/L23), the escaped usage pair inside the code-styled div (L30–31), `component:image-block` in same-site form (L38), and the license-box pair (L334/L347). Changes against the original: (a) the base include is new in form — the original loads BHL by URL, never by page include; the candidate includes the JP BHL page itself (B3's INCLUDE-REPOINT span covers the head zone); (b) the usage exhibit's two escaped includes are repointed `:scp-wiki:` → `:scp-jp:` (B8, orig L27–28 → cand L30–31) — the self-reference at cand L31 was completed to the `-jp` posting name by the sweep (b5cb724), closing the flag in the Per-theme record; (c) the image-block include keeps its component name in bare same-site form and its file argument is repointed to the candidate's own draft-host file (cand L38; section 4). No `:scp-wiki:` include remains (grep: none). No component swap (T8) was needed; ruling 4 does not engage.
- **Why:** P1: foreign-site includes are repointed to the JP site, and a same-site include takes the bare fullname form (the include forms by context, AGENTS.md §5). The BHL page include is the JP environment's delivery form for the base (T9).
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; the cand L31 self-reference flag is closed by the sweep repair (b5cb724; Per-theme record, item 1).

### 3. Delivery and code loading

- **What:** Three delivery layers. (1) The base: the original loads BHL's two stylesheets from two hosts (cdn.scpwiki.com in the module, nu-scptheme.github.io in the interwiki includes). The candidate loads the base once by page include (cand L1); inside its own code exhibit, the same two stylesheets are @imported from the JP BHL distribution, scp-jp.github.io (cand L209–210, inside B53). (2) The theme's own layer: the code exhibit (orig L194–305 → cand L200–329) is the page's local--code /1 on both sides; the candidate loads it by module-CSS @import (cand L4) and by the interwiki-style include at priority=3 (cand L7–10), both naming the draft host sigma10-jp-test.wdfiles.com (labels DELIVERY-HOST + DRAFT-HOST + SELF-DELIVERY on B2/B3). (3) The frame defect and its fix: as created, the candidate's own include also sat at priority=1, duplicating the base layer's priority and drawing a console error on every combination — the render row's port defect. FIX4-IWB (commit 5559209) changed exactly one line in this file, priority=1 → priority=3 (cand L8), completing the BHL split form (base 1/2, own 3). The original's tail module (orig L312–314, a second @import of the EN /1) has no counterpart: its load is the head module's (B57, orig L311–314 → cand L350 boundary).
- **Why:** P4/T9: deliveries are served from JP hosts in this environment; a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. KB-07 (patterns 9c5e907): duplicate interwiki-style priorities are a frame defect because the layering order becomes undefined; the split form (1 normalize / 2 base / 3 own) is the registered shape the localize #6 charge measures against.
- **Verify:** Read orig L3–16 against cand L1–10 and cand L209–210; `git show 5559209 -- pages/theme:bedbugs-theme-jp.txt` (one line).
- **Disposition:** The duplicate priority is FIXED (GOSIGN2-LEDGER (c2), FIX4-IWB). The draft-host URLs (cand L4, L9) are class (iii) draft form, recorded in section 11. The #6 registration-form item is DISPOSITIONED as a staff-confirmation form item (ledger group entry for bedbugs/black-market/black-serpent): the display-relevant part of #6 was the duplicate priority, and it is fixed.

### 4. Fonts and assets

- **What:** Fonts, all inside the code exhibit (B53, orig L195–200 → cand L200–224). The original imports five Latin faces from fonts.bunny.net (Teko, Rokkitt, Noto Sans Buginese, Sometype Mono, Dosis; orig L196–200). The candidate imports the same five from fonts.googleapis.com (cand L212–216), adds three JP faces from Google Fonts (Noto Sans JP, Noto Serif JP, M PLUS 1 Code; cand L222–224) under an explanatory CSS comment (cand L218–221), and appends a JP fallback to every one of the five font stacks (B54, orig L221–226 → cand L245–250: --header-font gains "Noto Sans JP", --title-font "Noto Serif JP", --body-font "Noto Sans JP", --mono-font "M PLUS 1 Code", --UI-font "Noto Sans JP"). B54's classifier label is CSS-BODY; its content is exactly the P7 stack rewrite, and it is narrated here, not in section 8. Every named face is loaded: the five Latin faces by cand L212–216, the JP faces by cand L222–224 (no KB-16 gap). Assets: the two theme images are repointed to the candidate's own draft-host files — the image-block's Site-95.png (orig L35 → cand L38) and the --logo-image entlogo.png (orig L229 → cand L253, inside B55) — class (ii) own-attachment form; neither image is re-uploaded by this campaign (owner order), and their licenses are unrecorded in the original (section 1's license box).
- **Why:** P7/T5: none of the five Latin faces has Japanese glyphs, so without a JP face in each stack, Japanese text falls back to an OS-dependent generic (the failure pattern 7 exists to prevent; the candidate's body 訳注 at cand L191 states the same ground for readers). KB-17 (patterns 9c5e907): fonts.bunny.net is outside the hotlink allowlist (SCP-JP storage, Google Fonts, BootstrapCDN, cdnjs), so the imports went to the canonical host. P5: own attachments ride the draft host at draft stage and are re-hosted at posting (class (ii)).
- **Verify:** `grep -n 'fonts.bunny.net\|fonts.googleapis.com' candidate.txt` (bunny absent; eight googleapis imports); read cand L245–250 against orig L221–226; `grep -n 'local--files' candidate.txt` (L38 and L253, both own draft-host paths).
- **Disposition:** Fonts FIXED as part of the port (the localize row charges no pattern-7 item for this theme; the supplement is the port's own). Assets DISPOSITIONED (ledger (c3): asset hosts = class (ii); the LOCALIZE-ROWS row 60 note carries the posting-time re-host and license-confirmation items).

### 5. Header, sidebar, site furniture

- **What:** The skeleton prints "none" for this section, but HEADERVAR fired inside B55 (orig L228–229 → cand L252–253): the --logo-image line, repointed in section 4. The theme's other header variables are carried verbatim: --header-title "Department of Entomology" and --header-subtitle "Odd Is To Be Expected" (orig L230–231 = cand L254–255, unchanged context). The LOCALIZE-ROWS row 60 charges exactly those two strings as its one display-affecting finding (#9, header untranslated). No sidebar or topbar rule was adapted (P8 does not engage: the furniture is BHL's, inherited with the base).
- **Why:** P9/T6 variables are overridden where the JP environment requires it; ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57, patterns 9c5e907), and the two strings are the work's own department name and motto.
- **Verify:** `grep -n 'header-title\|header-subtitle\|logo-image' candidate.txt` (L253–255); read orig L228–231 against cand L252–255.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER (c3): header language = ruling 2; ledger group entry, §(c3) tail: "Their #9 header items fall under ruling 2").

### 6. Text translation

- **What:** The candidate's prose is the original's sample body translated in place, entire: the intro and usage zone (B6–B10), the collapsible and tabview samples (B14–B49), the font specimen lines (B49–B52), and the source-code section furniture. 22 blocks are anchor-paired translations (TRANSLATION-ANCHORED); the 27 TRANS-UNANCHORED blocks are the same work without line anchors — the tabview's repeated sample sentence (orig "This tab has the same line in succession." ×11 → cand 「このタブは同じ行が続きます。」 ×11, B20–B30), one-line specimens (B18, B40–B48), and the heading B11 (+ Examples → + 見本， cand L40). Each was read against its original line; all are translations, none is a deletion or a restructuring. Two link-bearing translations sit in section 7. In-CSS text (R1): the CSS comments stay in English verbatim (porter-visible only), and the string variables --theme-base "black-highlighter" / --theme-id "bedbugs-theme" / --theme-name "Bedbugs Theme" (cand L228–230) are carried unchanged — they are BHL registration values, not reader text. The translator's note at cand L191–192 (B50) is the P10 訳注 form and is listed again in section 10.
- **Why:** P10: body, usage and sample text are translated; the 訳注 footnote form is P10's sanctioned shape for port-side explanation. KB-18 covers reader-visible strings; CSS comments and registration variables are not reader-visible, so their retention is recorded, not charged.
- **Verify:** Read orig L22–190 against cand L25–195; `grep -c 'このタブは同じ行が続きます' candidate.txt` = 11, matching the original's 11 identical sample lines.
- **Disposition:** Standing (the port itself). The localize T5 pass recorded no mistranslation finding for this theme; its one display-affecting item is the #9 header pair (section 5).

### 7. Links

- **What:** Two LINK-REPOINT blocks. B7 (orig L24 → cand L27): the intro's hub link — the original links the Department of Entomology hub on scp-wiki; the candidate keeps the EN target and labels it 昆虫学部（英語版） (the JP hub page does not exist; the link is a full-URL link to the original, marked as such). B13 (orig L41–42 → cand L44–45): the link specimens — the visited-link sample is repointed from `theme:bedbugs-theme` to `theme:bedbugs-theme-jp` (the candidate itself, in JP form), and the unvisited sample's label is translated. The credit block's source link (cand L22) names the recorded host scp-wiki.wikidot.com, matching sources.tsv; no probe was needed and no link defect arises there.
- **Why:** P11 repoints links to JP counterparts where they exist; where the counterpart does not exist, the EN target is kept and marked （英語版） rather than pointed at a nonexistent JP page (the dead-target failure P11 exists to prevent).
- **Verify:** Read cand L27 and L44–45 against orig L24 and L41–42.
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** The localize.md closing rule is honored: the stylesheet's rules, variables and order are preserved (the code exhibit's body from the :root block to .blueblock is unchanged context between B54/B55 and the tail), and the JP corrections sit at the frame, the exhibit head (imports) and the exhibit's variable block, not interleaved. The sample body's structure is likewise preserved entire (section 6). The three EXHIBIT-RESTRUCTURE labels adjudicate as follows: B3 and B4 (orig L8–16 → cand L7–12) are the head delivery zone — the two EN interwiki includes and the gate line — not exhibits; their content is decided in section 3. B10 (orig L35 → cand L38) is the image-block include line inside the sample body: the exhibit survives with its include repointed (the classifier's label fires on the repoint shape inside an exhibit region; the exhibit census — image-block, collapsible, tabview, font specimens — is identical on both sides). Nothing was dropped: no exhibit, section or rule present in the original is absent from the candidate.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the ground for each labeled block is stated; here the census decides — exhibit count and content match, so no R3 deletion occurred.
- **Verify:** `grep -n 'tabview\|collapsible\|image-block' original.txt candidate.txt` and compare the exhibit lists; blocks B3/B4/B10 in classification.json.
- **Disposition:** Standing (no structural deletion; the delivery restructure is section 3's subject).

### 9. Formatting only

- **What:** none — WS-ONLY blocks: 0; re-indentation pairs: 0 (the classifier's section 9 counts). The candidate's code was space-indented from creation; the EN4 tab-normalization commit (ab523f4) did not touch this file (its git log confirms).
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; here the ground for "none" is the classifier's count plus the file's history.
- **Verify:** classification.json (0 WS-ONLY blocks); `git log --oneline -- pages/theme:bedbugs-theme-jp.txt`.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The skeleton prints "none" (no signature fired), but three porter additions ride inside other blocks, found by direct inspection: (a) the body translator's note `//訳注: …//` at cand L191–192 (inside B50), explaining the JP font fallbacks to readers — the P10 footnote form; (b) the editor line inside the CSS comment header, "Ported for SCP-JP (theme:bedbugs-theme rev 11)" (cand L206, inside B53), added to the original's own comment header (which is otherwise carried verbatim); (c) the JP-font CSS comment block (cand L218–221, inside B53) explaining the supplement in English and Japanese. No `[!-- ... --]` notes exist (`grep -c '\[!--' candidate.txt` = 0).
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation.
- **Verify:** Read cand L191–192, L201–207 and L218–221.
- **Disposition:** None required; all three are recorded here and in sections 4 and 6.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The three draft-host URLs (cand L4, L9, L38): T1 pseudo-ref×3 — DISPOSITIONED, class (ii)/(iii) (posting rewrites the own-code host to scp-jp.wdfiles.com; own attachments are re-hosted at posting; GOSIGN2-LEDGER (c1) pseudo-ref entry). (2) The BHL min-width overflow 337–419px@≤375 on the sample: DISPOSITIONED as the cross-cutting page-overflow families (static credit replica fixed width KB-33 / preview chrome KB-34; GOSIGN2-LEDGER (c2)). The verdict stamp's T2/T3 line merges this with the priority defect; the register's own adjudication splits them — FIXED for the priority, DISPOSITIONED for the overflow — and this package follows the register. (3) Header language kept in English: DISPOSITIONED under ruling 2 (section 5). (4) The #6 interwiki registration form: DISPOSITIONED as a staff-confirmation form item (ledger group entry); its display-relevant half (the duplicate priority) is FIXED. (5) The two images' re-hosting and license confirmation: posting-time items recorded in LOCALIZE-ROWS row 60; the license box states the confirmation need in the candidate itself (cand L339, L344). (6) FLAGGED by this package and since repaired: the usage exhibit's plain-slug self-reference (cand L31) — see the Per-theme record; the sweep (b5cb724) completed the `-jp` posting name. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–5); item 6 was flagged with evidence and has since been repaired by the sweep (b5cb724), closing the flag; the frozen ledger verdict stands and the stamp reads STALE against it by design.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 3 errors / 2 warns / 0 infos; the errors are pseudo-ref×3 (the section 11 draft-host lines); the two warn codes are not itemized in the extracted row (T1-ROWS row 65; the stamp's citation). Register (c1) dispositions the pseudo-ref class as (ii). (b) T2/T3 render: FINDINGS — the duplicate-priority port defect, FIXED by FIX4-IWB after the render pass, and the sample overflow, dispositioned in (c2); the row records no credit-modal error for this theme, and engine coverage is the lane's full matrix as run (RENDER-ROWS-1). (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting item (#9, ruling 2); the follow-up currency check is the K5a-i artifact `diff-bedbugs-theme-from11.txt`, which records the upstream delta after revision 11 — the port is judged at its reference revision, so the delta is campaign record, not a charge against the candidate. (d) T5: judged jointly with T4 by the source lane; no mistranslation finding stands. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (57 change blocks) and the generator's (diff.md: +188/−154 in 6 hunks); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:bedbugs-theme-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 60).

## Per-theme record

### Item 1 — the usage exhibit names a page that will not exist (repaired)

As built, the usage exhibit's second line read `@@[[include :scp-jp:theme:bedbugs-theme]]@@` (cand L31). The original's line names `:scp-wiki:theme:bedbugs-theme` (orig L28) — correct on its own wiki. The port repointed the site prefix to `:scp-jp:` but kept the plain slug; the candidate posts as theme:bedbugs-theme-jp, so the exhibit instructed readers to include a page that will not exist under that name on scp-jp. The same file got it right elsewhere: the visited-link specimen at cand L44 was repointed to `theme:bedbugs-theme-jp`; the first exhibit line (cand L30, `:scp-jp:theme:black-highlighter-theme`) is not an instance (the JP BHL page's actual name). No register charged the line. The usage-example population sweep completed the reference to `@@[[include :scp-jp:theme:bedbugs-theme-jp]]@@` on the same line (sweep report SWEEP-USAGE.md in R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates, and U-3's batch report (BATCH-U3.md, flag F1) independently recorded the same line. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design. The U-3 repair landing (FIX-U3.md, canonical commit 49cfb90) touched only bloodraven and black-serpent — this theme's U-3 involvement was the sweep line, not that landing.

### Item 2 — wave attribution, checked against the bytes

The ledger's (c3) line closes this theme's row charges with "credit fields FIXED by the credit waves". The file's history is narrower: the credit block was present from creation (commit 053fd41), and the only credit-wave commit that touched the file, FIX-CREDIT-D (1869877), changed exactly one line — the translator field, `SCP-JP` → `AI`. The outcome the register claims (the eight fields present and in ruling-3 form) is true of the current bytes; only the granularity of the attribution differs, and this package follows the git record. The same discipline applies to the (c2) FIXED line: FIX4-IWB's diff for this file is the single priority line (section 3), so the FIXED verdict covers the priority defect and nothing else; the overflow named in the same render row is dispositioned, not fixed (section 11, item 2).

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-bedbugs-theme-jp.txt` — the render sample page the T2/T3 checks rendered (an include of the candidate plus the shared `theme-decoration-sample`). (2) `pages/theme:bedbugs-theme.txt` — the repo's EN-side copy of the original page, the EN sample's base. (3) The delivery itself: the candidate's own local--code /1 on the draft host, named by the frame (cand L4, L9), which is the runtime form of the code exhibit in this package.

## Multi-wave provenance

The candidate's current state is the product of three commits and three check waves, not a single porting pass: Stage 2 EN4 created it (commit 053fd41: translation, credit block, license box, font supplement, BHL delivery restructure, own-layer frame at priority=1); LOCALIZE-S2-A then examined that state and charged #6 (interwiki form) and #9 (header language) plus the posting-time items (LOCALIZE-ROWS row 60); the render lane (RENDER-S2-A, EN4) found the duplicate-priority defect and the sample overflow; FIX-CREDIT-D (commit 1869877) normalized the translator field; FIX4-IWB (commit 5559209, the file's last content change and this package's computed-against commit) repaired the priority; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 60, (c1) pseudo-ref entry, (c2) bedbugs entry, (c3) bedbugs entry and the §(c3) group entry on #6/#9; GOSIGN2-LEDGER-SUPPLEMENT.md (no bedbugs entries); T1-ROWS row 65; LOCALIZE-ROWS row 60; RENDER-ROWS-1 (RENDER-S2-A) bedbugs row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted 25 open blocks (1 residue, 24 heuristic). All are resolved; none required a new signature. The heuristic mass is one shape — prose translation whose script delta defeats the anchor majority — plus three special cases noted individually.

- **R1 — B11 (residue; orig L37 → cand L40).** The "+ Examples" heading → 「+ 見本」. Resolved in section 6 as P10 heading translation.
- **R2 — B7 (heuristic; orig L24 → cand L27).** The intro sentence; also carries the LINK-REPOINT of section 7 (the hub link kept EN with the （英語版） label). Resolved in sections 6–7.
- **R3 — B9 (heuristic; orig L31 → cand L34).** The BHL note under the usage exhibit, translated (its link label こちら included). Resolved in section 6.
- **R4 — B12, B18, B40–B48 (heuristic; orig L39–169 → cand L42–172).** One-line sample and specimen translations (horizontal-rule prose, blockquote specimens, code-block captions). Resolved in section 6 by shape; each was read against its original line.
- **R5 — B13 (heuristic; orig L41–42 → cand L44–45).** The link specimens; carries the LINK-REPOINT of section 7. Resolved there.
- **R6 — B20–B30 (heuristic; orig L71–91 → cand L74–94).** The tabview's eleven identical sample lines, translated identically eleven times. Resolved in section 6 (the count check is stated there).
- **R7 — B41 (heuristic; orig L127–129 → cand L130–132).** The div-blockquote instruction, translated over three lines. Resolved in section 6.
- **R8 — B50 (heuristic; orig at L188 → cand L191–192).** Pure addition with no original counterpart: the body 訳注 on JP font fallbacks. Resolved in sections 6 and 10 (porter annotation, P10 form).
- **R9 — B54 (heuristic-tier CSS-BODY; orig L222–226 → cand L246–250).** The five font-stack lines gaining JP fallbacks. The classifier's CSS-BODY label stands as its mechanical reading; the mechanism is the P7 stack rewrite, resolved in section 4.

## License and attribution

- **Title:** Bedbugs Theme
- **Author:** winkwonkboi
- **Source:** https://scp-wiki.wikidot.com/theme:bedbugs-theme — revision 11
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
