# Review package — theme:black-serpent-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:black-serpent-jp — origin EN, population #63 [GOSIGN2-LEDGER (b) row 63]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 5fc54837aabb89ac64d805ea01e01692070b39bdefe82945f2c9dab72dfee7a1); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 0 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 68; GOSIGN2-LEDGER (b) row 63]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — port defect: duplicate `interwiki-style` priority=1 + BHL min-width overflow 337–419px@≤375 on sample; webkit-375 hidden-*/http.cat cluster = transient 503 capture, not a defect. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 63, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 63]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 63]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:black-serpent-jp.txt sha256:5fc54837aabb89ac64d805ea01e01692070b39bdefe82945f2c9dab72dfee7a1; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/black-serpent-jp/candidate.txt (sha256 e85177d29f64ff90226b9728ddefb823e646765de2bb5f93cb14bdc8faebec41)
Original: theme:black-serpent — scp-wiki, revision 12 (sha256 525f5d1ee046f08a5dde2ae5822f7213f7a2af375a57e1de3372ba605d981258)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 63); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no black-serpent entries |
| Fixed after the localize check | The duplicate `interwiki-style` priority (FIX4-IWB, commit 5559209: priority=1 → 3, one line) and the translator-attribution normalization (FIX-CREDIT-D, commit 1869877) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref×3 (draft-host lines, classes (ii)/(iii)); header language under ruling 2 (the #9 charge); the #6 interwiki registration form as a staff-confirmation item; the webkit-375 503 capture (KB-44) |
| Flagged by this package | The usage exhibit's self-reference names the plain slug (candidate L34); the intro's BHL logo image exhibit was dropped without a register charge — see the Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:black-serpent | theme:black-serpent-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 12, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 12 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-black-serpent.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:black-serpent-jp.txt`, created in commit 053fd41 (Stage 2 EN4); later content changes in ab523f4, 1869877 and 5559209 |
| Lines / bytes | 285 lines / 8,113 bytes | 302 lines / 10,570 bytes |
| SHA-256 | 525f5d1ee046f08a5dde2ae5822f7213f7a2af375a57e1de3372ba605d981258 | e85177d29f64ff90226b9728ddefb823e646765de2bb5f93cb14bdc8faebec41 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted (no R4): the candidate's stylesheet is the original's own code exhibit carried in place, and its body is the original's, translated. Reference-revision currency: the upstream original has moved past revision 12 since the port; the follow-up artifact `diff-black-serpent-from12.txt` in the campaign record carries that later delta (sources.tsv kind K5a-i). This package judges the port against the revision it was made from.

## Summary

Black Serpent is a Serpent's Hand theme on a Black Highlighter base. The original carries the full EN furniture set: a head module importing the BHL stylesheets, a rating pair ("**Rating:**" with a bare Rate module, "**Rating w/ Credit Module:**"), a placeholder info module, an intro with the BHL logo image, usage and palette exhibits, a code exhibit importing its two display faces from a coollabs font host, an EN license box for the Serpent's Hand logo, and a tail module loading its own /1 from the EN wiki. The candidate replaces the furniture with the JP forms (preview credit block, JP license-box pair), loads the base through the JP BHL page include and its own layer at priority 3 on the draft host, repoints the font imports to Google Fonts with a Noto Sans JP supplement, and translates the body entire — minus one exhibit: the intro's BHL logo image has no counterpart (Per-theme record, item 2). Measured churn (diff.md, the generator's count: +166/−155 in 4 hunks; the classifier counts 72 change blocks) is mostly that translation. Two later waves touched the file: FIX-CREDIT-D's translator line and FIX4-IWB's priority repair; the usage exhibit's plain-slug self-reference escaped both (Per-theme record, item 1).

## Classification

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 47 |
| TRANSLATION-ANCHORED | 16 |
| DRAFT-HOST | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| LICENSE-BOX | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Counts: 72 blocks — 27 specific (37.5%), 44 heuristic (61.1%), 1 residue (1.4%), 0 skipped. Topology: no relocation; the original's code-css exhibit (orig L224–268) is the candidate's (cand L231–287), the /1 source on both sides. Labels are sets per block; the skeleton lists each block once under its primary label, so these sections were written from classification.json's label spans: the skeleton's section 5 prints "none" although HEADERVAR fired inside B67, and the font-stack rewrites sit inside B68 (labeled CSS-BODY), not under any font label.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–5) is a module CSS @importing the two BHL stylesheets from nu-scptheme.github.io, over the `[[iftags +theme]]` gate (L1); its own-layer loads sit at the tail (orig L282–285, a module @importing the page's EN /1). The candidate's head (L1–12) is the JP frame: the `:scp-jp:theme:black-highlighter-theme` include (L1), a module CSS @importing the candidate's own /1 from the draft host (L3–5), one `:scp-jp:` interwiki-style include at priority=3 naming the same /1 (L7–10), and the localized gate (L12). Blocks B1–B3 carry the rework; the tail module's disappearance is B72. Provenance route: derived from the original at reference revision 12 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P1/P2/P4/P6 rework exactly this frame, and each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–5 and L282–285 against candidate L1–12; blocks B1–B3 and B72 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original's credit furniture is threefold: the rating pair inside a right-aligned div (orig L9–13: "**Rating:**", a bare `[[module Rate]]`, "**Rating w/ Credit Module:**" — one module under the first label, the second label bare), the placeholder info module (orig L14–18: `:scp-wiki:info:start`/`more`/`end` around template text, "Info about your page."), and a real license box at the tail (orig L271–280: `:scp-wiki:component:license-box-theme`, author=Jerden, one entry — Serpents-Hand.svg, author [[*user Zyn]] modified by [[*user Jerden]], CC BY-SA 3.0, source the Serpent's Hand hub). The candidate deletes the rating pair and the info module (B4: BARE-RATE-DEL + INFO-DEL, orig L9–18 → cand L12) and installs the preview credit block (cand L14–23): all eight ruling-3 fields, 著作権者 [[*user Jerden]] — the theme's author, matching the original's prose (orig L20) and its license box; the header image's author Zyn is credited in the translated prose (cand L25) and in the license entry, as in the original, so nobody the original names is dropped from the record. The license box is converted, not dropped (B70–B71): `:scp-jp:component:license-box-backend` (author=Jerden, cand L291) with the entry translated （ファイル名/名称/作者/ライセンス/出典； the license rendered as a CC BY-SA 3.0 deed.ja link; the source link localized to 蛇の手ハブ） and `:scp-jp:component:license-box-end` (cand L301). No T7 credit-module CSS was added (no T7-CREDIT-CSS label fired; `grep -c 'creditRate' candidate.txt` = 0).
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form; the original's pair-and-placeholder furniture is the EN form it replaces, and the placeholder info body carried no content to preserve (its text is the module's template sample). T4: an original license box is converted to the JP backend/end form, never dropped (KB-63 is the dropped set; this theme is not in it).
- **Verify:** Read candidate L14–23 against the eight-field list; `grep -n 'module Rate\|info:start' candidate.txt` (absent) against original L11 and L14; read candidate L291–301 against original L271–280.
- **Disposition:** Standing (the port's credit form); the ledger closes the credit fields FIXED (register (c3)).

### 2. Includes and components

- **What:** The candidate's include list (grep): the JP BHL theme page (L1), the interwiki-style frame (L7–10), the credit pair (L14/L23), the escaped usage pair (L33–34), the theme-squares component repointed to `:scp-jp:` (cand L38), and the license-box pair (L291/L301). Changes: (a) theme-squares repointed with its parameters carried and its color names translated (テーマカラー, ダークアクセント, ブライトアクセント …); (b) the usage exhibit's escaped includes repointed `:scp-wiki:` → `:scp-jp:` (B9, orig L30–31 → cand L33–34) — with one survivor defect, the self-reference at cand L34, flagged in the Per-theme record; (c) the info module's three includes deleted with the module (section 1). No `:scp-wiki:` include remains (grep: none). No T8 swap was needed; ruling 4 does not engage.
- **Why:** P1: foreign-site includes are repointed to the JP counterpart that actually exists on scp-jp (KB-15); theme-squares has a JP port.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the lists.
- **Disposition:** Standing, with the cand L34 self-reference flagged (Per-theme record, item 1).

### 3. Delivery and code loading

- **What:** Three delivery layers. (1) The base: the original @imports BHL's two stylesheets from nu-scptheme.github.io (head module). The candidate loads the base by page include (cand L1); inside its code exhibit, the same two stylesheets are @imported from the JP BHL distribution, scp-jp.github.io (cand L241–242, inside B66). (2) The theme's own layer: the code exhibit (orig L224–268 → cand L231–287) is the page's local--code /1 on both sides; the original loads it at the tail by module @import from scp-wiki.wikidot.com (orig L283, its URL carrying a doubled slash), the candidate at the head by module @import (cand L4) and by the interwiki-style include at priority=3 (cand L7–10), both naming the draft host (labels DELIVERY-HOST + DRAFT-HOST + SELF-DELIVERY on B2/B3). (3) The frame defect and its fix: as created, the candidate's own include sat at priority=1, duplicating the base layer's registration — the render row's port defect. FIX4-IWB (commit 5559209) changed exactly one line, priority=1 → priority=3 (cand L8), completing the BHL split form (base 1/2, own 3). The LOCALIZE-ROWS row 63 #6 charge adds that this theme's registration form differed from the prescribed (1 normalize / 2 BHL / 3 theme) shape; the ledger group entry dispositions the #6 items as staff-confirmation form items, with the display-relevant duplicate priority fixed.
- **Why:** P4/T9: deliveries are served from JP hosts in this environment; a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. KB-07 (patterns 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): duplicate interwiki-style priorities leave the layering order undefined.
- **Verify:** Read orig L2–5 and L282–285 against cand L1–10 and cand L241–242; `git show 5559209 -- pages/theme:black-serpent-jp.txt` (one line).
- **Disposition:** The duplicate priority is FIXED (GOSIGN2-LEDGER (c2), FIX4-IWB). The draft-host URLs (cand L4, L9) are class (iii) draft form, recorded in section 11. The #6 form item is DISPOSITIONED (ledger group entry).

### 4. Fonts and assets

- **What:** Fonts, all inside the code exhibit (B66, orig L225–227 → cand L232–248). The original imports its two display faces from api.fonts.coollabs.io (Londrina Outline; Farro). The candidate imports both from fonts.googleapis.com (cand L244–245; Farro with its weight axis spelled out), adds Noto Sans JP from Google Fonts (cand L248) under a JP comment, and appends "Noto Sans JP" to the two stacks that consume the faces (B68, orig L253–254 → cand L273–274: --header-font 'Londrina Outline', "Noto Sans JP", sans-serif; --title-font 'Farro', "Noto Sans JP", sans-serif). B68's classifier label is CSS-BODY; its content is exactly the P7 stack rewrite, narrated here. Every named face is loaded (no KB-16 gap). Assets: the theme's one image, Serpents-Hand.svg, is repointed in --logo-image from the original's EN file path to the candidate's own draft-host file (B67, orig L248 → cand L268) — class (ii) own-attachment form; its license entry rides in the converted license box (section 1). The intro's BHL logo image (orig L22) was dropped, not repointed — Per-theme record, item 2.
- **Why:** P7/T5: neither display face has Japanese glyphs, so without a JP face in the stack, Japanese header text falls back to an OS-dependent generic. KB-17 (patterns 9c5e907): api.fonts.coollabs.io is outside the hotlink allowlist (SCP-JP storage, Google Fonts, BootstrapCDN, cdnjs), so the imports went to the canonical host, which serves both families. P5: own attachments ride the draft host at draft stage (class (ii)).
- **Verify:** `grep -n 'coollabs\|fonts.googleapis.com' candidate.txt` (coollabs absent; three googleapis imports in the exhibit); read cand L273–274 against orig L253–254; `grep -n 'logo-image' candidate.txt` (L268).
- **Disposition:** Fonts FIXED as part of the port (the localize row's font-host note is answered by the repoint; the row charges no pattern-7 stack item for this theme). The asset is DISPOSITIONED (ledger (c3): asset hosts = class (ii)).

### 5. Header, sidebar, site furniture

- **What:** The skeleton prints "none" for this section, but HEADERVAR fired inside B67 (orig L247–248 → cand L267–268): the --logo-image line, repointed in section 4. The theme's other header variables are carried verbatim: --header-title "SERPENT'S HAND" and --header-subtitle "The Anomalous is on the Rise" (orig L249–251 zone = cand L269–271 zone, unchanged context). The LOCALIZE-ROWS row 63 charges those two strings as its one display-affecting finding (#9, header in English). No sidebar or topbar rule was adapted (P8 does not engage: the furniture is BHL's, inherited with the base).
- **Why:** P9/T6 variables are overridden where the JP environment requires it; ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57, patterns 9c5e907), and the two strings are the work's own group name and slogan.
- **Verify:** `grep -n 'header-title\|header-subtitle\|logo-image' candidate.txt` (L268–271); read orig L247–254 against cand L267–274.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER (c3): header language = ruling 2; ledger group entry: "Their #9 header items fall under ruling 2").

### 6. Text translation

- **What:** The candidate's prose is the original's body translated in place: the intro (B6–B8, with its hub links — section 7), the usage instruction (B8–B9 zone), the theme-squares palette names, the sample body (B11–B64: specimens, collapsibles, tabview samples), and the source-code section furniture. 16 blocks are anchor-paired; the 44 TRANS-UNANCHORED blocks and the heuristic mass are the same work without line anchors (one-line specimens and repeated sample lines), each read against its original line — all are translations, with two exceptions that are not translation blocks at all: B6 also carries the dropped intro image (Per-theme record, item 2), and B50-zone additions in sibling themes do not occur here (this candidate has no body 訳注). In-CSS text (R1): the CSS comments stay in English verbatim (porter-visible only), including the section banners (===THEME COLORS=== / ===THEME HEADER=== / ===PAGE CONTENT===); the string variables --theme-base "nuscp" / --theme-id "black-serpent" / --theme-name "Black Serpent Theme" (cand L251–253) are carried unchanged — BHL registration values, not reader text.
- **Why:** P10: body, usage and sample text are translated. KB-18 covers reader-visible strings; comments and registration variables are not reader-visible, so their retention is recorded, not charged.
- **Verify:** Read orig L20–220 against cand L25–230; `grep -n 'theme-name' candidate.txt`.
- **Disposition:** Standing (the port itself). The localize T5 pass recorded no mistranslation finding for this theme; its one display-affecting item is the #9 header pair (section 5).

### 7. Links

- **What:** One LINK-REPOINT block (inside B6/B7's zone) plus the intro's link set, read directly. The original's intro links the Wanderer's Library theme and the Serpent's Hand hub as same-site links and the "Now, the Serpent" series by full EN URL. The candidate localizes the two hub/theme links to their JP same-site forms (`[[[theme:wanderers|放浪者の図書館テーマ]]]`, `[[[serpent-s-hand-hub|蛇の手]]]`, cand L25 — both name pages that exist on scp-jp), keeps the series link on the EN original by full URL (the series' JP presence is not a page this link can name), and repoints the BHL detail link in the usage prose from the EN page to the JP page (`[https://scp-jp.wikidot.com/theme:black-highlighter-theme こちら]`, cand L29). The license box's source link is localized with its entry (蛇の手ハブ, cand L299). The credit block's source link (cand L22) names the recorded host scp-wiki.wikidot.com, matching sources.tsv; no probe was needed.
- **Why:** P11: links take the JP counterpart where it exists; the dead-target failure P11 exists to prevent does not arise for the kept EN series link, whose target is the original itself.
- **Verify:** Read cand L25 and L29 against orig L20 and L26.
- **Disposition:** Standing; no link item was charged for this theme in any register (the LOCALIZE row's P11-adjacent text does not charge this theme's links).

### 8. Structure

- **What:** The localize.md closing rule is honored for the stylesheet: the code exhibit's rules, variables and order are preserved (the body from the :root block to the blockquote rules is unchanged context between B66/B68 and the tail), and the JP corrections sit at the frame, the exhibit head (imports and comment header) and the exhibit's header-variable block. Two structural acts sit outside the CSS. (a) The furniture swap of section 1 (rating pair + placeholder info module out, preview credit in) — decided there. (b) The intro image drop: the original's `[[image …black-highlighter-logo.svg]]` (orig L22) has no candidate counterpart (B6 pairs the line with the translated intro). The image is the base theme's logo, hosted on the base theme's own EN page; the candidate's intro instead links the JP BHL page in prose (section 7). No register charges the drop, and no CSS for the image survives (it was a body image, not a styled element). It is recorded here and in the Per-theme record so the deletion is visible rather than silent. The three EXHIBIT-RESTRUCTURE labels adjudicate as follows: B10 (orig L35–38 → cand L38–41) is the theme-squares include zone — the exhibit survives, repointed; B70/B71 (orig L271–280 → cand L290–301) are the license box's form conversion, decided in section 1. The remaining exhibit census (usage code div, samples, collapsible code exhibit) is identical on both sides.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the ground for each is stated; here one genuine drop exists (the intro image) and it is named, with its ground, rather than waved through.
- **Verify:** `grep -n 'black-highlighter-logo' original.txt candidate.txt` (original only); `grep -n 'tabview\|collapsible\|theme-squares' original.txt candidate.txt` for the surviving census.
- **Disposition:** Standing (restructuring recorded), with the image drop carried to the Per-theme record.

### 9. Formatting only

- **What:** No WS-ONLY label fired over 72 blocks. One formatting act exists in the file's history: the EN4 tab-normalization commit (ab523f4) changed 4 lines in this file (tabs to spaces in the code exhibit) — below the classifier's block threshold against the current pair, since both sides of this package's diff postdate it in effect (the mirror is the EN original, whose corresponding lines carry spaces already in the fetched copy). The trailing-space line inside the blockquote rule (orig L263 = cand L283, `border: 1px solid …;  `) is carried byte-identical on both sides.
- **Why:** Formatting-only churn is disclosed as its own class; here the ground is the classifier's count plus the file's history.
- **Verify:** classification.json (no WS-ONLY blocks); `git show ab523f4 --stat -- pages/theme:black-serpent-jp.txt` (4 lines).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter addition: the CSS comment header inside the code exhibit (cand L232–238), which the original's exhibit does not have — it names the theme, its year and author, its BHL basis, and the editor line "Ported for SCP-JP (theme:black-serpent rev 12)". It rides inside B66 with the import repoints. A second, smaller one: the JP font comment `/* 日本語フォント (JP localization) */` (cand L247). No `[!-- ... --]` notes and no body 訳注 exist (`grep -c '\[!--' candidate.txt` = 0); no annotation signature fired, and direct inspection finds nothing else.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation.
- **Verify:** Read cand L232–248 against orig L225–227.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The three draft-host URLs (cand L4, L9, L268): T1 pseudo-ref×3 — DISPOSITIONED, classes (ii)/(iii) (posting rewrites the own-code host to scp-jp.wdfiles.com; the own attachment is re-hosted at posting; GOSIGN2-LEDGER (c1) pseudo-ref entry). The two warn codes in the T1 row are not itemized in the extracted row. (2) The BHL min-width overflow 337–419px@≤375 on the sample: the (c2) register brackets it inside this theme's FIXED line together with the priority defect; the fixing commit's diff in this file is the single priority line, and the overflow is the cross-cutting BHL min-width family item the same register dispositions for its sibling themes (KB-33/KB-34 formulas) — this package follows the bytes and records the bracket as covering the priority (Per-theme record, item 3). (3) The webkit-375 hidden-*/http.cat cluster: DISPOSITIONED, a transient Wikidot 503 capture, not a defect (KB-44). (4) Header language kept in English: DISPOSITIONED under ruling 2 (section 5). (5) The #6 interwiki registration form: DISPOSITIONED as a staff-confirmation form item (ledger group entry); its display-relevant half (the duplicate priority) is FIXED. (6) FLAGGED by this package, not dispositioned: the usage exhibit's plain-slug self-reference (cand L34) and the intro image drop (orig L22) — see the Per-theme record. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1, 3, 4, 5); item 2 recorded as bracketed; item 6 flagged for the repair sweep and the record.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 3 errors / 2 warns / 0 infos; the errors are pseudo-ref×3 (section 11, item 1) (T1-ROWS row 68). Register (c1) dispositions the pseudo-ref class as (ii). (b) T2/T3 render: FINDINGS — the duplicate-priority port defect, FIXED by FIX4-IWB after the render pass; the sample overflow and the 503 capture, dispositioned in (c2) (section 11); the row records no credit-modal error for this theme, and engine coverage is the lane's full matrix as run (RENDER-ROWS-1). (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting item (#9, ruling 2); the follow-up currency check is the K5a-i artifact `diff-black-serpent-from12.txt`, recording the upstream delta after revision 12 — the port is judged at its reference revision. (d) T5: judged jointly with T4; no mistranslation finding stands. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (72 change blocks) and the generator's (diff.md: +166/−155 in 4 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:black-serpent-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 63).

## Per-theme record

### Item 1 — the usage exhibit names a page that will not exist (flagged by this package)

The usage exhibit's second line reads `@@[[include :scp-jp:theme:black-serpent]]@@` (cand L34). The original's line names `:scp-wiki:theme:black-serpent` (orig L31) — correct on its own wiki. The port repointed the site prefix to `:scp-jp:` but kept the plain slug; the candidate itself posts as theme:black-serpent-jp, so the exhibit instructs readers to include a page that will not exist under that name on scp-jp. The first exhibit line (cand L33, `:scp-jp:theme:black-highlighter-theme`) is not an instance: that is the JP BHL page's actual name. No register charges the line. This package flags it for the population sweep repairing this family; the candidate is not edited here (review packages never edit candidates).

### Item 2 — the dropped intro image (recorded by this package)

The original's intro carries the BHL logo as a body image (orig L22: `[[image https://scp-wiki.wdfiles.com/local--files/theme%3Ablack-highlighter-theme/black-highlighter-logo.svg]]`). The candidate's intro (cand L25) has no image. The deletion is real and uncharged: no ledger line, localize charge or render finding names it. The mitigating facts are stated in section 8 (the image is the base theme's logo on the base theme's own file space; the candidate links the JP BHL page in the same paragraph's neighborhood), but no register sanctions the drop, so this package records it as an open observation for any future exhibit pass rather than dispositioning it itself.

### Item 3 — wave attribution and the (c2) bracket, checked against the bytes

The ledger's (c3) line closes this theme's row charges with "credit fields FIXED by the credit waves". The file's history: the credit block was present from creation (053fd41), and the only credit-wave commit that touched the file, FIX-CREDIT-D (1869877), changed exactly one line — the translator field, `SCP-JP` → `AI`. The claimed outcome is true of the current bytes; only the attribution granularity differs. Likewise the (c2) FIXED bracket (section 11, item 2): FIX4-IWB's diff in this file is the single priority line, so the FIXED verdict is verified for the priority defect; the overflow named in the same bracket is the cross-cutting family item. This package follows the git record in both places.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-black-serpent-jp.txt` — the render sample page the T2/T3 checks rendered. (2) `pages/theme:black-serpent.txt` — the repo's EN-side copy of the original page, the EN sample's base. (3) The delivery itself: the candidate's own local--code /1 on the draft host, named by the frame (cand L4, L9), which is the runtime form of the code exhibit in this package.

## Multi-wave provenance

The candidate's current state is the product of four commits and three check waves: Stage 2 EN4 created it (commit 053fd41: translation, credit block, license-box conversion, font repoints and supplement, frame at priority=1, the intro image drop) and normalized its code-block tabs in a follow-up commit (ab523f4, 4 lines); LOCALIZE-S2-A then examined that state and charged #9 (header language) and #6 (interwiki form) plus the posting-time host item (LOCALIZE-ROWS row 63); the render lane (RENDER-S2-A, EN4) found the duplicate-priority defect, the sample overflow and the 503 capture; FIX-CREDIT-D (commit 1869877) normalized the translator field; FIX4-IWB (commit 5559209, the file's last content change and this package's computed-against commit) repaired the priority; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 63, (c1) pseudo-ref entry, (c2) black-serpent entry, (c3) black-serpent entry and the §(c3) group entry on #6/#9; GOSIGN2-LEDGER-SUPPLEMENT.md (no black-serpent entries); T1-ROWS row 68; LOCALIZE-ROWS row 63; RENDER-ROWS-1 (RENDER-S2-A) black-serpent row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted 45 open blocks (1 residue, 44 heuristic). All are resolved; none required a new signature. The heuristic mass is one shape — prose translation whose script delta defeats the anchor majority — plus the special cases noted individually.

- **R1 — B69 (residue; orig L267 → cand L287).** The code exhibit's closing `[[/code]]` line, present and identical on both sides; the differ paired it across the channel boundary (code-css → body) and left it unlabeled. Alignment noise at the exhibit boundary; no content. Resolved here.
- **R2 — B6 (heuristic; orig L22 → cand L25).** The translated intro paragraph; also carries the dropped intro image (Per-theme record, item 2) and the LINK-REPOINT of section 7. Resolved in sections 6–8.
- **R3 — B7 (heuristic; orig L26 → cand L29).** The BHL instruction sentence, translated, with its detail link repointed to the JP BHL page. Resolved in sections 6–7.
- **R4 — B11–B64 (heuristic, the remaining mass).** One-line sample, specimen and palette-name translations across the body. Resolved in section 6 by shape; each was read against its original line.
- **R5 — B68 (heuristic-tier CSS-BODY; orig L253–254 → cand L273–274).** The two font-stack lines gaining "Noto Sans JP". The classifier's CSS-BODY label stands as its mechanical reading; the mechanism is the P7 stack rewrite, resolved in section 4.
