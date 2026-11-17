# Review package — theme:oneiroi-west-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:oneiroi-west-jp — origin CN, population #210 [GOSIGN2-LEDGER (b) row 210]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 738012018874dac50f3c6c11404574253e39c63bce2ee2c9a6bddf5701cd0326); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 2 warns / 1 info (hotlink×6); standing classes dispositioned in register c1 [T1-ROWS row 225; GOSIGN2-LEDGER (b) row 210]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow + candidate-side hosts kaktuskontainer.wdfiles.com, scpsandboxcn.wdfiles.com. [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 209, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 209]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 210]
- Computed against: canonical commit 1db8300464d032875c6f8cc6ab61a5cafc6b7433; candidate file pages/theme:oneiroi-west-jp.txt sha256:738012018874dac50f3c6c11404574253e39c63bce2ee2c9a6bddf5701cd0326; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 210) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×6 (the three sandbox-hosted images, in both CSS copies; class (ii) / KB-58, section 11); T4's one display-affecting finding (P5, the same three images) DISPOSITIONED at GOSIGN2-LEDGER §(c3) (class (ii) / KB-58); the render row's items (site-theme chain, credit-modal preview form, overflow, candidate-side hosts, section 11). **FLAGGED by this package** — the holder field's silence on the underlying work's author (per-theme record, item 1), one inherited credit rule in the pre-correction selector form (item 2), and the two-copy delivery state (item 3) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:oneiroi-west | theme:oneiroi-west-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (first translation; the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-oneiroi-west.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:oneiroi-west-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 429 lines / 10,580 bytes | 713 lines / 18,409 bytes |
| SHA-256 | 82eb3672076f55dc28ded7aeecbfadfbfc32326bead664cfec5df5890419c029 | 6d43fcab7217c5833af4ffe020f7efd372a599e6597487d4fc6aceb5fe12b3ea |

Wave history: the candidate was created by the Stage 2 CN10 integration (commit a89eccf, the LOCALIZE-S2-E wave's port) and has two later commits: f1138e4 (FIX-P4, the pattern-4 repoint of base-theme CSS imports to JP port candidates, 39 files) and a497307 (FIX4-MECH, duplicate @import removal across 29 themes, KB-65; the verdict stamp's computed-against commit). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A CN Oneiroi theme whose port restructures delivery. The original delivers its CSS by importing its own `[[code]]` exhibit from the CN wdfiles host, and styles its sidebar through a hidden styleFrame iframe pointed at a CN wiki file. The candidate keeps the exhibit as the framed delivery (an interwiki-style frame at priority 3 naming the exhibit on the production host) and additionally inlines the same CSS into a head `[[module css]]`, so the theme page renders in the draft composition where the production-host code address does not yet resolve; the two copies are 99.1% identical, and the module copy alone carries the JP font loads. The styleFrame embed is deleted, the CN credit furniture is swapped for the JP preview block, the CJK font stacks convert from the SC/TC faces to the JP faces, and the body is translated in place. Three key images stay hotlinked from CN-sandbox and third-party wdfiles hosts in both copies: that is T4's one display-affecting finding, dispositioned class (ii) / KB-58 in the ledger. Measured churn (diff.md, the generator's difflib count with autojunk off: +441/−157, 598 changed lines in 22 change blocks / 10 diff sections) is dominated by the relocation: most blocks are single lines inside the one moved body.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 22 change blocks — 22 specific (100%), 0 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 12 |
| WS-ONLY | 8 |
| CONTENT-STRING | 6 |
| TRANSLATION-ANCHORED | 5 |
| GLYPH-FORM | 2 |
| IFTAGS | 2 |
| EXHIBIT-RESTRUCTURE | 1 |
| ASSET-REHOST | 1 |
| DELIVERY-HOST | 1 |
| SELF-DELIVERY | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| JPFONT-LOAD | 1 |
| FONTLOAD-CJK-STACK | 1 |
| CREDIT-PREVIEW | 1 |
| RESTORATION | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE count of 12 is one relocation measured twelve times — B3–B21 are single lines or pairs inside the moved body (the topology pass measures the move itself once, code-css → module-css at 0.949 similarity), and their second labels (JPFONT-LOAD, CONTENT-STRING, GLYPH-FORM, FONTLOAD-CJK-STACK) are the real changes, adjudicated in sections 4 and 6. B2's EXHIBIT-RESTRUCTURE primary is the body block displaced by the module insertion (the exhibit census in section 8 shows every exhibit carried), and its RATE-EXHIBIT-KEPT-CANDIDATE label is wrong for this theme: the candidate contains no `[[module Rate]]`; the original's labeled bare Rate (original L12–15) was deleted under P3 (section 1). B22's RESTORATION label sits on the tail block that reassembles the gate, credit block, and exhibit after the move; nothing in it restores previously deleted content, and its T7-CREDIT-CSS spans name only the exhibit copy of the credit rules, which exist in both copies (section 1). The skeleton's "none" readings for the include and annotation sections are adjudicated in sections 2 and 10. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:oneiroi-west-jp; original theme:oneiroi-west on scp-wiki-cn at reference revision 10; candidate `pages/theme:oneiroi-west-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved: the original opens with its delivery module, the hidden styleFrame embed, and then its gate (original L1–11); the candidate opens with the interwiki-style frame and the inline CSS module, both ahead of the localized gate (candidate L1–297).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frame is P6/T3, the embed's deletion is recorded in section 8.
- **Verify:** The sources.tsv row for oneiroi-west-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labeled exhibit pair: a centered bare `[[module Rate]]` under its caption (original L12–15), and the CN credit module pair `:scp-wiki-cn:credit:start`/`end` under a second caption (original L17–23), its body the placeholder 页面信息. The candidate deletes both exhibits and their captions and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block directly under the gate (candidate L299–309) carrying the eight ruling-3 fields (title 西部夢神テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 西部梦神 主题版式, the original's simplified-Chinese title kept as the original-title field; 著作権者 Mercuresphere; 作成年 2022; 初訳時参照リビジョン 10; the source link, candidate L308, on scp-wiki-cn.wikidot.com, the host sources.tsv records for the original). Author check against the original: Mercuresphere is the theme's author (the original's about prose, original L26, and the exhibit banner, original L142); the banner and prose also credit the underlying work to Feitag and Sigma 9 to Aelanna and Dr Devan — the field names the author of record alone, and the Feitag credit is flagged in the per-theme record, item 1. The translator field took its ruling-3 form in the CN10 integration itself. No license box exists on either side. T7 credit-module CSS: the theme carries its own credit-rule group inherited from the original's exhibit (the `/* rate-box */` group, original L231–277 zone), present in both candidate copies (module, candidate L99–145 zone; exhibit, candidate L516–562 zone) and byte-identical in substance; one selector in it is flagged in the per-theme record, item 2. No supplement was added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate and the branch credit pair are deleted rather than duplicated (a kept Rate would be the KB-09 duplicate; a kept branch credit module does not render in the JP environment). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns only the preview pair at L299 and L309; read candidate L299–309 against the eight fields.
- **Disposition:** Applied; the ledger §(c3) line for this theme dispositions its T4 P5 item only (section 11), and no credit item is charged.

### 2. Includes and components

- **What:** The candidate's live includes are three: the interwiki-style frame (candidate L1–4, section 3) and the credit pair (section 1). The original's only live includes were its CN credit pair, deleted in the swap. The usage example's escaped include changes form: the original's `@@[[include :scp-wiki-cn:theme:oneiroi-west]]@@` (original L33) becomes the bare `@@[[include theme:oneiroi-west-jp]]@@` (candidate L317), naming the candidate's own fullname without a site prefix — the correct page under either reading, in contrast to the plain-slug shape flagged in sibling packages. The title-customization example (a `[[module CSS]]` snippet setting the header `content:` strings) is carried in translation (candidate L320–330). No component include exists on either side, so no P1 repoint and no ruling-4 port arises.
- **Why:** P1 is satisfied by the self-reference naming the page that will exist; the frame and credit includes are sections 3 and 1.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three live includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS by importing its code exhibit from the CN wdfiles host: a head `[[module CSS]]` with `@import url(https://scp-wiki-cn.wdfiles.com/local--code/theme%3Aoneiroi-west/1)` (original L1–3), the exhibit being the `[[code type="css"]]` block at original L139–428. The candidate delivers the same body two ways at once. (a) The framed delivery survives in posting form: an interwiki-style include at the head (candidate L1–4) with `priority=3` and `theme=` naming the exhibit as `local--code/theme%3Aoneiroi-west-jp/1` on the production host scp-jp.wdfiles.com; priority 3 is the own-layer value, and there are no priority 1/2 entries because the theme has no base. (b) The same CSS is inlined into a head `[[module css]]` (candidate L5–296), which is what renders the theme page itself in the draft composition, where the production-host code address does not yet resolve. The two copies were compared directly for this package: 291 module lines against 286 exhibit lines, similarity 0.9913, and the only differences are the module wrapper and the two JP font `@import` lines, which the module copy alone carries (candidate L16–17; per-theme record, item 3). The exhibit copy keeps the original's `[[code type="css"]]` form (candidate L425–712) and is the frame's target body. B1 is the head change itself: the original's import line gives way to the frame.
- **Why:** P4/T9 (own-code delivery served from JP hosts: the CN wdfiles address becomes the JP production address) and P6/T3 (the interwiki-style frame). The production-host form of the frame URL is class (ii) mechanics, already in its posting form; the inline module is the draft-stage rendering device, recorded here rather than hidden.
- **Verify:** `grep -n 'local--code\|module css' candidate.txt` — the frame at L1–4 and the module at L5; compare original L1–3.
- **Disposition:** DISPOSITIONED (the frame's production-host form, class (ii)); the two-copy state is flagged as a note in the per-theme record, item 3.

### 4. Fonts and assets

- **What:** Loads: the original's exhibit loads one CJK font CSS from a jsdelivr GitHub mirror (original L150: Crimone/wanderers-dustjacket-fonts' noto-fonts.css, serving the Noto SC/TC faces). The candidate's module copy loads the two JP faces from Google Fonts (candidate L16–17: Noto Serif JP 400;700;900 and Noto Sans JP 400;700;900); the exhibit copy carries no font load (section 3's asymmetry). Stacks (the FONTLOAD-CJK-STACK block B9 and the serif pair): `'Noto Serif SC','Noto Serif TC', serif` → `'Noto Serif JP', serif` (candidate L30, exhibit twin L447) and `'Noto Sans SC','Noto Sans TC'` → `'Noto Sans JP'` (candidate L49, exhibit twin L466). Load-gap check: the first-named faces (Noto Serif JP, Noto Sans JP) are loaded by the module copy on the same page, so a page that includes this theme page receives the loads with the stacks; there is no KB-16 gap in the include path. Assets: three key images stay on outside hosts, in both copies — the header art `go.png` (candidate L21 and L438, scpsandboxcn.wdfiles.com; the original's line was plain `http`, upgraded to `https` in the port), the page background `body_bg.png` (candidate L70 and L487, kaktuskontainer.wdfiles.com), and the dropdown arrow `expand.png` (candidate L220 and L637, scpsandboxcn.wikidot.com). These three are T1's six hotlink errors (three URLs × two copies) and T4's one display-affecting finding ("P5 MISSED: all three key images hotlinked from CN-sandbox / third-party wdfiles", LOCALIZE-ROWS row 209), dispositioned in the ledger at §(c3) as class (ii) / KB-58: re-hosting is a posting-procedure act, not a candidate edit. The styleFrame iframe's target file is an asset of the same family; its mechanism is deleted instead (section 8).
- **Why:** P7 (the JP faces replace the CN faces in load and stack together; the jsdelivr mirror of a third-party font repo gives way to the allowed Google Fonts host, KB-17). P5 is the class T4 charged; its disposition is the ledger's, recorded here with its grounds.
- **Verify:** `grep -n '@import' candidate.txt` — the frame's exhibit carries none, the module carries the two JP loads at L16–17; `grep -n 'kaktuskontainer\|scpsandboxcn' candidate.txt` returns the six asset lines above.
- **Disposition:** Loads and stacks applied; the three images DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The sidebar half of this section is the styleFrame embed, deleted and recorded in section 8. For the header: the theme sets no `--header-title` or `--logo-image` override on either side; the header and subtitle are user-customized through the documented `content:` example, which the candidate carries in translation (candidate L320–330), and the header art is section 4's `go.png`. No P8 layout adaptation fired beyond the embed's removal.
- **Why:** P9/T6 do not apply to a theme that sets no header variables; the embed is a P8-adjacent sidebar mechanism whose JP treatment is deletion, argued in section 8.
- **Verify:** `grep -n -- '--header-title\|--logo-image' candidate.txt` returns nothing; read candidate L320–330 against original L36–46.
- **Disposition:** Standing; the embed deletion is dispositioned in section 8.

### 6. Text translation

- **What:** The body is translated throughout: the about prose (candidate L313–318, including the Feitag credit line, section 7), the usage prose, and the syntax exhibits in the same order as the original's (headings, tabs, collapsibles, blockquote and comment samples). The classifier's translation mass rides inside the relocation blocks; counted by label, TRANSLATION-ANCHORED fires on 5 blocks and TRANS-UNANCHORED on 1, which understates the body because the matcher anchors the moved CSS first. Reader-visible CSS strings (the CONTENT-STRING blocks B7, B11, B19–B21 and the tail spans in B22): the lock-info `::before` text is translated from Chinese to Japanese (original L394–395 zone → candidate L262–263), as are the remaining UI strings in the body of the CSS. R5 glyph-form conversion, stated separately: retained Chinese strings in the CSS take Japanese glyph forms where the string survives (the GLYPH-FORM spans of B7 and B11), distinct from full translation. In-CSS text (R1): the exhibit's banner comment (the authorship banner, original L140–148) is carried verbatim in English in both candidate copies, porter-visible only. Chinese survives in the candidate on exactly one line, the credit block's original-title field (candidate L304), where it is a quotation.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings, including the lock-info UI text). R5 is separated per the taxonomy so a reviewer can tell a converted string from a translated one.
- **Verify:** The body sections of diff.md in order; a Chinese-prose scan of candidate.txt outside the credit field returns nothing.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the one quotation.

### 7. Links

- **What:** One prose-link change, in the about prose: the original links Feitag's underlying work with an empty-label intra-wiki link (`[[[oneiroi-food-guide-ambrose-dreams-teashop| ]]]`, original L26); the candidate converts it to a labeled external-form link to the same work on its home wiki, with the work's title and a （中国語版） note (candidate L314). The target stays on scp-wiki-cn because the work has no JP counterpart page; the link is the attribution record for the theme's basis. The credit source link (candidate L308) names scp-wiki-cn.wikidot.com, the recorded host, and serves the original. No other outbound links exist in the candidate outside the asset URLs of section 4.
- **Why:** P11: a prose link takes the JP counterpart where one exists and the serving original where it does not; the dead-reference standard is not engaged, nothing here is dead.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the Feitag link and the source link.
- **Disposition:** Standing.

### 8. Structure

- **What:** Two declared deviations from the localize.md closing rule, both named here rather than hidden. (a) The delivery restructure of section 3: the CSS body exists twice in the candidate (inline module and framed exhibit) where the original carries it once (the exhibit, imported by the head module). (b) The styleFrame embed is deleted (original L5–9): a hidden `[[div_]]` wrapping an iframe that pulls `nav:side/styleFrame.html` from the CN wiki's file storage with sidebar CSS encoded in its query string. The mechanism has no JP counterpart — the JP sidebar is the environment's own furniture, and the embed's payload targeted the CN sidebar DOM (`.side-block` rules) — so the port deletes it outright; KB-43 records the styleFrame shape at the environment layer. Everything else holds: variable names, selectors, and rule order inside the CSS are preserved (topology similarity 0.949 for the move, the differences being sections 3 and 4), and the exhibit census (heading samples, tabview, collapsibles, blockquote samples, the code exhibit) corresponds one to one in the same order, so no R3 deletion arises. B2's EXHIBIT-RESTRUCTURE primary is the body block displaced by the module insertion, adjudicated by this census.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census and by naming the two deviations, not by the label.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[collapsible\|\[\[embed' original.txt candidate.txt` — the embed is the only exhibit-form line with no counterpart.
- **Disposition:** Standing with the two deviations declared; no class I item (the embed's deletion is dispositioned here, and the render row charges nothing for it).

### 9. Formatting only

- **What:** Eight WS-ONLY blocks (B6, B8, B10, B13–B17), each a single whitespace-only line pair inside the moved CSS body (blank-line and spacing differences between the original's exhibit text and the candidate's copies). The classifier finds 0 re-indentation blocks, so there is no wholesale R7 re-indent; the eight lines are disclosed so they are not mistaken for semantic change.
- **Why:** Formatting churn is disclosed as its own class; the follow-up-diff hazard is limited to these eight lines.
- **Verify:** The WS-ONLY entries in classification.json, at original L166–301 against candidate L34–169.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, not assumed: the candidate adds no comment-form annotation (no `[!-- --]` note and no added CSS comment; the banner comment in both copies is the original's own, original L140–148, and the `/* header */` comments are the original's). The port's one explanatory addition is structural, not textual: the inline module of section 3 carries no comment explaining itself, which is part of why item 3 of the per-theme record exists.
- **Why:** R2 requires the check to be explicit, because annotations ride inside other labeled blocks in sibling packages; here the grep is the evidence.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; compare the CSS comments on both sides of diff.md.
- **Disposition:** None — checked, absent.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's six hotlink errors and T4's P5 finding: the three sandbox/third-party images of section 4, DISPOSITIONED at GOSIGN2-LEDGER §(c3) as class (ii) / KB-58 (deferred asset re-hosting at posting). (2) The render row's items (RENDER-ROWS-2, lane RENDER-S2-F (CN10)), none charged to the candidate at the ledger determination: the page's runtime-hotlink site-theme chain (KB-40, environment layer); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); the sample's 884px@768 overflow, recorded verbatim; and the candidate-side hosts item, which is item (1)'s hosts seen from the render side. (3) The styleFrame embed's deletion, dispositioned in section 8 (no JP counterpart mechanism; KB-43's shape). (4) The three per-theme flags (the holder field's silence on Feitag; the inherited `.creditButton p a` selector; the two-copy delivery note) are flagged, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 225): exit 1, 6 errors / 2 warns / 1 info; all six errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-F (CN10)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 209, LOCALIZE-S2-E): FINDINGS / FINDINGS jointly, display-affecting findings 1 (the P5 image item), dispositioned at §(c3). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +441/−157 in 22 change blocks / 10 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:oneiroi-west-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 210; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the holder field and Feitag (flagged) Adjudicated after this package was built (FIX-CREDITBTN item 2, commit 1db8300): Feitag stands in both banners and the prose; attribution stands, no edit. See the post-package repairs item below.

The original credits Feitag in two places: its about prose ("由 [[*user Mercuresphere]] 基于 [[*user Feitag]] 的 [[[oneiroi-food-guide-ambrose-dreams-teashop| ]]] 制作", original L26 — made by Mercuresphere, based on Feitag's page) and its exhibit banner ("Based on "Oneiroi Food Guide: Ambrose Dreams Teashop" by Feitag", original L144). The candidate's credit block names Mercuresphere alone in the 著作権者 field (candidate L304). Feitag's credit survives in the candidate's translated prose (candidate L314, with the link to the CN page) and in the carried banner (both copies). The distinction from the sibling flags in this campaign is real — Feitag authored the underlying work this theme is based on, not this theme, and the prose credit is a reader-visible place, not only a comment — but the shape is the family the U-1 and U-2 batches repaired (a contributor the original names in its credit furniture, absent from the TASL field). This package flags the gap with both sides' text and does not edit the candidate; the ledger's determination for this theme is PASS and its T4 row charges only the P5 image item.

### Item 2 — the inherited `.creditButton p a` selector (flagged) Repaired after this package was built (FIX-CREDITBTN item 1, commit 1db8300): both copies now read `.creditButton > a`; see the post-package repairs item below.

The theme's own credit-rule group is carried in both candidate copies (module, candidate L138; exhibit, candidate L555), including `#page-content .creditButton p a`, byte-identical to the original's exhibit (original L270). The campaign's T7 record (SUPPLEMENT-TYPES T7; KB-11) states the JP credit module emits the anchor as a direct child of `.creditButton`, without the `<p>` wrapper this selector requires, and sibling ports corrected exactly this shape (theme:sodium-jp in place, theme:jiha-jp by restatement). Here the rule stands uncorrected in both copies, so on the JP DOM it cannot match. The same flag is recorded for theme:mr-reprisal-jp in this batch; the pair suggests the in-place correction was applied only where a wave happened to touch the file. This package flags the selector with its evidence and does not edit the candidate; the theme's T4 row does not charge it.

### Item 3 — the two-copy delivery state (note)

Section 3 records the fact; this item records the risk a reviewer should weigh. The candidate carries its CSS twice in one file, and the copies are not byte-identical: the module copy alone loads the JP fonts (candidate L16–17), so the framed delivery (the exhibit copy, the form a posting user actually applies) depends on the module copy's loads arriving on the same page. They do, in the include path, because including the theme page brings its module with it. But any future edit made to one copy and not the other will silently split the theme's appearance between the theme page and the pages that apply it, and the diff record will not show it, because this package's diff compares the original against the candidate as wholes. The original's single-copy form did not have this failure mode. Recorded as a note, not a defect: the framed delivery the original used survives in posting form, and the module copy is the draft composition's rendering device.

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-CREDITBTN item 1 — KB-11 selector correction (landing 1db8300).** Commit 1db8300 retargeted both copies of the inherited selector: the module copy (candidate L138) and the exhibit copy (L555), `#page-content .creditButton p a {` → `#page-content .creditButton > a {`, declarations byte-untouched. T1 before/after identical (6/2/1).

**FIX-CREDITBTN item 2 — base-work contributor adjudication (no edits).** `FIX-CREDITBTN.md` item 2 adjudicates Feitag as STANDING. The loci are the banner in both CSS copies (candidate L10–11 and L429–430: `Edited by Mercuresphere` / `Based on "Oneiroi Food Guide: Ambrose Dreams Teashop" by Feitag`) and the translated prose (candidate L313, `[[*user Mercuresphere]] が [[*user Feitag]] による『夢神の食事ガイド…』…をもとに制作したものです`), against the 著作権者 field (L305) naming Mercuresphere. Feitag authored the base work, not this theme; attribution stands, no edit.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-oneiroi-west-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
