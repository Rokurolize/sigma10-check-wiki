# Review package — theme:shoebill-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:shoebill-jp — origin EN, population #137 [GOSIGN2-LEDGER (b) row 137]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2c2cb8293d9bfd56559d3ffe3546fd5bbc937a7b7c728fbef79333b9529b2a5a); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 3 warns / 2 infos (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 122; GOSIGN2-LEDGER (b) row 137]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-D (EN19))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN19))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 137, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 137]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 137]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:shoebill-jp.txt sha256:2c2cb8293d9bfd56559d3ffe3546fd5bbc937a7b7c728fbef79333b9529b2a5a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 137) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (class (ii), section 11); the render row's two items (KB-40 / KB-32, section 11); the four draft-host image files (KB-58, section 11). **FLAGGED by this package** — the kept bare Rate beside the rate-bearing credit block, the usage example's plain-slug self-reference, and the prose Sigma Plus link (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:shoebill | theme:shoebill-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16 (first translation; the candidate's credit block records 初訳時参照リビジョン: 16) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-shoebill.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:shoebill-jp.txt`, copied at worktree HEAD 8d2d71c |
| Lines / bytes | 700 lines / 19,074 bytes | 712 lines / 20,547 bytes |
| SHA-256 | f1061cfe02e21b548873ed8d299ca05df515f0dc1f59dd6142f6a83944e18736 | dbe3c27ad0d8f7ef153a285cdc951916b0c88524f679224b8cdda593e66a3953 |

Wave history: the candidate was created by the Stage 2 EN19 integration (commit 765e2f8, the LOCALIZE-S2-C wave's port) and has exactly two later commits: 666f543 (FIX2-CREDIT, completing the credit fields T4 had found missing) and 1cdad38 (FIX4-SIGMA, unifying the sigma-plus include form to component:sigma-plus-jp). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Sigma Plus theme whose port is the standard standing classes, applied once each, plus a component swap with real content: the candidate installs the JP preview credit block with the eight ruling-3 fields, repoints the closing furniture (the license box to its JP backend form, toggle-sidebar and betterfootnotes to their `:scp-jp:` pages, and the base component to its ruling-4 JP port `component:sigma-plus-jp`), moves the three display fonts from fonts.bunny.net to Google Fonts and adds Noto Sans JP to the load and to all three font stacks, repoints its own delivery and its four image files to the draft host, and translates the body, the header subtitle, and the license entries. Measured churn (diff.md, the generator's difflib count with autojunk off: +145/−133 in 50 change blocks / 19 hunks; a GNU-diff count of the same pair gives 268 changed lines — the difference is alignment choice, not content). Three byte-level items deserve a reviewer's eye rather than a skim, all flagged in the per-theme record: the original's bare Rate module is kept beside the rate-bearing credit block, the usage example's self-include kept the plain slug, and the prose Sigma Plus link names a page scp-jp does not have.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 50 change blocks — 33 specific (66.0%), 16 heuristic (32.0%), 1 residue (2.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 8 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 6 |
| EXHIBIT-RESTRUCTURE | 5 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 4 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 15 |
| TRANSLATION-ANCHORED | 8 |
| WS-ONLY | 14 |

Adjudication for this README (every block was read against the bytes): the 1 residue block (B32) is a one-line CSS comment translation, counted in section 6 with the 8 COMMENT-TEXT blocks; the 2 CSS-BODY blocks adjudicate to a P7 font-stack rewrite (B14, section 4) and an in-place JP-DOM selector correction (B31, section 5); the 5 EXHIBIT-RESTRUCTURE primaries are include repoints and license-box lines (sections 2 and 8), not exhibit changes; of the 15 TRANS-UNANCHORED-labeled blocks, 3 are prose translations, 8 are the CSS comment translations (dual-labeled COMMENT-TEXT), 3 are license-entry translations, and 1 rides inside the credit block (B1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:shoebill-jp; original theme:shoebill on scp-wiki at reference revision 16; candidate `pages/theme:shoebill-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-C wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself did not move: the original opens with its tag gate `[[iftags +theme]]` (original L1) and delivers from the tail; the candidate opens with the localized gate `[[iftags +テーマ]]` (candidate L1) ahead of the credit block and keeps the tail delivery. Delivery topology is identical on both sides (one code-css exhibit, one tail module-css; no relocation detected).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization), the tail delivery is P4/P6 (section 3).
- **Verify:** The sources.tsv row for shoebill-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is recorded here and the delivery in section 3.

### 1. Credit and attribution

- **What:** The original has no head credit furniture at all: no info block and no credit block; its only rating furniture is a bare `[[module rate]]` inside a `[[>]]` div (original L3–5), and its attribution lives in the prose (created by Fish^12, original L9) and in the tail license box for the icon images. The candidate installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L3–12, block B1) carrying the eight ruling-3 fields (title Shoebill Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Shoebill Theme; 著作権者 [[*user Fish^12]]; 作成年 2026 — the original's own code banner dates the work "[2026 Wikidot Theme]"; 初訳時参照リビジョン 16; the source link https://scp-wiki.wikidot.com/theme:shoebill, whose host is the host sources.tsv records for the original, so no probe was needed). The fields were not complete at creation: T4 found six of the eight missing, and FIX2-CREDIT (commit 666f543) completed them. The bare Rate is **kept** (candidate L14–16) — that is the flagged item of the per-theme record, not a silent pass. The license box (T4): the original's `:scp-wiki:component:license-box-theme` (original L667) becomes `:scp-jp:component:license-box-backend` with `|author=Fish^12` (candidate L679, block B42's LICENSE-BOX span), the three game-icons entries are translated in place (blocks B43–B45: Name → 名称, License → ライセンス, Source Link → 出典リンク; author names and CC terms kept as proper nouns), and the end include is repointed (candidate L699, B46). T7 credit-module CSS: none added — the `.rate-box-with-credit-button` rules in the code exhibit (candidate L528, L536) are the original's own Sigma Plus styling, carried unchanged; no `.creditRate`/`.creditButton` supplement was needed and none was added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form and carries the eight ruling-3 fields; ruling 3 fixes the fields and the translator credit form. T4 (JP license box): the JP backend form is what renders the entries in this environment. The kept Rate is the KB-09 question, argued in the per-theme record.
- **Verify:** Read candidate L3–12 against the eight fields; `grep -n 'module rate' candidate.txt` returns exactly candidate L15; `grep -n 'license-box' candidate.txt` returns L679 and L699.
- **Disposition:** Credit fields FIXED (FIX2-CREDIT; the ledger §(c3) line for this theme records the P1 disposition, and the field completion is the FIX2-CREDIT wave's, checker-verified). The license box stands as the T4 supplement. The kept Rate is flagged, not dispositioned (per-theme record, item 1).

### 2. Includes and components

- **What:** Four INCLUDE-REPOINT blocks and one component swap. B6: the usage example's self-include, `:scp-wiki:theme:shoebill` → `:scp-jp:theme:shoebill` (original L16 → candidate L27) — repointed in site prefix only; the plain slug it keeps is flagged in the per-theme record (item 2). B7's include span: the image-block exhibit, `:scp-jp:component:image-block` with its `name=` repointed to the draft-host asset URL (original L23 → candidate L34; the asset itself is section 4). B46/B49: the license-box end and the interwiki-style include lines at the tail (sections 1 and 3). B47 (COMPONENT-SWAP + SIGMA-PLUS-JP): the closing component trio — `:scp-wiki:component:sigma-plus` → `[[include component:sigma-plus-jp]]` (original L690 → candidate L702; the bare same-site form naming the JP port, unified by FIX4-SIGMA, commit 1cdad38), and toggle-sidebar / betterfootnotes repointed to their `:scp-jp:` pages under their plain names (candidate L703–704), which are the names those JP components actually carry. The credit includes (section 1) complete the candidate's include list; every include names a `:scp-jp:` target or the same-site JP port. The prose component links (candidate L22) are section 7.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. T8 / ruling 4: sigma-plus was ported alongside the themes that need it (component:sigma-plus-jp exists in `pages/`), so the base include names the port rather than the EN page that 404s here — this is the repair of T4's pattern-1 charge.
- **Verify:** `grep -n '\[\[include' candidate.txt` — nine includes; `ls pages/component:sigma-plus-jp.txt` confirms the swap target exists.
- **Disposition:** Applied; no foreign include kept, no named exception needed. The usage example's slug is flagged (per-theme record, item 2).

### 3. Delivery and code loading

- **What:** The original delivers its own CSS from the tail: a `[[module css]]` importing `local--code/theme:shoebill/1` from scp-wiki.wdfiles.com (original L695) and an interwiki-style include at priority 1 with `theme=` naming the same delivery (original L697–699). The candidate keeps that exact apparatus with both addresses moved to the draft host (candidate L707 and L711; blocks B48 and B50, SELF-DELIVERY + DELIVERY-HOST + DRAFT-HOST). No head frame was added and none was needed: the original already carried the frame, at priority 1, the theme's own layer only — the Sigma Plus base arrives by include (section 2), not by frame layering, so there is no priority stack to narrate. The in-CSS self-references take the same draft-host form: the header-logo variable (B15's DRAFT-HOST span, candidate L90), the two body background URLs (B25, candidate L300–301), and the hummingbird background (B36, candidate L539).
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame the original already had, repointed). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L707 and L711, both draft-host; compare original L695–699.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Font delivery (block B13, FONT-IMPORT + JPFONT-LOAD): the original loads three families from fonts.bunny.net (original L55–57: Stick No Bills 200–800, Taprom, Roboto Flex). The candidate loads the same three families from Google Fonts and adds a fourth, Noto Sans JP (400;700) (candidate L66–69). Stacks (block B14, adjudicated here from its CSS-BODY label): all three font variables gain the JP face — `--stic`, `--tapr`, `--robo` each become `"<family>", "Noto Sans JP", sans-serif` (candidate L80–82). Every family named in a stack is loaded, so there is no KB-16 gap and no retired-family residue. Assets (P5): the theme's four image files move from `scp-wiki.wikidot.com/local--files/theme:shoebill/` to the draft host's `theme%3Ashoebill-jp` folder with filenames unchanged — the image-block `name=` (candidate L34), `--sp_header-logo` 225.webp (candidate L90), the stork/fish backgrounds (candidate L300–301), and the hummingbird background (candidate L539). All four return 404 on the draft host today (probed for this package, 2026-11-17); the originals serve on scp-wiki. That is the deferred-hosting state of section 11, not a candidate-side host error: the URLs name the right folder and files.
- **Why:** P7/T5 with KB-16 (the font load gap): the Latin display faces cannot render Japanese text, so the JP face joins the load and every stack that can receive Japanese text; the delivery host changes because fonts.bunny.net is outside the environment's hotlink set while Google Fonts is inside it (P5/KB-17). P5 for the assets: the theme's own images are re-hosted to the JP side; the upload itself is a posting-time act.
- **Verify:** `grep -n '@import' candidate.txt` — four Google Fonts lines at L66–69 and the delivery import at L707; `grep -n 'local--files' candidate.txt` against the four asset lines above.
- **Disposition:** Font load, host swap, and stacks applied. The four asset files are DISPOSITIONED (class (ii) / KB-58, section 11).

### 5. Header, sidebar, and site furniture

- **What:** Two variable-level items and one selector correction. B15's HEADERVAR span: `--header-subtitle` is translated in place (original L77, "Protecting The Small" → candidate L89, 「小さきものを保護する」) on the same lines as the logo variable's host repoint (section 4). `--header-title` keeps the original's value "SITE-225" (candidate L88) — the ported site's proper name, carried as a name rather than translated as prose. B31 (adjudicated here from its CSS-BODY label): the interwiki/sidebar menu-icon rule gains the JP markup's element form — `#interwiki .menu-item img, #side-bar .menu-item img` becomes the same selectors plus `#interwiki .menu-item > .image, #side-bar .menu-item > .image` (candidate L391) — an in-place correction (R6 shape) because the JP interwiki and sidebar components emit `.image` elements beside `img`. No other P8 layout adaptation was needed: the theme's sidebar and topbar rules are carried unmodified apart from the font variables of section 4.
- **Why:** P9/T6 for the variables; the subtitle is reader-visible header text, so its translation is P10/KB-18 carried in a string variable. KB-57 and ruling 2 are not engaged: the subtitle was translated, and the title is a proper name, not header prose in the original's language.
- **Verify:** `grep -n -- '--header-' candidate.txt` — two lines (L88–89); read candidate L391 against original L379.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body is translated throughout, in counted groups. Eight TRANSLATION-ANCHORED blocks (B2, B8–B12 and the anchored spans of B7/B15): the heading sample (B2: "+ SANTA CLAUS HAS A FAT ASS." → 「+ サンタクロースは尻がでかい。」, candidate L18), the table sample's headers and cells (B9–B10), the tab titles (B11: "Click Me" → 「クリックしてください」), and the font sample spans (B12). Three TRANS-UNANCHORED prose blocks (B3–B5), each a one-paragraph translation verified line by line against the mirror: the theme's self-description (B3), the component paragraph (B4, whose links are section 7), and the usage lead-in (B5). The license entries are counted in section 1 (B43–B45). In-CSS text (R1): the 8 COMMENT-TEXT blocks (B16, B19, B21, B23, B28, B30, B33, B37) plus the residue block B32 are one-line CSS comment translations (e.g. `/* Header. */` → `/* ヘッダー。 */`, candidate L287) — porter-visible only, stated here separately from reader-visible text as the taxonomy requires. The code exhibit's banner (Shoebill Theme / [2026 Wikidot Theme] / by Fish^12) is kept in English: it is the work's own title block, not prose. R5 glyph-form conversion: none — the source is English, and no retained string changes glyph form.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). CSS comments are R1's porter-visible half: translated for the JP porter, with no display effect either way.
- **Verify:** The pairs are diff.md's body sections in order; a Latin-prose scan of candidate.txt outside the banner, the license entries' proper nouns, and "SITE-225" returns only quotations and names.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the banner and proper nouns.

### 7. Links

- **What:** The candidate's outbound links are the credit source link (section 1; host matches the recorded host), the license entries' game-icons.net source links (kept verbatim on both sides — they are the assets' home and serve; they do not appear in the diff), and the three prose component links inside B4 (candidate L22). Two of the three name pages that exist on scp-jp under those names (`component:toggle-sidebar`, `component:betterfootnotes` — the same pages the tail includes use). The third, `[[[component:sigma-plus|Sigma Plus]]]`, names a same-site page scp-jp does not have: the JP port is `component:sigma-plus-jp`, which the candidate's own include (candidate L702) correctly names. That link is flagged in the per-theme record (item 3). No P11 tag-page or hub links exist in this theme on either side.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; a link naming a nonexistent same-site page is neither.
- **Verify:** `grep -n 'component:sigma-plus' candidate.txt` — L22 (the dead prose link) against L702 (the correct include).
- **Disposition:** Two links standing; the Sigma Plus prose link is flagged, not dispositioned (per-theme record, item 3).

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the candidate's single code exhibit and tail delivery sit where the original's sit (original L47–664 and L693–696 → candidate L58–676 and L705–708), and the JP corrections arrive as the head credit block and the tail include swaps, not interleaved into the inherited CSS. The classifier's five EXHIBIT-RESTRUCTURE primaries adjudicate to include and license lines, not exhibit changes: in B7 the image-block exhibit keeps its include, its image, and its caption (translated); in B42/B46 the license-box lines swap form (section 1); in B47/B49 the closing includes are repointed (sections 2–3). An exhibit census confirms the shape: the tabview and its two tabs, the table sample, the image-block exhibit, the font sample spans, and the three license entries are present on both sides in the same order — nothing was dropped or replaced, so the R3 question (sanctioned replacement vs silent deletion) does not arise for this theme. B31's selector correction is recorded in section 5, and B14's stack rewrite in section 4.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Fourteen WS-ONLY blocks (B17, B18, B20, B22, B24, B26, B27, B29, B34, B35, B38–B41), all whitespace-only line pairs inside the code exhibit. The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The WS-ONLY blocks are listed in classification.json; each pair differs only in whitespace.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none — no annotation signature fired over the 50 change blocks, and a direct check confirms it: the candidate carries no `[!--` comment and no editor line; the only comment head in the file is the original's own banner (section 6). The skeleton's "none" for this section survives contact with the bytes.
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Three dispositioned items, each with its ground, and three flagged items carried in the per-theme record. (1) T1's six pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host local--code and local--files lines (sections 3–4); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (2) The render row's two items, both environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40), and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). (3) The four image files of section 4: 404 on the draft host (probed 2026-11-17), the owner-deferred hosting state (KB-58), class (ii) — the files are uploaded or re-hosted at posting; the ledger §(c3) line for this theme names only the P1 disposition, so this package records the P5 outcome explicitly rather than leaving it implicit in the T4 charge. The ledger's determination for this theme is PASS and this package does not re-open it; the three flagged items below are the documentation doing its job, because each is visible in the bytes a reviewer reads today.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the per-theme items are flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 122): exit 1, 6 errors / 3 warns / 2 infos; all six errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-D (EN19)): FINDINGS, the two items of section 11(2), both dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 137, source LOCALIZE-S2-C): FINDINGS jointly, display-affecting findings 2 at measurement time (the duplicate Rate of the per-theme record and the four 404 assets of section 4); the pattern-1 sigma-plus charge and the credit-fields charge were answered in the bytes by FIX4-SIGMA and FIX2-CREDIT respectively, and the ledger §(c3) line records the theme's T4 outcome as P1 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +145/−133 in 50 change blocks / 19 hunks; the GNU-diff count of the same pair is 268 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:shoebill-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 137; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the kept bare Rate (KB-09 shape)

The original's only rating furniture is a bare `[[module rate]]` inside a `[[>]]` div at its head (original L3–5). The candidate installs the rate-bearing preview credit block at its head (candidate L3–12) and keeps the bare Rate directly below it (candidate L14–16), so the page carries two rating widgets. T4 charged exactly this shape at measurement time (pattern 3: "duplicate live `[[module rate]]` … outside the credit flow → two rating widgets — display-affecting"), at the line numbers the file then had. FIX2-CREDIT answered the charge's other half (the six missing fields) and no wave removed the Rate; no ledger line dispositions it for this theme. The campaign's standing rule is that the preview credit module is rate-bearing and a kept bare Rate is the KB-09 duplicate; the exemplar port of the same furniture (theme:jiha-jp) deleted it. This package flags the item with its lines and does not edit the candidate; the repair, if the coordinator orders one, is the deletion of candidate L14–16.

### Item 2 — the usage example's plain-slug self-reference

Candidate L27 reads `> [[include :scp-jp:theme:shoebill]]`, repointed from the original's `:scp-wiki:theme:shoebill` (original L16) in site prefix only. The candidate's posting name is theme:shoebill-jp, so the snippet a user pastes names a page that will not exist on scp-jp. T4 charged the same target at measurement time ("usage-sample include L21 also targets nonexistent `theme:shoebill`"). A population sweep owns this family across the candidates; this package flags the exact line and does not edit it.

### Item 3 — the prose Sigma Plus link

Candidate L22 links `[[[component:sigma-plus|Sigma Plus]]]`. On scp-jp there is no component:sigma-plus page; the JP port is component:sigma-plus-jp, which the candidate's own closing include (candidate L702) correctly names after FIX4-SIGMA. T5 charged the dead same-site component link at measurement time; the include was repaired and the prose link was not. The two component links beside it (toggle-sidebar, betterfootnotes) name pages scp-jp carries under those names, so only this one link is dead. Flagged with its line; the repair is a one-word target change, for the coordinator to land.

### Item 4 — the vendored T4 cell truncates

The vendored LOCALIZE-ROWS row 137 in review/AUTHORITIES/ledger-parts/ truncates its charge text mid-sentence ("usage-sample include L21 also targets …"). The full charge text survives in the campaign record (gosign2-lanes/lane-oc-gs-localize-s2-C/REPORT-body.md and sections/shoebill.md), and sections 11–12 and items 1–3 above were adjudicated against that full text. Record gap, noted so a reviewer working from the vendored authorities alone knows the cell is incomplete.

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-shoebill-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. `pages/component:sigma-plus-jp.txt` is the ruling-4 companion port the theme's base include names; it is a shared component with its own record, not part of this theme's diff. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
