# Review package — theme:black-market-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:black-market-jp — origin EN, population #62 [GOSIGN2-LEDGER (b) row 62]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 147c95237ecb6b6b110154dd5ccd5a78622668c40b9cccf085eaa0ef7665cd2e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 0 infos (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 67; GOSIGN2-LEDGER (b) row 62]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — port defect: duplicate `interwiki-style` priority=1; sample machine verdict missing after one retry (page-open failure, documented), sample T3 from surviving screenshots only. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 62, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 62]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 62]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:black-market-jp.txt sha256:147c95237ecb6b6b110154dd5ccd5a78622668c40b9cccf085eaa0ef7665cd2e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/black-market-jp/candidate.txt (sha256 e1e9de4daef943f3d7f598ddc4575afb6d87955c5a21b5d061e979482532f388)
Original: theme:black-market — scp-wiki, revision 35 (sha256 c82bd72330591ad015bd297e098876e5f159f2868fb595736ecabbfcc985154a)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 62); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no black-market entries |
| Fixed after the localize check | The duplicate `interwiki-style` priority (FIX4-IWB, commit 5559209: priority=1 → 3, one line) and the translator-attribution normalization (FIX-CREDIT-D, commit 1869877) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref×4 (draft-host lines, classes (ii)/(iii)); the #6 interwiki registration form as a staff-confirmation item; license confirmation for the two images and mcdLogo.css at posting |
| Coverage caveat | The render row's sample machine verdict is missing after one retry (page-open failure, documented in the row); the sample T3 rests on surviving screenshots only |
| Flagged by this package | The usage exhibit's self-reference names the plain slug (candidate L39) — see the Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:black-market | theme:black-market-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 35, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 35 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-black-market.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:black-market-jp.txt`, created in commit 053fd41 (Stage 2 EN4); later content changes in ab523f4, 1869877 and 5559209 |
| Lines / bytes | 225 lines / 6,387 bytes | 248 lines / 7,997 bytes |
| SHA-256 | c82bd72330591ad015bd297e098876e5f159f2868fb595736ecabbfcc985154a | e1e9de4daef943f3d7f598ddc4575afb6d87955c5a21b5d061e979482532f388 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted (no R4): the candidate's stylesheet is the original's own code exhibit carried in place, and its body is the original's, translated. Reference-revision currency: the upstream original has moved past revision 35 since the port; the follow-up artifact `diff-black-market-from35.txt` in the campaign record carries that later delta (sources.tsv kind K5a-i). This package judges the port against the revision it was made from.

## Summary

Black Market is an MC&D theme on a Black Highlighter base. The original splits its delivery across both ends of the page: BHL stylesheets and the MC&D logo-animation stylesheet are @imported in a head module and registered by two EN interwiki-style includes (priorities 1 and 2), while its own stylesheet — a code exhibit served as the page's local--code /1 — is loaded at the tail by a module @import and a third interwiki-style include (priority 3), followed by the BHL dark-sidebar component. The candidate consolidates all of that into the JP head frame: the JP BHL page include, its own /1 by module @import and a single priority=3 interwiki-style include, and the dark-sidebar component repointed and moved up into the frame. The body (usage, table demo, theme-squares palette, code exhibit) survives entire and translated; the bare Rate is deleted for the preview credit block, and a license box is added for the theme's three assets. The classifier sees only 9 change blocks because the differ aligns the consolidated head and the moved body as single large blocks; the narration below follows diff.md's five hunks and direct reading. Two later waves touched the file beyond its creation-era tab normalization: FIX-CREDIT-D's translator line and FIX4-IWB's priority repair. One exhibit line escaped both: the usage example's plain-slug self-reference (Per-theme record).

## Classification

| Label | Blocks |
|---|---|
| WS-ONLY | 3 |
| DRAFT-HOST | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| TRANS-UNANCHORED | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| HEADERVAR | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Counts: 9 blocks — 9 specific (100%), 0 heuristic, 0 residue, 0 skipped. The small block count is a differ artifact, disclosed in the Summary: B2 spans orig L3–5 → cand L4–92 (the head frame plus the body the differ aligned with it) and B3 spans orig L14–90 → cand L100 (the deletion side of the same restructure), so the per-section reading below cites diff.md's hunks and line numbers, not block granularity. Topology: no relocation of the stylesheet body; the code-css exhibit (orig L81–215) is the candidate's (cand L79–225) at a near-constant offset. Labels are sets per block, and these sections were written from classification.json's label spans together with the diff.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's frame is split: a head module (orig L2–6) @importing the two BHL stylesheets from nu-scptheme.github.io and mcdLogo.css from scp-wiki.wdfiles.com, two EN interwiki-style includes at priorities 1 and 2 for the BHL pair, and — after the closing `[[/iftags]]` — a tail module @importing the page's own EN /1, a third interwiki-style include at priority=3 for the same /1, and the `:scp-wiki:component:bhl-dark-sidebar` include (orig L218–225). The candidate's frame is consolidated at the head (cand L1–14): the `:scp-jp:theme:black-highlighter-theme` include (L1), a module CSS @importing the candidate's own /1 from the draft host (L3–5), one `:scp-jp:` interwiki-style include at priority=3 naming the same /1 (L7–10), the dark-sidebar component repointed to `:scp-jp:` (L12), and the localized gate (L14). Provenance route: derived from the original at reference revision 35 (see Provenance); no R4 adoption.
- **Why:** The frame is where the original declares its delivery; P1/P2/P4/P6 rework exactly this frame, and each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–13 and L217–225 against candidate L1–14; diff.md hunks 1 and 5.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a right-aligned div (orig L31–33) and the CSS comment header inside its code exhibit (orig L84–91: created by Randomini for the 2014 GoI Contest, based on Sigma-9, updated later by stormbreath, all images by Randomini). The candidate deletes the bare Rate (B3 carries BARE-RATE-DEL) and installs the preview credit block (cand L21–30): all eight ruling-3 fields, with 著作権者 naming both [[*user Randomini]] and [[*user stormbreath]] — the creator and the updater the original's header names; nobody is dropped. The comment header is carried inside the moved exhibit with one line added (cand L87: "Ported for SCP-JP (theme:black-market rev 35)"; section 10). A license box is added before the gate close (cand L228–247, B8): `:scp-jp:component:license-box-backend` (author=Randomini, stormbreath) with entries for mcdpride.png, mcd.png and mcdLogo.css, each stating that the original records no license and the author must be asked before posting. No T7 credit-module CSS was added (no T7-CREDIT-CSS label fired; the rate-box rules the candidate carries at cand L203–210 are the original's own, tab-normalized).
- **Why:** P3/T1: the preview credit module is rate-bearing, so a separate bare Rate would duplicate the widget (KB-09, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 fixes the eight fields and credits campaign translations to AI. T4/KB-60: the license box is a supplement where the original had none, in the author-confirmation form the original's silence requires.
- **Verify:** Read candidate L21–30 against the eight-field list and original L84–91; `grep -n 'module Rate' candidate.txt` (absent) against original L32; read candidate L228–247.
- **Disposition:** Standing (the port's credit form); the ledger closes the credit fields FIXED (register (c3)).

### 2. Includes and components

- **What:** The candidate's include list (grep): the JP BHL theme page (L1), the interwiki-style frame (L7–10), the dark-sidebar component (L12), the credit pair (L21/L30), the escaped usage pair (L38–39), the theme-squares component repointed to `:scp-jp:` (cand L48–), and the license-box pair (L228/L247). Changes: (a) theme-squares repointed `:scp-wiki:` → `:scp-jp:` with its parameters carried and its color names translated (アイザベリン, ブラックコーヒー, オーキッド, ビザンティン, ロイヤル, ティリアン); (b) bhl-dark-sidebar repointed and moved from the tail (orig L218, outside the gate) into the head frame (cand L12, outside the gate in the same relative sense — before the gate opens); (c) the usage exhibit's escaped includes repointed to `:scp-jp:` — with one survivor defect, the self-reference at cand L39, flagged in the Per-theme record. No `:scp-wiki:` include remains (grep: none). No T8 swap was needed; ruling 4 does not engage.
- **Why:** P1: foreign-site includes are repointed to the JP counterpart that actually exists on scp-jp (KB-15); both components have JP ports.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the lists.
- **Disposition:** Standing, with the cand L39 self-reference flagged (Per-theme record).

### 3. Delivery and code loading

- **What:** Three delivery layers, consolidated. (1) The base: the original @imports BHL's two stylesheets from nu-scptheme.github.io (head module) and registers them by interwiki at priorities 1/2. The candidate loads the base by page include (cand L1); inside its code exhibit — the /1 source — the same two stylesheets are @imported from the JP BHL distribution, scp-jp.github.io (cand L89–90). (2) The logo animation: the original @imports mcdLogo.css from a shared EN file page (scp-wiki.wdfiles.com/local--files/svg-animation/, head module). The candidate's exhibit @imports it from the candidate's own draft-host files (cand L92, local--files/theme%3Ablack-market-jp/mcdLogo.css) — an own-file copy, class (ii) at posting, with its license-confirmation item recorded (sections 4 and 11). (3) The theme's own layer: the code exhibit is the page's /1 on both sides; the original loads it at the tail (module @import of the EN /1 + interwiki priority=3, orig L219–225), the candidate at the head (module @import, cand L4; interwiki, cand L7–10), both draft-host in the candidate (labels DELIVERY-HOST + DRAFT-HOST + SELF-DELIVERY on B2/B9). The frame defect and its fix: as created, the candidate's own interwiki-style sat at priority=1, duplicating the base layer's registration — the render row's port defect. FIX4-IWB (commit 5559209) changed exactly one line, priority=1 → priority=3 (cand L8), the BHL split form (base 1/2, own 3).
- **Why:** P4/T9: deliveries are served from JP hosts in this environment; a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. KB-07 (patterns 9c5e907): duplicate interwiki-style priorities leave the layering order undefined; the split form is the registered shape.
- **Verify:** Read orig L2–13 and L218–225 against cand L1–12 and cand L89–92; `git show 5559209 -- pages/theme:black-market-jp.txt` (one line).
- **Disposition:** The duplicate priority is FIXED (GOSIGN2-LEDGER (c2), FIX4-IWB). The draft-host URLs (cand L4, L9, L92) are class (iii)/(ii) forms, recorded in section 11. The #6 registration-form item is DISPOSITIONED as a staff-confirmation form item (ledger group entry for bedbugs/black-market/black-serpent).

### 4. Fonts and assets

- **What:** Fonts: neither side loads a webfont for this theme — its stacks are BHL's, inherited with the base — so no P7 supplement was needed and no font label fired beyond the delivery blocks; the ground for "no font change" is the pair's import lists (sections 0 and 3), which contain stylesheets only. Assets: the theme's two images and its logo-animation stylesheet. The CSS variables --logo-image and --gradient-header are repointed from the original's EN file paths to the candidate's own draft-host files (B5, orig L100–101 → cand L110–111: mcdpride.png, mcd.png), and mcdLogo.css rides the exhibit import (cand L92, section 3) — all class (ii) own-attachment forms. The license box (cand L228–247) records all three assets with their EN source links and the author-confirmation wording; the LOCALIZE-ROWS row 62 note names the license confirmation for the images and mcdLogo.css as a pre-posting item.
- **Why:** P5: own attachments ride the draft host at draft stage and are re-hosted to SCP-JP storage at posting (class (ii)); re-upload by the campaign is barred by owner order, and unknown-license assets are confirmed with the author rather than silently carried (the dead-reference/asset evidence standard).
- **Verify:** `grep -n 'local--files' candidate.txt` (L92, L110, L111 own draft-host paths; the license box's source links name the EN originals); read orig L99–101 against cand L109–111.
- **Disposition:** DISPOSITIONED (ledger (c3): asset hosts = class (ii); LOCALIZE-ROWS row 62 posting items).

### 5. Header, sidebar, site furniture

- **What:** HEADERVAR fired on B5: the --logo-image / --gradient-header pair (section 4). The theme defines no --header-title/--header-subtitle of its own (the header text is BHL's furniture, inherited), so no header-language item arises for this theme — the ledger (c3) line's generic "header language = ruling 2" wording has no instance here, and this package does not claim one. The sidebar furniture is the bhl-dark-sidebar component, repointed and repositioned in section 2; no P8 layout adaptation was made.
- **Why:** P9/T6 variables are overridden where the JP environment requires it; this theme's only variable-level changes are its asset URLs.
- **Verify:** `grep -n 'header-title\|header-subtitle' candidate.txt` (absent); read cand L109–111.
- **Disposition:** Standing; no furniture disposition is claimed.

### 6. Text translation

- **What:** The candidate's prose is the original's body translated in place, entire: the usage section (cand L32–42: the note, the import instruction), the table demo (cand L44–47), the theme-squares palette (names translated, section 2), and the collapsible labels ("+ テーマのコードを表示"). Only 2 blocks carry TRANS-UNANCHORED because the differ aligned the body into the large B2/B3 pair; the translation itself is complete — no body paragraph in the original lacks a candidate counterpart. In-CSS text (R1): the CSS comments stay in English verbatim (porter-visible only), and the string variables --theme-base "nuscp" / --theme-id "black-market-theme" / --theme-name "Black Market Theme" are carried unchanged (BHL/Sigma registration values, not reader text).
- **Why:** P10: body and usage text are translated. KB-18 covers reader-visible strings; comments and registration variables are not reader-visible, so their retention is recorded, not charged.
- **Verify:** Read orig L36–78 against cand L32–77; `grep -n 'theme-name' candidate.txt`.
- **Disposition:** Standing (the port itself). The localize T5 pass recorded no mistranslation finding for this theme; its one display-affecting item is the #6 form item (section 3).

### 7. Links

- **What:** The candidate's prose links are the usage note's BHL link (`[[[theme:black-highlighter-theme|詳しくはこちら]]]`, cand L34 — a same-site bare link naming the JP BHL page, which exists) and the credit block's source link (cand L29, to the EN original — the required ruling-3 back-reference, host matching sources.tsv's recorded scp-wiki.wikidot.com; no probe needed). The license box's source links name the EN originals' file URLs as citations (cand L234, L239, L244). No other prose links exist on either side.
- **Why:** P11: the BHL link's referent is the JP page a reader must also load, so it takes the JP form; citations of the originals keep their original targets.
- **Verify:** `grep -n 'theme:black-highlighter-theme\|\[\*' candidate.txt` and read each hit's role.
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** Two structural acts, both delivery-driven. (a) The frame consolidation (section 0): the original's tail delivery zone (orig L218–225 — sidebar include, tail module, tail interwiki) is dissolved into the head frame; the differ records it as B9 (orig L218–225 → cand L248, the gate close) with EXHIBIT-RESTRUCTURE + SELF-DELIVERY labels — it is not an exhibit, and nothing it carried was dropped: the sidebar is at cand L12, the own-layer loads at cand L4/L9. (b) The bare Rate's deletion inside B3, decided in section 1. Everything else is preserved under the closing rule: the body order (usage, demo, palette, exhibit) is the original's, the stylesheet's rules and order are unchanged apart from the tab normalization (section 9) and the header asset lines (section 4), and the JP additions sit at the frame and at the body's tail (the license box, cand L228–247, inside the gate before its close — the supplement position). The mcdLogo div moves with the frame's logic: in the original it follows the interwiki includes (orig L14–15 area); in the candidate it follows the gate (cand L16–17), ahead of the credit block. The exhibit census (table demo, theme-squares, code exhibit, collapsible) is identical on both sides.
- **Why:** Residue class R3: the ground for each labeled block is stated; here the census and the delivery reading decide — a consolidation of delivery lines, not a deletion of content.
- **Verify:** `grep -n 'theme-squares\|code type\|collapsible\|bhl-dark-sidebar' original.txt candidate.txt` and compare; blocks B3/B9 in classification.json.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** 3 WS-ONLY blocks (B4, B6, B7), all one act: the EN4 tab-normalization commit (ab523f4, "normalize code-block tabs to spaces") rewrote the code exhibit's tab-indented lines to 8-space indentation (65 lines changed in that commit, all inside the exhibit: the :root variable lines, the mobile @media block, the rate-box gradient lines visible in diff.md hunks 2–4). Content lines' text is otherwise untouched. This is R7 formatting normalization, disclosed as its own class: it was a deliberate campaign commit applied to the EN4 batch, not porter drift, and its follow-up-diff cost is the recorded trade-off of that commit.
- **Why:** R7: wholesale re-indentation defeats follow-up-diff applicability, so explanations must disclose it in this section even when, as here, it was a considered batch decision.
- **Verify:** `git show ab523f4 -- pages/theme:black-market-jp.txt` (65 insertions, 65 deletions, whitespace only); classification.json (3 WS-ONLY blocks).
- **Disposition:** None required (recorded).

### 10. Porter annotations

- **What:** One porter addition: the editor line inside the CSS comment header, "Ported for SCP-JP (theme:black-market rev 35)" (cand L87), added to the original's own header (which is otherwise carried verbatim, cand L81–88). No `[!-- ... --]` notes and no body 訳注 exist (`grep -c '\[!--' candidate.txt` = 0); no annotation signature fired, and direct inspection finds nothing else.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation.
- **Verify:** Read cand L81–88 against orig L84–91.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The candidate's draft-host lines (cand L4, L9, L92, L110–111): T1 pseudo-ref×4 as extracted in T1-ROWS row 67 — DISPOSITIONED, classes (ii)/(iii) (posting rewrites the own-code host to scp-jp.wdfiles.com and re-hosts the own attachments; GOSIGN2-LEDGER (c1) pseudo-ref entry). (2) The #6 interwiki registration form: DISPOSITIONED as a staff-confirmation form item (ledger group entry); its display-relevant half (the duplicate priority) is FIXED. (3) The asset re-hosting and the license confirmations for mcdpride.png, mcd.png and mcdLogo.css: posting-time items recorded in LOCALIZE-ROWS row 62, with the confirmation need stated in the candidate's own license box. (4) The render row's missing sample machine verdict: a coverage caveat, not a finding (section 12). (5) FLAGGED by this package, not dispositioned: the usage exhibit's plain-slug self-reference (cand L39) — see the Per-theme record. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 recorded; item 5 flagged for the repair sweep.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 4 errors / 1 warn / 0 infos; the errors are pseudo-ref×4 (section 11, item 1); the warn code is not itemized in the extracted row (T1-ROWS row 67). Register (c1) dispositions the pseudo-ref class as (ii). (b) T2/T3 render: FINDINGS — the duplicate-priority port defect, FIXED by FIX4-IWB after the render pass. Coverage caveat, recorded in the row itself: the sample's machine verdict is missing after one retry (page-open failure), so the sample T3 rests on surviving screenshots only; the row records no credit-modal error for this theme, and engine coverage is otherwise the lane's full matrix (RENDER-ROWS-1). (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting item (#6, the form item of section 3); the follow-up currency check is the K5a-i artifact `diff-black-market-from35.txt`, recording the upstream delta after revision 35 — the port is judged at its reference revision. (d) T5: judged jointly with T4; no mistranslation finding stands. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (9 change blocks, with the coarseness disclosed in the Classification section) and the generator's (diff.md: +122/−99 in 5 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:black-market-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 62).

## Per-theme record

### Item 1 — the usage exhibit names a page that will not exist (flagged by this package)

The usage exhibit's second line reads `> @@[[include :scp-jp:theme:black-market]]@@` (cand L39). The original's line names `:scp-wiki:theme:black-market` — correct on its own wiki. The port repointed the site prefix to `:scp-jp:` but kept the plain slug; the candidate itself posts as theme:black-market-jp, so the exhibit instructs readers to include a page that will not exist under that name on scp-jp. The first exhibit line (cand L38, `:scp-jp:theme:black-highlighter-theme`) is not an instance: that is the JP BHL page's actual name. No register charges the line. This package flags it for the population sweep repairing this family; the candidate is not edited here (review packages never edit candidates).

### Item 2 — wave attribution, checked against the bytes

The ledger's (c3) line closes this theme's row charges with the generic class outcomes, "credit fields FIXED by the credit waves" among them. The file's history: the credit block was present from creation (053fd41), and the only credit-wave commit that touched the file, FIX-CREDIT-D (1869877), changed exactly one line — the translator field, `SCP-JP` → `AI`. The claimed outcome is true of the current bytes; only the attribution granularity differs, and this package follows the git record. The same discipline applies to the tab normalization: it has its own commit (ab523f4) between creation and the check waves, and section 9 records it under that commit rather than under the port.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-black-market-jp.txt` — the render sample page the T2/T3 checks rendered. (2) `pages/theme:black-market.txt` — the repo's EN-side copy of the original page, the EN sample's base. (3) The delivery itself: the candidate's own local--code /1 on the draft host, named by the frame (cand L4, L9), which is the runtime form of the code exhibit in this package; and the own-file copy of mcdLogo.css under the candidate's draft-host file space (cand L92).

## Multi-wave provenance

The candidate's current state is the product of four commits and three check waves: Stage 2 EN4 created it (commit 053fd41: translation, credit block, license box, frame consolidation, own-layer frame at priority=1) and normalized its code-block tabs in a follow-up commit (ab523f4); LOCALIZE-S2-A then examined that state and charged #6 (interwiki form) plus the posting-time items (LOCALIZE-ROWS row 62); the render lane (RENDER-S2-A, EN4) found the duplicate-priority defect and recorded the sample coverage caveat; FIX-CREDIT-D (commit 1869877) normalized the translator field; FIX4-IWB (commit 5559209, the file's last content change and this package's computed-against commit) repaired the priority; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 62, (c1) pseudo-ref entry, (c2) black-market entry, (c3) black-market entry and the §(c3) group entry on #6/#9; GOSIGN2-LEDGER-SUPPLEMENT.md (no black-market entries); T1-ROWS row 67; LOCALIZE-ROWS row 62; RENDER-ROWS-1 (RENDER-S2-A) black-market row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted no residue or heuristic blocks for this pair (9 blocks, all specific). The open shapes a reviewer might expect are accounted for in the standing sections: the large B2/B3 pair is the head-and-body restructure (sections 0, 3 and 8, with its coarseness disclosed in the Classification section), the three WS-ONLY blocks are the tab normalization (section 9), and B9 is the dissolved tail delivery zone (section 8). No new signature is proposed from this theme; the coarse-block shape itself is carried to the lane report as a classifier observation.
