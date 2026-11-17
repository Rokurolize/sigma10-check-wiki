# Review package — theme:vanguard-supplement-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:vanguard-supplement-jp — origin EN, population #156 [GOSIGN2-LEDGER (b) row 156]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4cbdf8d33a257ca37764871acd872b786403008f750a11373ee96449632d16af); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 2 warns / 2 infos (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 171; GOSIGN2-LEDGER (b) row 156]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page T2 no machine verdict (exit 2, no summary); sample hidden-rate (all combos) + page-overflow 330–335px@320 + 884px@768 + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 156, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 156]
- FIX5 re-judgement: item 38 (class B) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 38]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:vanguard-supplement-jp.txt sha256:4cbdf8d33a257ca37764871acd872b786403008f750a11373ee96449632d16af; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:vanguard-supplement` on scp-wiki (EN), revision 17 — `original.txt` in this package (4,411 bytes; `wc -l` reports 224, last line unterminated) |
| Candidate | `theme:vanguard-supplement-jp` — `candidate.txt` (261 lines / 7,113 bytes), a byte copy of `pages/theme:vanguard-supplement-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): a supplement sub-theme that renders by including its parent theme hidden and overriding its variables. The port repoints the parent include to the parent's JP candidate, adds the standard head frame, swaps in the preview credit, adds the JP license box, re-hosts the logo, applies the JP font supplement, and translates the body. |

This theme's `review/sources.tsv` note reads "first-translation rev 17": it makes no supersession claim, and no correction is owed for this package.

Status note: the verdict stamp above reads STALE by design. The stamp was computed against canonical commit b5cb724 — the usage-example sweep changed the candidate (its usage lines) after the FIX5 verdict was computed. The stamp's verdicts describe the pre-sweep file; the per-theme record below re-derives the theme's one blocking item on the current bytes, which is the point of the STALE form.

Summary: a supplement to `theme:scp-human-resources-sigma`. The port repoints the hidden parent include to the parent's JP candidate, adds the priority-1 head frame the original lacks, replaces the labelled bare Rate region with the preview credit block, adds a license box for the parent theme, re-hosts the header logo to SCP-JP storage, loads the parent's Latin faces from Google Fonts alongside a Noto Serif JP supplement, and translates the body and the slogan. The theme carried one blocking item, 38 (class B), re-derived in the per-theme record. One minor defect flag stands: the head module's Latin font imports duplicate the parent candidate's own loads, and one imported family is applied nowhere in the delivery chain (section 4).

## Class summary

| Label | Blocks |
|---|---|
| ASSET-REHOST | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 2 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 2 |
| ESCAPED-INCLUDE | 2 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 3 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 10 |
| TRANSLATION-ANCHORED | 1 |

Counts: 19 blocks, 10 specific, 8 heuristic, 1 residue, 0 skipped (comment text). Topology: module-css + code-css on both sides, no moves, external own delivery true.

## 1. Credit and attribution

- The original has no credit block; its attribution is the code-block banner (original L55–61: "By macro_au_micro", "adapted from code by Placeholder McD", "based on Sigma 9 by Aelanna and Dr Devan"). The candidate's credit block (candidate L19–29; block B4, CREDIT-PREVIEW + TASL-FIELDS) carries the ruling-3 fields: 著者 `macro_au_micro` (L23) and 著作権者 `macro_au_micro` (L25) name the person the original names, and the 著者 line also carries the parent-theme attribution with its CC BY-SA 3.0 / rev 13 reading note. Placeholder McD, Aelanna and Dr Devan stand in the code banner (candidate L74–80), carried verbatim — the original's own attribution carrier for them. No pointer-in-place-of-a-name defect stands. Ledger (c3): P3 credit fields FIXED by the credit waves, checker-verified.
- The labelled bare `[[module rate]]` at original L11–14 is this theme's blocking item 38; the per-theme record re-derives its removal. Census: `[[module rate]]` (any case) 1 → 0 (class P3 / KB-09, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa: the preview credit module is rate-bearing).
- License box (block B19): the original carried no license box; the candidate adds one (candidate L245–260) in the JP backend form with `author=macro_au_micro` — a T4 supplement applied as an addition. Its two entries are both about the parent theme (the parent theme itself; `hrlogo.png`, whose author and license are recorded as 記載なし）. The candidate's own header logo (section 4) has no entry; the sibling vanguard-jp package's box likewise omits its re-hosted logo. Recorded as an observation matching the sibling's practice, not a drop: nothing else the candidate loads lacks an entry.
- Verify: `grep -ci 'module rate'` on both files (1 / 0); read candidate L19–29 and L245–260 against original L55–61.

## 2. Includes and components

- The supplement mechanism: a hidden div (original L7–9) includes the parent theme, and the theme's own CSS overrides the parent's variables. The candidate repoints the include to `[[include theme:scp-human-resources-sigma-jp]]` (candidate L16; block B3, COMPONENT-SWAP + INCLUDE-REPOINT). The bare fullname form (no `:scp-jp:` prefix) differs from the usage example's form (candidate L42) but resolves on-wiki the same way; a form difference, recorded, not a defect.
- Live includes: the head frame (section 3), the hidden parent include, the credit pair (section 1), the license pair (section 1).
- Usage examples (blocks B8, B10): the self and parent examples are repointed to `:scp-jp:` forms (candidate L42–43), and the toggle-sidebar example names `:scp-jp:component:toggle-sidebar` (candidate L49). Probed by this lane on 2026-11-17: `https://scp-jp.wikidot.com/component:toggle-sidebar` serves 200, so the repointed example resolves. Block B10's EXHIBIT-RESTRUCTURE primary is a false fire — a mere include repoint inside an exhibit region.
- Verify: `grep -n 'include' candidate.txt`.

## 3. Delivery and code loading

- The original delivers through a head `[[module CSS]]` (original L1–3) importing its own `/1` from `scp-wiki.wikidot.com`, standing outside its gate (the gate opens at original L5). The candidate's head module (candidate L1–6; block B1: DELIVERY-HOST + DRAFT-HOST + FONT-IMPORT + JPFONT-LOAD + SELF-DELIVERY) imports own `/1` from the draft host and adds the font loads (section 4).
- The candidate adds the standard head frame (candidate L8–11; block B2): one `component:interwiki-style` include at priority=1 naming own `/1` on the draft host. The T4 lane had charged this theme with a missing translation frame (LOCALIZE-ROWS row 156, pattern 6); the frame stands in the current bytes, and ledger (c3) records P6 FIXED by the frame waves. The gate `[[iftags +テーマ]]` opens at candidate L13, below the frame and the head module, so delivery is not tag-gated — the same ungated-delivery topology as the original.
- Census: exactly one `[[code type="css"]]` block on each side (original L53–221; candidate L71–240), and both delivery addresses (candidate L5, L10) name `/1` — the block that holds the CSS. Self-delivery census: MATCH (class FIX-CODEADDR).
- No include-parameter gates are documented or defined on either side; nothing in the gate family arises.
- Verify: `grep -n 'local--code' candidate.txt` (`/1` twice); count `[[code` blocks (1).

## 4. Fonts and assets

- Head-module font loads (candidate L2–4; block B1): Noto Serif JP (L2), `Basic` + IBM Plex Mono wght 400;700 (L3), and Zilla Slab (L4), all Google Fonts css2. The Latin pair replicates the parent original's bunny.net import set (parent original L130–131: `family=Basic|IBM+Plex+Mono:400,700` and the Zilla Slab css2 line) converted to Google Fonts.
- Block B18 (JPFONT-STACK; original L198 → candidate L217): the page-title stack `'Copperplate Gothic', serif` gains `'Noto Serif JP'` — the pattern-7 supplement (class P7). Copperplate Gothic itself is named on both sides with no load: a system-font name, parity, not a gap.
- Minor defect flag (recorded for repair; this lane does not edit candidates): the L3–4 loads duplicate the parent candidate's own loads, and one family is applied nowhere. The hidden-included parent candidate (`pages/theme:scp-human-resources-sigma-jp.txt`) loads IBM Plex Mono (its L137) and Zilla Slab (its L138) from Google Fonts with specifications identical to candidate L3/L4, so in the delivered chain both families load twice — the duplicated-import minor class. And `Basic` occurs exactly once in the candidate (the L3 import) and in no stack in either file; the parent candidate dropped the family entirely (0 occurrences). `Basic` is therefore imported but applied by no stack or variable (the KB-16 mirror case). The pair's origin is visible (it replicates the parent original's import set), which explains it without excusing it.
- Assets: block B16 (ASSET-REHOST; original L78 → candidate L97): `--logo-image` is re-hosted from `scp-wiki.wdfiles.com` (`theme%3Avanguard-supplement/vanguard_transparent.png`) to SCP-JP storage (`scp-jp-storage.wdfiles.com`, `file%3A2963469-77-1a78/vanguard%20transparent.png`) — the same storage file the sibling vanguard-jp package's logo uses; class P5.
- The porter prose at candidate L31 announces only the Noto Serif JP page-title supplement, which matches candidate L217; it does not mention the L3–4 Latin loads — recorded with the flag above (section 10).
- Verify: `grep -n 'googleapis' candidate.txt` and the parent candidate; `grep -c 'Basic'` on both candidates (1 / 0).

## 5. Header, sidebar, site furniture

- Block B17 (labeled CSS-BODY heuristic; original L114 → candidate L133): the header mark's slogan `content:` string "SHELTER - NORMALIZE - INFORM" becomes 「保護 - 正常化 - 告知」. A prose slogan rendered for every reader, so it translates under the T5 boundary (names, brand marks and slogans functioning as marks stay as identity strings; this one is prose). The hyphen separators are kept where the sibling vanguard-jp used commas — a presentation difference between two ports of the same slogan, recorded. `content: "ANGUARD"` (candidate L128) is kept: the mark itself, its missing V being the logo's design.
- The theme carries no header or sidebar rules of its own beyond the variable overrides; the furniture comes from the parent.
- Verify: `grep -n 'content:' candidate.txt` against the original.

## 6. Text translation

- The body is translated throughout (TRANS-UNANCHORED 10 blocks, TRANSLATION-ANCHORED 1): the 使用方法 heading and prose, the usage examples' framing, the porter prose (candidate L31), and the slogan (section 5). The code banner and the CSS comments are the original's English, carried (the banner is the attribution carrier, section 1).
- The one residue block is a heading translation: B5 (original L17 → candidate L34, the centered 使用方法 heading), class P10, adjudicated in the appendix.
- Verify: the translation spans in `classification.json` against both files.

## 7. Links

- Block B6 (LINK-REPOINT; original L20 → candidate L37): the prose link to the parent theme is repointed `theme:scp-human-resources-sigma` → `theme:scp-human-resources-sigma-jp`. This lane's `--check-links` run warns `link-target-missing` for it: the JP candidate page is not yet posted on scp-jp — the posting-resolution class (the campaign candidate exists in this repository at `pages/theme:scp-human-resources-sigma-jp.txt`). Recorded verbatim; not a defect.
- The credit block's parent-theme attribution (candidate L23) links the EN parent on scp-wiki with its rev 13 reading note — the original-side source link, on the recorded origin host. No host defect stands for this theme.
- Verify: the `--check-links` output in section 12; `grep -n 'scp-human-resources' candidate.txt`.

## 8. Structure

- Topology unchanged: head module + one code block on both sides, no moves (classifier topology). The structural changes are the head frame addition (section 3), the credit block replacing the Rate region (section 1), and the license box at the tail (section 1).
- Exhibit census: the usage examples (self, parent, toggle-sidebar) all stand against the original; nothing was dropped or escaped away. The original carries no footnote specimens, so no footnoteblock question arises.
- CSS brace balance was checked by depth, not count: both files scan to final depth 0 with minimum depth 0.
- Verify: the topology record in `classification.json`; the depth scan in section 12.

## 9. Formatting only

- None as a class: WS-ONLY is 0 blocks. The candidate's line growth (225 → 261) is the frame, credit, license and font-load additions named in sections 1–4.

## 10. Porter annotations

- One comment-form annotation: candidate L73, the banner comment `/* ===== Vanguard Supplement（本テーマ） ===== */` added ahead of the original banner inside the code block (block B15, COMMENT-TEXT). It labels the block as the theme's own; its statement matches the bytes.
- One prose-carrier annotation: candidate L31, the font-program statement (Japanese page titles use Noto Serif JP, SIL OFL 1.1, loaded from Google Fonts). It announces the section-4 supplement and matches candidate L217; it does not announce the L3–4 Latin loads (section 4's flag).
- Verify: `grep -n '=====' candidate.txt`; read candidate L31.

## 11. Dispositions and exceptions

- Draft-host line (pseudo-ref ×1, the T1 baseline's error): candidate L5 (the `/1` import) — class (iii) draft form, rewritten at posting.
- Warning recorded verbatim: `link-target-missing` ×1 (candidate L37, the posting-resolution notice; section 7).
- Render row (RENDER-S2-D, EN23): the sample's hidden-rate (all combos) is the KB-09 family's render face, closed by item 38's fix; page-overflow 330–335px@320 and 884px@768 (KB-33 / KB-34 family) plus the runtime-hotlink site-theme chain (KB-40, environment layer) — DISPOSITIONED. The page's T2 returned no machine verdict (exit 2): a coverage caveat, not a finding.
- The STALE stamp's ground is section 0's status note: the post-verdict change is the usage sweep's lines (section 2), and no re-judgement is fabricated for it.
- The font flag (section 4) is a defect recorded for repair, not a disposition.
- No class (i) item stands for this theme.

## 12. Verification

- T1 run by this lane on the current candidate: plain run error 1 / warn 0 / info 1; with `--check-links`, error 1 / warn 1 / info 1 — FIX5-FURNA's after state (1/1/1, its run including link checks); the stamp baseline (1/2/2) describes the pre-FIX5 file. No `double-rate` finding in either mode.
- T2/T3: FINDINGS with dispositions only (ledger row (c2)).
- T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `4cbdf8d33a257ca37764871acd872b786403008f750a11373ee96449632d16af`); `original.txt` hash equals the sources.tsv value (`b311da0347c166373d515f3c00a70e72cafd19962466d2e89bb0f3d1260c1194`); brace-depth scans clean on both files; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 38 (ledger (b) row 156, class B): a duplicate bare `[[module rate]]` standing beside the rate-bearing preview credit — two rating widgets on one page (T1-ROWS row 171; LOCALIZE-ROWS row 156, pattern 3). The theme's (c3) line records P3 FIXED by the credit waves → (e), and P6 FIXED by the frame waves.
- History: LOCALIZE-S2-C checklist item 14 had left the Rate an unmade staff call under the exhibit-exception reading — a labelled paired exhibit may keep a demonstration Rate.
- What the fix was supposed to change: remove the duplicate block, leaving the preview credit as the page's only rating widget — if the exception did not cover the block.
- Supplement re-judgement: FIXED, FIX5-FURNA, commit 9e8931f. The FURNA lane report's evidence: the pre-edit candidate at L19–22 held `[[>]]` / `**評価:**` / `[[module rate]]` / `[[/>]]` immediately before `credit:start-preview` (L24); the single 評価 label is not the exempt paired-label exhibit, so the exception does not apply and the whole 4-line wrapper was removed; checker 1/1/2 → 1/1/1, the `double-rate` info cleared, no new errors.
- Re-derived from this package's bytes: the original carries the labelled Rate at original L11–14. The current candidate contains no `[[module rate]]` in any case (`grep -ci` = 0), and its credit block stands alone at candidate L19–29. This lane's checker runs report no `double-rate` line.
- Closure: CONFIRMED on current bytes — which matters here, because the verdict stamp is STALE (section 0): the closure is re-derived from the package, not inherited from the stamp.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-vanguard-supplement-jp.txt` — the render-check sample page for this theme.
2. `pages/theme:scp-human-resources-sigma-jp.txt` — the parent candidate the supplement includes hidden (section 2); its own package is `review/scp-human-resources-sigma-jp/`. Section 4's font flag spans this file.
3. The candidate's own delivered file: the storage-hosted logo (section 4).

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-C) produced the port: P3 credit fields fixed by the credit waves, P6 by the frame waves (the head frame), the font supplement applied; the bare Rate survived that wave as the unmade staff call.
- FIX5-FURNA (commit 9e8931f) removed the Rate wrapper and closed item 38.
- The usage-example sweep (commit b5cb724) then completed the usage lines' `:scp-jp:` names — the post-verdict change behind the STALE stamp.

## Appendix — heuristic and residue adjudication

The classifier reports 1 residue block and 8 heuristic blocks. All resolve by shape:

- Residue B5: the centered 使用方法 heading translation (class P10) — section 6. A classifier artefact, not a content question.
- Heuristic B6 (LINK-REPOINT): the parent prose link repoint — section 7.
- Heuristic B7, B9, B11, B12, B13 (TRANS-UNANCHORED): body prose translations — section 6.
- Heuristic B10 (EXHIBIT-RESTRUCTURE primary): a mere include repoint inside the toggle-sidebar usage exhibit — section 2. False fire.
- Heuristic B15 (COMMENT-TEXT): the added porter banner comment — section 10.
- Heuristic B17 (CSS-BODY): the slogan `content:` translation — section 5 (rendered strings are narrated as their own class even when the classifier labels them CSS-BODY).

No heuristic or residue block is left unadjudicated. One defect flag arises from this package (section 4's duplicated and unapplied font imports, minor); the candidate is not edited by this lane.
