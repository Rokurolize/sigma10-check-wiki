# Review package — theme:bloodraven-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:bloodraven-jp — origin EN, population #65 [GOSIGN2-LEDGER (b) row 65]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ef125a4e588854c0f768607156f1e60d699d3175fbfbd13caa3679641e967dd7); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 43 errors / 1 warn / 1 info (hotlink×42, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 70; GOSIGN2-LEDGER (b) row 65]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — port defect: `interwiki-style` rejected (missing `priority` parameter, every combo) + dead `fondo-code.png` asset (404 every combo); webkit-375 503 transient. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 65, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 65]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 65]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:bloodraven-jp.txt sha256:ef125a4e588854c0f768607156f1e60d699d3175fbfbd13caa3679641e967dd7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/bloodraven-jp/candidate.txt (sha256 bcbd7db724ea5f6f2fa7a92d8217ed68c85ddde033e5eeb58d2af4a3b55f6381)
Original: theme:bloodraven — scp-wiki, revision 62 (sha256 dd61ab9d4004613271d36c6a345e3c5bb0cb1342dbb292fb2dd8edbffbbe7250)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 65); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no bloodraven entries |
| Fixed after the localize check | The missing interwiki-style priority (FIX4-IWB, commit 5559209: exactly one added line, `\| priority=1`) and the dead fondo-code.png reference (FIX2-DEADREF, commit b33b69f, which also carried this file's translator normalization — Per-theme record, item 3) |
| Standing items | **DISPOSITIONED** — pattern 5 (all display assets and variant modules hotlink EN/author sites; class (ii), KB-58); pattern 11 (the hub link kept on the EN original; sibling / batch-posting class); the webkit-375 503 capture (KB-44) |
| Flagged by this package | The five usage exhibits name the plain slug (candidate L32, L50, L62, L74, L86); the comic-runes font import was dropped while its font stack survives (candidate L413) — see the Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:bloodraven | theme:bloodraven-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 62, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 62 | — |
| Source of this copy | Campaign mirror store (fetched once by the campaign's localize lane; byte-identical copy, SHA-256 verified against sources.tsv) | Canonical file `pages/theme:bloodraven-jp.txt`, created in commit 7e07438 (Stage 2 EN5); later content changes in b33b69f and 5559209 |
| Lines / bytes | 1,440 lines / 32,782 bytes | 1,442 lines / 34,032 bytes |
| SHA-256 | dd61ab9d4004613271d36c6a345e3c5bb0cb1342dbb292fb2dd8edbffbbe7250 | bcbd7db724ea5f6f2fa7a92d8217ed68c85ddde033e5eeb58d2af4a3b55f6381 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted (no R4): the candidate's stylesheet is the original's own code exhibit carried in place, and its body is the original's, translated. The theme is a standalone design (no base-theme include on either side); its four color variants are parameter-gated module blocks inside the same file on both sides.

## Summary

Blood Raven is a large single-file theme (1,440 lines) for Valravn Corporation articles, with four color variants (Frostblood, Sunblood, Acidblood, Paleblood) selected by include parameters. The original delivers its code by a page-URL self-import (`theme:bloodraven/code/1`), carries an info module whose body duplicates the usage intro, a bare Rate module, five usage exhibits, four screenshot exhibits, a 1,175-line code exhibit importing three display faces from a coollabs host plus a runes stylesheet from a sibling theme's file space, and four parameter-gated variant modules at the tail whose assets live on the author's own wiki. The candidate converts the furniture to the JP forms (preview credit block naming both contributors, info module and bare Rate deleted), repoints the delivery to its own draft-host /1 with the interwiki frame completed by FIX4-IWB, repoints the font imports to Google Fonts with a Noto Sans JP supplement, and translates the body entire. Two content defects survive every wave and are flagged by this package: all five usage exhibits name the plain slug, and the runes stylesheet import was dropped while the CSS rule naming its two faces survives (candidate L413), so the runic text the rule styles has no loaded face. Measured churn (diff.md, the generator's count: +185/−192 in 9 hunks; the classifier counts 87 change blocks) is small against the file's size because the stylesheet body is carried verbatim.

## Classification

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 49 |
| TRANSLATION-ANCHORED | 19 |
| EXHIBIT-RESTRUCTURE | 6 |
| COLON-ENC | 5 |
| DRAFT-HOST | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| TASL-FIELDS | 1 |

Counts: 87 blocks — 31 specific (35.6%), 49 heuristic (56.3%), 7 residue (8.0%), 0 skipped. Topology: no relocation; the original's code exhibit (orig L187–1361) is the candidate's (cand L188–1362), and the four variant modules (orig L1367–1431) are the candidate's (cand L1372–1432). Labels are sets per block; the skeleton lists each block once under its primary label, so these sections were written from classification.json's label spans: the dropped font import sits inside B79 (labeled FONT-IMPORT + JPFONT-LOAD), and the dead-asset repoint is B82 (labeled CSS-BODY).

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–9) is a module CSS @importing the page's own code from a page URL (`https://scp-wiki.wikidot.com/theme:bloodraven/code/1`, L2), the `:scp-wiki:component:toggle-sidebar` include (L5), an empty header div, and the `[[iftags +theme]]` gate (L9). The candidate's head (L1–13) is: a module CSS @importing the candidate's own /1 from the draft host (L2), the `:scp-jp:` interwiki-style include naming the same /1 (L4–7; the `| priority=1` line, L5, was added by FIX4-IWB — section 3), the toggle-sidebar repointed to `:scp-jp:` (L9), the header div, and the localized gate (L13). Blocks B1–B3 carry the rework. Provenance route: derived from the original at reference revision 62 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P1/P2/P4/P6 rework exactly this frame, and each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–9 against candidate L1–13; blocks B1–B3 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original's credit furniture is an info module (orig L11–13: `:scp-wiki:info:start`/`end` around one sentence naming the theme's creator [[*user Dc_Yerko]] "with indications of [[*user Kilerpoyo]]") and a bare `[[module Rate]]` in a right-aligned div (orig L15–17). The candidate deletes both (B5: INFO-DEL + BARE-RATE-DEL inside the credit zone) and installs the preview credit block (cand L15–24): all eight ruling-3 fields, 著作権者 "Dc_Yerko, Kilerpoyo" — both people the original names, the creator and the indications contributor, so nobody is dropped from the record. The deleted info body is not lost content: its sentence is the usage intro, which survives translated at cand L28 (and names both contributors there too, in prose). No license box exists on either side (`grep -c 'license-box'` = 0 in both files), so no T4 conversion arises. No T7 credit-module CSS was added: the candidate's four creditRate/creditButton rule hits are the original's own rules, carried verbatim (grep count 4 in both files).
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form; the original's info-plus-bare-Rate furniture is the EN form it replaces. The two-name author field follows the original's own attribution sentence.
- **Verify:** Read candidate L15–24 against the eight-field list and original L11–17; `grep -c 'creditRate\|creditButton' original.txt candidate.txt` (4 and 4).
- **Disposition:** Standing (the port's credit form); the ledger closes the credit fields FIXED (register (c3)) — with the attribution caveat of Per-theme record, item 3.

### 2. Includes and components

- **What:** The candidate's include list (grep): the interwiki-style frame (L4–7), toggle-sidebar (L9), the credit pair (L15/L24), the five escaped usage exhibits (L32, L50, L62, L74, L86), and the five image-block exhibits (L40, L52, L64, L76, L90). Changes: (a) toggle-sidebar repointed `:scp-wiki:` → `:scp-jp:` (B3, with INCLUDE-REPOINT); (b) the image-block includes repointed from the original's un-namespaced `component:image-block` to `:scp-jp:component:image-block`, their file names colon-encoded (`theme%3Abloodraven`), and their captions translated (フロストブラッド・レイヴン etc.) — the five EXHIBIT-RESTRUCTURE labels on B15, B21, B27, B33 and the logo block are this repoint's false-fire shape: every exhibit survives (section 8's census); (c) the usage exhibits repointed to `:scp-jp:` — with the survivor defect that all five kept the plain slug (Per-theme record, item 1); (d) the info module's two includes deleted with the module (section 1). No `:scp-wiki:` include remains (grep: none). No T8 swap was needed; ruling 4 does not engage.
- **Why:** P1: foreign-site includes are repointed to the JP counterpart that actually exists on scp-jp (KB-15); image-block and toggle-sidebar have JP ports.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the lists.
- **Disposition:** Standing, with the five exhibit self-references flagged (Per-theme record, item 1).

### 3. Delivery and code loading

- **What:** One delivery layer, the theme's own: the code exhibit (orig L187–1361 → cand L188–1362) is the page's local--code /1 on both sides. The original loads it by a page-URL self-import (orig L2: `theme:bloodraven/code/1` — a wikitext page URL, not a local--code path). The candidate loads it at the head by module CSS @import (cand L2) and by the interwiki-style include (cand L4–7), both naming the draft host (labels DELIVERY-HOST + DRAFT-HOST + SELF-DELIVERY). The frame defect and its fix: as created, the interwiki-style include carried no priority parameter — the LOCALIZE-ROWS row 65 pattern-6 charge (interwiki-style missing priority=1). FIX4-IWB (commit 5559209) added exactly one line, `| priority=1` (cand L5); the ledger's KB-07b note (lines 1678–1679) records this theme's missing-priority fix under FIX4-IWB. The include's theme parameter keeps a space after its `=` sign in the bytes (`| theme= https://…`, cand L6) — recorded as written; Wikidot include parameters tolerate it, and no register charges it. The four variant modules at the tail are parameter-gated module CSS blocks on both sides (orig L1367–1431 → cand L1372–1432); their only change is the colon-encoding of their asset URLs (B83–B86, section 4).
- **Why:** P4/T9: a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. KB-07 (patterns 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): an interwiki-style include without its priority leaves the frame's layering contract incomplete.
- **Verify:** Read orig L1–3 against cand L1–7; `git show 5559209 -- pages/theme:bloodraven-jp.txt` (one added line).
- **Disposition:** The missing priority is FIXED (GOSIGN2-LEDGER (c3): P6 FIXED, frame waves, checker-verified). The draft-host URLs (cand L2, L6) are class (iii) draft form, recorded in section 11.

### 4. Fonts and assets

- **What:** Fonts, all inside the code exhibit head (B79, orig L187–191 → cand L188–192). The original imports four stylesheets: Tilt Prism, Jost and Wallpoet from api.fonts.coollabs.io, and — from a sibling theme's file space on the EN wiki — `theme:valravn/comic-runes.css` (orig L189), which loads the two rune faces. The candidate imports Noto Sans JP first (cand L189), then the three display faces from fonts.googleapis.com (cand L190–192) — and the comic-runes import is gone, with no counterpart anywhere in the file (`grep -n 'comic' candidate.txt` finds only the surviving stack). That stack is real CSS: `font-family: 'comic_runesregular', 'nocurvesboustrophedonregular';` (cand L413, = orig L412) styles the theme's runic text, and neither face is loaded by anything the candidate imports. This is the dropped-import defect of Per-theme record, item 2. The JP supplement proper is B81 (JPFONT-STACK, orig L560–561 → cand L561–562): the body stack gains "Noto Sans JP" behind Jost. Assets: every display asset is an EN/author-site hotlink on both sides — the five exhibit images (section 2), the body backgrounds, and the variant modules' art on the author's own wiki (scp-yerko-7.wdfiles.com, under the ES theme tema:necropolitics' file space). The candidate's only asset-URL changes are the colon-encodings (B80: one body URL; B83–B86: the four variant zones, `tema:necropolitics` → `tema%3Anecropolitics`) and one repoint with its own story: the `.code` background fondo-code.png pointed at the EN theme's file space (orig L1048), where the file does not exist; FIX2-DEADREF (commit b33b69f) repointed it to the asset's real home, the author's own wiki under the ES theme's file space, same filename (cand L1049; block B82, labeled CSS-BODY). The repointed URL is still an author-site hotlink — class (ii) under pattern 5 — but the reference is no longer dead.
- **Why:** P7/T5: Jost has no Japanese glyphs, so without a JP face in the body stack, Japanese body text falls back to an OS-dependent generic. KB-17 (patterns 9c5e907): api.fonts.coollabs.io is outside the hotlink allowlist, so the three faces went to the canonical host. KB-16 family: a font import dropped while its stack survives leaves the styled text faceless — the failure the dropped-import flag exists to catch. P5 / KB-58: the asset hotlinks are the owner-deferred hosting state, class (ii); a dead reference inside that state is still repaired when its real home is known (the dead-reference evidence standard: same filename, author's own file space).
- **Verify:** `grep -n 'coollabs\|fonts.googleapis.com\|comic' candidate.txt` (coollabs absent; four googleapis imports; comic only at L413); read cand L561–562 against orig L560–561; read cand L1049 against orig L1048; `git show b33b69f -- pages/theme:bloodraven-jp.txt`.
- **Disposition:** Fonts: the coollabs repoint and the JP supplement are FIXED as part of the port; the comic-runes drop is FLAGGED (Per-theme record, item 2), not dispositioned — no register names it. Assets: DISPOSITIONED (ledger (c3): P5 = class (ii)/KB-58); the fondo-code repoint is FIXED (FIX2-DEADREF; the (c2) entry's KB-58 bracket and this fix are reconciled in section 11, item 2).

### 5. Header, sidebar, site furniture

- **What:** The candidate repoints the toggle-sidebar include (section 2) and carries the original's empty header div verbatim (cand L10–11). No header variables are overridden in a head block — this theme's header art and titles are CSS variables inside the code exhibit (`--logo`, `--banner-*`, `--header-*` family), carried unchanged except for the colon-encodings of section 4; the variant modules override the same variables per color. No HEADERVAR label fired, and direct inspection of the exhibit's :root blocks confirms the values are the original's. P8 does not engage: there is no BHL base here whose furniture could be inherited.
- **Why:** P9/T6 variables are overridden where the JP environment requires it; nothing in this theme's header layer required it.
- **Verify:** `grep -n -- '--logo\|--banner\|--header' candidate.txt` and compare values against original.txt.
- **Disposition:** Standing; no furniture item was charged for this theme in any register.

### 6. Text translation

- **What:** The candidate's prose is the original's body translated in place: the usage intro (cand L28, = the deleted info body), the five variant descriptions, the Examples section (B38: the "+* Examples" heading → 例）, the collapsible labels （コードを表示/コードを閉じる）, and the sample body. 19 blocks are anchor-paired; the 49 TRANS-UNANCHORED blocks and most of the heuristic mass are the same work without line anchors (one-line variant descriptions and exhibit-adjacent lines), each read against its original line — all are translations. In-CSS text (R1): the CSS comments stay in English verbatim (porter-visible only), including the section banners (/* ROOT */ and its siblings); no reader-visible string variable carries prose in this theme.
- **Why:** P10: body, usage and sample text are translated. KB-18 covers reader-visible strings; comments are not reader-visible, so their retention is recorded, not charged.
- **Verify:** Read orig L20–185 against cand L26–186; `grep -n 'Examples\|例' candidate.txt` (L91 zone).
- **Disposition:** Standing (the port itself). The localize T5 pass recorded no mistranslation finding for this theme; its display-affecting items are patterns 5, 6 and 11, decided in sections 3, 4 and 7.

### 7. Links

- **What:** The theme's one prose link is the Valravn Corporation hub link in the intro: the original names the EN hub by full URL (orig L12 and L23); the candidate keeps the full EN URL and labels it ヴァルラヴン社（英語版） (cand L28). That kept-EN link is the LOCALIZE-ROWS row 65 pattern-11 charge ("L27 links EN hub though JP…"). No JP hub page is named by any register as the counterpart, and the ledger closes the item in the sibling / batch-posting class: the link's target is a hub whose JP posting belongs to a sibling batch. The credit block's source link (cand L23) names the recorded host scp-wiki.wikidot.com, matching sources.tsv; no probe was needed. The license/source citations do not arise (no license box, section 1).
- **Why:** P11: links take the JP counterpart where it exists; where the counterpart is itself an unposted sibling candidate, the EN link with an explicit （英語版） label is the honest interim form, and the charge is dispositioned rather than silently fixed to a dead target.
- **Verify:** Read cand L28 against orig L12; T1-ROWS row 70 and the ledger (c3) pattern-11 line.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER (c3): P11 = sibling / batch-posting class).

### 8. Structure

- **What:** The localize.md closing rule is honored for the stylesheet: the code exhibit's rules, variables and order are preserved (the ~1,170 lines between B79/B81 and B82 are unchanged context), and the JP corrections sit at the frame, the exhibit head (imports) and one body stack (B81). The structural acts outside the CSS are the furniture swap of section 1 (info module + bare Rate out, preview credit in) and nothing else: the exhibit census is identical on both sides — five usage exhibits, five image-blocks (four screenshots plus the Valravn logo), the Examples section, the code collapsible, and the four gated variant modules. The six EXHIBIT-RESTRUCTURE labels adjudicate as follows: B3 (orig L4–5 → cand L8–9) is the head frame zone (toggle-sidebar repoint), not an exhibit; B15, B21, B27, B33 and the logo block are the image-block repoints of section 2. No exhibit was dropped, merged or reordered. One content deletion does exist, but it is not structural: the comic-runes @import inside the exhibit head (section 4, Per-theme record item 2).
- **Why:** Residue class R3: restructuring claims are checked against the exhibit census; here the census is unchanged and every EXHIBIT label is a repoint false-fire, which is exactly the adjudication this section exists to record.
- **Verify:** `grep -cn 'image-block\|Screenshot\|collapsible' original.txt candidate.txt`; read classification.json blocks B3, B15, B21, B27, B33.
- **Disposition:** Standing (no restructuring).

### 9. Formatting only

- **What:** No WS-ONLY label fired over 87 blocks, and this file's history has no tab-normalization commit (its three commits are 7e07438, b33b69f, 5559209 — creation and the two waves). One termination difference exists at the file tail (B87, the sole pure-residue block): the original's final line `[!----]` is unterminated (no trailing newline), while the candidate's is terminated and followed by an empty final line (cand L1441–1442). No content differs.
- **Why:** Formatting-only churn is disclosed as its own class; here the ground is the classifier's count plus the file's history.
- **Verify:** classification.json (no WS-ONLY blocks); `tail -c 20 original.txt | od -c` against the same for candidate.txt.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. No `[!-- ... --]` porter note, no 訳注， and no added CSS comment header exists in this candidate (`grep -c '\[!--' candidate.txt` counts only the original's own variant-gate comments `[!-- {$frostblood-raven}` and siblings at the tail, which are the original's mechanism, carried verbatim — not annotations). No annotation signature fired, and direct inspection of the frame, exhibit head and tail finds no porter addition.
- **Why:** R2: porter additions are listed so they are never mistaken for original content; here the ground for "none" is the grep plus inspection, stated explicitly because annotations elsewhere ride inside other labeled blocks.
- **Verify:** `grep -n '\[!--' candidate.txt` (only the four variant gates); read cand L186–193 against orig L185–192.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The T1 row's 42 hotlink errors and 1 pseudo-ref: T1-ROWS row 70 records exit 1 with 43 errors (hotlink×42, pseudo-ref×1), 1 warn, 1 info. The hotlinks are the pattern-5 asset set — DISPOSITIONED, class (ii)/KB-58 (the (c1) hotlink formula: no fetchable JP storage copy exists for these assets; the bytes are original-identical or author-hosted). The pseudo-ref is the draft-host own delivery (cand L2, L6) — class (iii). (2) The render row's combined finding (missing priority + dead fondo-code.png): the (c2) entry DISPOSITIONS it under KB-58, yet the bytes carry two fixes — the priority line (FIX4-IWB) and the fondo-code repoint (FIX2-DEADREF) — and the (c3) register names both: P6 FIXED, and pattern 5's line names "FIX2-DEADREF repoints (bloodraven, eigenmachine)" among its named fixes inside the class. This package follows the bytes and the (c3) register: both items FIXED, with the KB-58 bracket read as covering the remaining hotlink state, not these two repairs (Per-theme record, item 4). (3) The webkit-375 cluster: DISPOSITIONED, a transient Wikidot 503 capture, not a defect (KB-44). (4) Pattern 11 (the EN hub link): DISPOSITIONED (section 7). (5) FLAGGED by this package, not dispositioned: the five plain-slug usage exhibits (cand L32, L50, L62, L74, L86) and the dropped comic-runes import (orig L189; surviving stack cand L413) — see the Per-theme record. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1, 3, 4); item 2 recorded as FIXED per the bytes; item 5 flagged for the repair sweep and the record.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 43 errors / 1 warn / 1 info; the errors are hotlink×42 and pseudo-ref×1 (section 11, item 1) (T1-ROWS row 70). Register (c1) dispositions both classes ((ii) and (iii) respectively). (b) T2/T3 render: FINDINGS — the combined priority/dead-asset finding (fixed, section 11 item 2) and the 503 capture (KB-44); the row records no credit-modal error for this theme, and engine coverage is the lane's full matrix as run (RENDER-ROWS-1). (c) T4 localize: FINDINGS with 3 display-affecting items (patterns 5, 6, 11 — sections 3, 4, 7). (d) T5: judged jointly with T4; no mistranslation finding stands. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (87 change blocks) and the generator's (diff.md: +185/−192 in 9 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:bloodraven-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 65).

## Per-theme record

### Item 1 — the five usage exhibits name a page that will not exist (flagged by this package)

Each usage exhibit reads `@@[[include :scp-jp:theme:bloodraven …]]@@` (cand L32, and with the variant parameters at L50, L62, L74, L86). The originals name `:scp-wiki:theme:bloodraven` — correct on their own wiki. The port repointed the site prefix to `:scp-jp:` but kept the plain slug in all five; the candidate itself posts as theme:bloodraven-jp, so every exhibit instructs readers to include a page that will not exist under that name on scp-jp. No register charges the lines. This package flags them for the population sweep repairing this family; the candidate is not edited here (review packages never edit candidates).

### Item 2 — the dropped runes import with its stack surviving (flagged by this package)

The original imports `comic-runes.css` from the sibling theme:valravn's file space (orig L189), loading 'comic_runesregular' and 'nocurvesboustrophedonregular'. The candidate's exhibit head (cand L189–192) imports Noto Sans JP and the three Google faces only; the runes import has no counterpart. The consuming rule survives verbatim: `font-family: 'comic_runesregular', 'nocurvesboustrophedonregular';` (cand L413). Neither face is loaded anywhere else in the file or by any include (the theme has no base), so the runic text falls back to a generic face. No ledger line, localize charge or render finding names the drop; the localize row's pattern-5 charge covers hotlinked assets as a class, but this is the reverse shape — an import removed, not kept. This package flags it as a KB-16-family defect for the repair queue: the fix is to restore the import (repointed per the asset rules) or to record a disposition; neither is done here.

### Item 3 — wave attribution, checked against the bytes (bloodraven)

The ledger's (c3) formula closes this theme's credit fields among the credit waves' work. The file's history has exactly three commits (7e07438 creation, b33b69f FIX2-DEADREF, 5559209 FIX4-IWB): FIX-CREDIT-D (1869877) never touched this file. Its translator normalization (`SCP-JP` → `AI`, cand L17) landed inside FIX2-DEADREF (b33b69f), the dead-reference wave. The claimed outcome is true of the current bytes; only the wave attribution differs. This package follows the git record.

### Item 4 — the (c2) bracket versus the (c3) register (bloodraven)

The render register's (c2) entry dispositions the combined priority/fondo-code finding under KB-58 ("missing/404 decorative assets are the owner-deferred hosting state"), while the bytes carry both repairs and (c3) names them as fixes. The readings reconcile if the KB-58 bracket is scoped to the hosting state that remains (the 42 hotlinks), which is how sections 4 and 11 record it; read unscoped, the (c2) line would contradict the FIX2-DEADREF commit in the same campaign's history. Flagged here as a record-reading note, not a defect in the candidate.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-bloodraven-jp.txt` — the render sample page the T2/T3 checks rendered. (2) `pages/theme:bloodraven.txt` — the repo's EN-side copy of the original page, the EN sample's base. (3) The delivery itself: the candidate's own local--code /1 on the draft host, named by the frame (cand L2, L6), which is the runtime form of the code exhibit in this package.

## Multi-wave provenance

The candidate's current state is the product of three commits and three check waves: Stage 2 EN5 created it (commit 7e07438: translation, credit block, font repoints and supplement, the comic-runes drop, the frame without its priority line); LOCALIZE-S2-A then examined that state and charged patterns 5, 6 and 11 (LOCALIZE-ROWS row 65); the render lane (RENDER-S2-A) recorded the combined priority/dead-asset finding and the 503 capture; FIX2-DEADREF (commit b33b69f) repointed fondo-code.png to its real home and, in the same commit, normalized the translator field; FIX4-IWB (commit 5559209, the file's last content change and this package's computed-against commit) added the priority line; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 65, (c1) hotlink and pseudo-ref entries, (c2) bloodraven entry, (c3) bloodraven entry and the KB-07b note at lines 1678–1679; GOSIGN2-LEDGER-SUPPLEMENT.md (no bloodraven entries); T1-ROWS row 70; LOCALIZE-ROWS row 65; RENDER-ROWS-1 (RENDER-S2-A) bloodraven row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted 56 open blocks (7 residue, 49 heuristic). All are resolved; none required a new signature. Five of the seven residue blocks are the usage-exhibit lines themselves, each paired by the differ with the one-line prose translation that precedes it; they are resolved individually because they carry item 1's flag. The heuristic mass is prose translation whose script delta defeats the anchor majority, plus one CSS case noted individually.

- **R1 — B9 (residue; orig L22–23 → cand L31–32).** The usage intro sentence (translated at cand L28) paired with the first usage exhibit (cand L32). The exhibit line is item 1's first instance. Resolved in sections 2 and 6.
- **R2 — B18 (residue; → cand L49–50).** The Frostblood one-line description ("Good for tales on winterlands.", translated) paired with its exhibit (cand L50). Resolved in sections 2 and 6; the exhibit is item 1's second instance.
- **R3 — B24 (residue; → cand L61–62).** The Sunblood description and exhibit (cand L62). As R2.
- **R4 — B30 (residue; → cand L73–74).** The Acidblood description and exhibit (cand L74). As R2.
- **R5 — B36 (residue; → cand L85–86).** The Paleblood description and exhibit (cand L86). As R2.
- **R6 — B38 (residue; → cand L91–92).** The "+* Examples" section heading, translated (+* 例）. Resolved in section 6.
- **R7 — B87 (residue; orig L1440 → cand L1441–1442).** The file tail: both files end with the line `[!----]`; the original leaves it unterminated, the candidate terminates it and adds an empty final line. Termination only; no content. Resolved in section 9.
- **R8 — B82 (heuristic, CSS-BODY; orig L1047–1048 → cand L1048–1049).** The fondo-code.png repoint — a one-line URL change inside a CSS rule, which is why the differ's CSS-BODY reading stands as its mechanical label. The mechanism is the FIX2-DEADREF dead-reference repair, resolved in section 4.
- **R9 — the remaining heuristic mass (TRANS-UNANCHORED siblings).** One-line and short prose translations across the usage, variant and Examples sections, each read against its original line. Resolved in section 6 by shape.
